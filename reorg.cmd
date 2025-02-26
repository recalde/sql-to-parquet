@echo off

:: Create directories
mkdir docker
mkdir scripts
mkdir src
mkdir tests

:: Move Docker-related files
git mv Dockerfile docker/
git mv docker-build-and-push.sh docker/

:: Move shell scripts
git mv run_program.sh scripts/

:: Move Python source files
git mv program.py src/main.py
git mv utils.py src/

:: Move test files
git mv test_program.py tests/test_main.py

:: Stage the changes
git add .

:: Commit the changes
git commit -m "Reorganized project structure"