# Docker Project: Word Count and Analysis

This Docker project aims to perform word count and analysis on text files within a Docker container environment. It includes a Python script that reads text files, counts the number of words, lists the top words, and extracts information such as the IP address of the machine.

## Getting Started

To use this project, follow these steps:

### Prerequisites

- Docker installed on your system

### Usage

1. Clone this repository to your local machine.
2. Navigate to the project directory.

### Build the Docker Image

```bash
docker build -t proj2docker_rk .

```
### Run the Docker Container
```bash

docker run proj2docker_rk 
```

### Project Structure
```bash
Dockerfile: Defines the steps to build the Docker image.

script.py: Python script to perform word count and analysis.

IF.txt: Sample input text file.

Limerick-1.txt: Sample input text file.

```

### Additional Notes

Ensure that your input text files are placed in the TextFiles directory.

Modify the script.py file if you need to customize the word counting and analysis logic.

For more detailed instructions, refer to the comments in the Python script.

### Contributor

Saumick Pradhan

### License

This project is licensed under the MIT License. Feel free to modify and expand upon this template to better suit your project's needs. You can include additional sections such as "Troubleshooting", "Contributing Guidelines", or "References" if necessary.

