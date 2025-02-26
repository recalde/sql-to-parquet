# SQL to Parquet Converter

This program clones a Git repository, scans for `.sql` files, extracts `CREATE TABLE` and `INSERT INTO` statements, and converts the extracted data into Parquet files.

## Prerequisites

- Docker installed
- Git repository with `.sql` files containing `CREATE TABLE` and `INSERT INTO` statements

## Running in Docker

1. Build the Docker image:
   ```sh
   docker build -t sql-to-parquet .
   ```

2. Run the container with environment variables:
   ```sh
   docker run -e GIT_REPO_URL="https://github.com/example/repo.git" -e CLONE_DIR="./repo_clone" -e OUTPUT_DIR="./parquet_output" sql-to-parquet
   ```

Parquet files will be saved in the `parquet_output` directory.

## Running Locally

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/sql-to-parquet.git
   cd sql-to-parquet
   ```

2. Install the required Python packages:
   ```sh
   pip install -r requirements.txt
   ```

3. Run the script:
   ```sh
   python program.py
   ```

Parquet files will be saved in the `parquet_output` directory.

## Configuration

You can configure the Git repository URL, clone directory, and output directory by modifying the following variables in `program.py`:

- `GIT_REPO_URL`: URL of the Git repository to clone
- `CLONE_DIR`: Directory to clone the repository into
- `OUTPUT_DIR`: Directory to save the Parquet files

## Environment Variables

- `GIT_REPO_URL`: URL of the Git repository to clone.
- `CLONE_DIR`: Directory to clone the repository into.
- `OUTPUT_DIR`: Directory to save the Parquet files.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.