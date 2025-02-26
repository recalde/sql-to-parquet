import os
import re
import git
import sqlparse
import pandas as pd
import pyarrow.parquet as pq
from collections import defaultdict

GIT_REPO_URL = "https://github.com/example/repo.git"
CLONE_DIR = "./repo_clone"
OUTPUT_DIR = "./parquet_output"

# Regex patterns
CREATE_TABLE_PATTERN = re.compile(r'CREATE TABLE (\w+)\s*\((.*?)\);', re.S)
INSERT_PATTERN = re.compile(r'INSERT INTO (\w+)\s*\((.*?)\) VALUES (.*?);', re.S)

# Clone the repository
def clone_repo():
    if os.path.exists(CLONE_DIR):
        os.system(f"rm -rf {CLONE_DIR}")
    git.Repo.clone_from(GIT_REPO_URL, CLONE_DIR)

# Extract SQL files
def get_sql_files():
    sql_files = []
    for root, _, files in os.walk(CLONE_DIR):
        for file in files:
            if file.endswith(".sql"):
                sql_files.append(os.path.join(root, file))
    return sql_files

# Parse CREATE TABLE statements
def extract_table_schemas(sql_text):
    tables = {}
    for match in CREATE_TABLE_PATTERN.finditer(sql_text):
        table_name, columns = match.groups()
        column_defs = [col.strip().split(" ")[0] for col in columns.split(",")]
        tables[table_name] = column_defs
    return tables

# Parse INSERT statements
def extract_insert_data(sql_text):
    data = defaultdict(list)
    for match in INSERT_PATTERN.finditer(sql_text):
        table_name, columns, values = match.groups()
        columns = [col.strip() for col in columns.split(",")]
        rows = re.findall(r'\((.*?)\)', values)
        for row in rows:
            row_values = [v.strip().strip("'") for v in row.split(",")]
            data[table_name].append(dict(zip(columns, row_values)))
    return data

# Convert extracted data to Parquet
def save_to_parquet(table_name, rows):
    df = pd.DataFrame(rows)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    parquet_file = os.path.join(OUTPUT_DIR, f"{table_name}.parquet")
    df.to_parquet(parquet_file, engine="pyarrow")
    print(f"Saved {table_name}.parquet")

# Main execution
def main():
    clone_repo()
    sql_files = get_sql_files()
    table_schemas = {}
    insert_data = defaultdict(list)
    
    for file in sql_files:
        with open(file, "r") as f:
            sql_text = f.read()
            table_schemas.update(extract_table_schemas(sql_text))
            new_data = extract_insert_data(sql_text)
            for table, rows in new_data.items():
                insert_data[table].extend(rows)
    
    for table, rows in insert_data.items():
        save_to_parquet(table, rows)

if __name__ == "__main__":
    main()
