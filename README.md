# Fake News Detection

This is a simple Flask web application for detecting fake news using a neural network model. Users can input news articles, and the application will classify them as either "Real" or "Fake".

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Technologies](#technologies)
- [CI/CD with GitHub Actions](#CI/CD with GitHub Actions)
- [Future Enhancements](#FutureEnhancements)

## Features

- **Dockerized Application**: The app is containerized using Docker for consistent deployment across different environments.
- **CI/CD Pipeline**: Automated testing, building, and deployment managed using GitHub Actions.

### Prerequisites

1. **Docker**: [Install Docker](https://docs.docker.com/get-docker/)

---

### Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/DrFranko/Fake-News-Detection.git
    cd Fake-News-Detection
    ```

2. **Build Docker Image**:
    ```bash
    docker build -t fake-news-app:latest .
    ```

3. **Run Docker Container**:
    ```bash
    docker run --rm -p 5000:5000 fake-news-app:latest
    ```

---

## CI/CD with GitHub Actions

This repository is configured with GitHub Actions for Continuous Integration and Deployment. Upon each push, the following steps are executed:

1. **Flake8 Linting**: Ensures code quality by checking for syntax and style issues.
2. **Docker Build**: Builds the Docker image.

---

## Future Enhancements

- **Production-Ready Setup**: More features will be included.
- **Better Interface**: Beautiful UI and more complex queries will be added.
- **Dataset Inclusion**: Robust Model with better datasets will be included.

---
