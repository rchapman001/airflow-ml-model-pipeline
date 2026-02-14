# Airflow ML Model Pipeline

## Table of Contents

- [Overview](#overview)
- [Installation](#installation-and-set-up)
- [Usage](#usage)
- [Testing](#testing)
- [Code Formatting](#code-formatting)

## Overview

This project is a microservice based system for orchestrating end to end machine learning workflows.

- Architecture Overview:
  1. Scraper Service: Collects raw data from external sources and performs basic transformations to
    clean and normalize the data so it is ready for model training.
  2. Trainer Service: Consumes processed data and trains machine learning models.
  3. Prediction Service: Loads trained models and exposes REST endpoints for generating predictions
    based on new input data.
  4. UI Service: Provides a simple web interface for triggering training workflows and monitoring
    execution status. Communicates with Airflow using authenticated API calls.
  5. Airflow: Acts as the central orchestration layer, managing workflow execution, task
    dependencies, and retries.

- Tech Used: 
  1. Python: Primary programming language for all services.
  2. FastAPI: Web framework used to build REST APIs with Python
  3. Uvicorn: Web server used to run FastAPI applications.
  4. spaCy: Natural language processing library used for text processing.
  5. Apache Airflow: Workflow orchestration engine.
  6. Pipenv: Python dependency and virtual environment management.
  7. Bootstrap: Frontend framework used for the UI service.

## Installation and Set Up

1. Prerequisites: Before you begin, ensure you have the following installed on your machine:
    - [Visual Studio Code](https://code.visualstudio.com/download): This app is set up for VS Code,
      but you may use a different editor if you would like.
    - [Python](https://www.python.org/downloads/): Install Python version 3.11.4
        - To check if Python is installed, run the command below. If it is installed correctly
          you'll see its version number. 
            ```bash
            python --version
            ```
        - To check if pip is installed, run the command below. If it is installed correctly you'll
          see its version number. 
            ```bash
            pip --version
            ```
    - [Git](https://git-scm.com/downloads/)
        - To check if Git is installed, run the command below. If it is installed correctly you'll
          see its version number. 
            ```bash
            git --version
            ```
    - [Docker Desktop](https://www.docker.com/get-started/): To check if Docker is installed, run
      the command below. If it is installed correctly you'll see its version number.
        ```bash
        docker version
        ```
    - [Postman](https://www.postman.com/downloads/): Verify Postman was installed on your computer.

2. Clone Repository: 
    - Open a terminal or command prompt and run the following command to clone the repository:
        ```bash
        git clone https://github.com/rchapman001/airflow-ml-model-pipeline.git
        ```
      
3. Setup VS Code: 
    - Install the VS Code Extensions: Navigate to extensions.json file in .vscode folder and install
      all extensions listed in the file.
    - Set Java home path: Navigate to settings.json file in .vscode folder and set the
      `"java.jdt.ls.java.home"` setting to the correct path of your JDK installation.

4. Install Dependencies: Navigate to the root directory of this project. Install pipenv globally
   using this command: `pip install pipenv --user`. Then for each python project (every folder with
   a Pipfile), use pipenv to run the following commands to create a new virtual environment. 
    - Create the virtual environment and install all dependencies in the Pipfile: `pipenv install`
    - Recommended, if you want to automate this setup, you can run the `setup.sh` script from the
      root directory. This script will create the virtual environments and install all dependencies
      for all Python apps in the repository, so you don’t have to run `pipenv install` manually for
      each service.
    - Run this command from the root of the repository to make the script executable (macOS/Linux):
      `chmod +x ./scripts/setup.sh`
    - Run the setup script from the root of the repository to setup all virtual environments:
      `./scripts/setup.sh`

## Usage

- Local Development Environment
  - How to launch Airflow: Navigate to the airflow folder and run the following command. After
    Airflow starts, the username and password to login will be printed in the logs. Use these to
    authenticate in the ui or api.
    ```bash
    pipenv run airflow standalone
    ```
  - How to launch scraper-service: Navigate to the scraper-service folder and run the following
    command.
    ```bash
    APP_ENV=desktop pipenv run uvicorn app.main:app --host 0.0.0.0 --port 8001 --reload
    ```
  - How to launch trainer-service: Navigate to the trainer-service folder and run the following
    command.
    ```bash
    APP_ENV=desktop pipenv run uvicorn app.main:app --host 0.0.0.0 --port 8002 --reload
    ```
  - How to launch prediction-service: Navigate to the prediction-service folder and run the
    following command.
    ```bash
    APP_ENV=desktop pipenv run uvicorn app.main:app --host 0.0.0.0 --port 8003 --reload
    ```
  - How to launch ui-service: Navigate to the ui-service folder and run the following command.
    Before running this command you will have to update the airflow password for authentication in
    the .env.desktop file. After the ui-service starts, you can access it using this url:
    http://localhost:8004/ui-service/train
    ```bash
    APP_ENV=desktop pipenv run uvicorn app.main:app --host 0.0.0.0 --port 8004 --reload
    ```
  - Postman: With the backend services and their dependencies running. Open Postman and import the
    Postman collection located here: docs/airflow-ml-model-pipeline.postman_collection.json to
    interact with the backend using the predefined requests.
    - Airflow API: For the Airflow API there is a request to generate a bearer token. Use that
      request in any api calls you want to make to the Airflow API.
  - How to shutdown Airflow: With the Docker extension installed, right click the
    docker-compose-local.yml file and select 'Compose Down'. Alternatively, you can run the
    following command in the directory where the docker-compose.yml file is located: `docker compose
    -f docker-compose-local.yml down`
  - How to shutdown python backend services: type `ctrl + c` in the terminal. 
  - If you want to completely restart airflow and clear all data run the following command in the
    terminal: `Remove DB: rm -rf ~/airflow`.
  - If an app fails to start and it doesn't properly kill the app you may have to manually kill the
    app on the port. To see everything running on a specific port run: `lsof -i :8003`. Then to kill
    the app run `kill -9 <pid> <pid>`

## Testing

TODO

## Code Formatting
This repository uses automated code formatting tools to help maintain consistency in this code base.
Follow the below guidelines to maintain these guidelines.

1. [Black](https://github.com/psf/black) is a Python code formatter that ensures consistent code
   style by automatically formatting Python code according to PEP 8 standards. To format your code
   using Black.
    - Install Black if you haven't already:
      ```bash
      pip install black
      ```
    - Run Black on your Python files:
      ```bash
      black --line-length 100 your_python_file.py
      ```
  - If you want to automatically format your Python code using black before committing, follow these
    steps.
    - Install Black if you haven't already: `pip install black` 
    - Set the custom Git hooks path: Run the following command to configure Git to use the .githooks
      directory for hooks. `git config core.hooksPath .githooks`
    - Make the pre-commit script executable: Ensure that the pre-commit hook script in the .githooks
      directory is executable. `chmod +x .githooks/pre-commit`


2. [rewrap](https://github.com/staabm/vscode-rewrap) is a Visual Studio Code extension that wraps
   comments and other text to a specified line length, improving readability. To use rewrap in VS
   Code:
    - Install the rewrap extension from the Visual Studio Code Marketplace.
    - Set the desired line length for wrapping comments in your `settings.json`:
      ```json
      {
          "editor.wordWrap": "wordWrapColumn", // Rewrap setting
          "editor.wordWrapColumn": 100, // Rewrap setting
          "editor.rulers": [100], // Rewrap setting
      }
      ```
    - With your cursor in the comment block, press the appropriate keyboard shortcut (usually Alt+Q
      or Alt+Shift+Q) to rewrap the comment to the specified line length.