# Breast Cancer Prediction

**Status: In Progress** 🚧

This project is currently under development. Contributions and feedback are welcome!

# Overview

This repository demonstrates a machine learning approach to predict breast cancer likelihood based on features derived from medical imaging. It includes a Jupyter Notebook for model development and evaluation, as well as a Flask web application that serves the model through a user-friendly interface. The Flask app is containerized using Docker, enabling easy deployment.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation and Usage](#installation_and_usage)
  - [Docker](#docker)
    - [Running the Jupyter Notebook](#running_jupyter_notebook)
    - [Running the Flask Web Application](#running_flask_web_application)
  - [Local Installation] (#local_Installation)
  - [Jupyter Notebook](#jupyter_notebook)
  - [Flask Web Application](#flask_web_application)
  - [Using Play with Docker](#using_play_with_docker)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [Environment Details](#environment-details)
- [License](#license)
- [Acknowledgements](#acknowledgements)

# Features

- **Jupyter Notebook**: Includes data preprocessing (cleaning and preparing data for machine learning models), modeling (Logistic Regression, SVM, and Random Forest models), evaluation (accuracy, precision, recall, F1-score, confusion matrix, ROC curve), and prediction (predicting the likelihood of breast cancer).
- **Flask Web Application**: A web interface for breast cancer prediction, allowing users to interact with the model.
- **Dockerized Environment**: Both the Jupyter Notebook and the web application are containerized using Docker, ensuring consistent setup and easy deployment across different environments.


# Installation and Usage

To get started, clone the repository and choose how you want to run the Jupyter Notebook and Flask web application—either by installing the necessary dependencies locally or by using Docker.

## Option 1: Using Play with Docker
If you prefer an easy, browser-based solution, you can use [Play with Docker](https://labs.play-with-docker.com/).
You can run both the Jupyter Notebook and Flask web application using [Play with Docker](https://labs.play-with-docker.com/), either by building the images locally or by pulling them from Docker Hub.

1. Start a New Session on [Play with Docker](https://labs.play-with-docker.com/) and add an instance.
2. Clone the repository:
```bash
git clone https://github.com/Ilagri/Breast-cancer-prediction.git
cd Breast-cancer-prediction
```
3. Build and run the Docker containers as described below.

### Running the Jupyter Notebook

- **Option 1: Build Locally**

```bash
docker build -t breast-cancer-prediction .
docker run -p 8888:8888 breast-cancer-prediction
```

- **Option 2: Pull from Docker Hub**

```bash
docker pull ilagri/breast-cancer-prediction:latest
docker run -p 8888:8888 ilagri/breast-cancer-prediction:latest
```

Access the notebook at http://localhost:8888.

## Running the Flask Web Application

- **Option 1: Build Locally**

```bash
cd flask_app
docker build -t flask-app .
docker run -p 5000:5000 flask-app
```
- **Option 2: Pull from Docker Hub**

```bash
docker pull ilagri/flask-app:latest
docker run -p 5000:5000 ilagri/flask-app:latest
```
Access the Web Application: Open your browser and navigate to http://localhost:5000 to interact with the web app.

   
### Install Dependencies

This project relies on Python and several libraries. You can install the dependencies using pip:
```bash
pip install -r requirements.txt
```

If you don't have pip installed, you can follow the instructions [here](https://pip.pypa.io/en/stable/installation/) to install it.

# Project Structure
```bash
Breast-cancer-prediction/
├── notebooks/                    # Jupyter notebooks
│   └── breast_cancer_prediction.ipynb
├── flask_app/                    # Flask app directory
│   ├── data/                     # Dataset directory
│   │   └── dataset.csv           # The dataset used for prediction
│   ├── app.py                    # Flask application
│   ├── templates/                # HTML templates for Flask
│   ├── model.pkl                 # Pre-trained machine learning model
│   ├── Dockerfile                # Docker configuration for Flask app
│   └── requirements.txt          # Python dependencies for Flask app
├── Dockerfile                    # Docker configuration for Jupyter Notebook
├── requirements.txt              # Python dependencies for Jupyter Notebook
└── README.md                     # Project documentation
```

# Environment Details

- **Python Version**: 3.10.12
- **Libraries**:
  - `numpy`: 1.26.4
  - `pandas`: 2.1.4
  - `seaborn`: 0.13.1
  - `scikit-learn`: 1.3.2
  - `ucimlrepo`

# License
This project is licensed under the MIT License - see the [LICENCE](https://github.com/Ilagri/Breast-cancer-prediction/blob/main/LICENSE) file for details.

# Acknowledgements

- **Dataset:** The Breast Cancer Wisconsin (Diagnostic) Dataset was created by Dr. William H. Wolberg and is available from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+%28Diagnostic%29). 
- **Mentorship and Feedback:** Special thanks to Dr. Veronica Maidel for her invaluable feedback and mentoring.

