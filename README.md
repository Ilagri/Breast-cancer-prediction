# Breast Cancer Prediction

**Status: In Progress** 🚧

This project is currently under development. Contributions and feedback are welcome!

# Overview

This project uses machine learning to predict breast cancer likelihood based on features from medical imaging. It includes a Jupyter Notebook for model development and a Flask web application for serving the model as an API or web interface.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Environment Details](#environment-details)
- [Installation](#installation)
- [Usage](#usage)
- [Docker](#docker)
  - [Jupyter Notebook](#jupyter_notebook)
  - [Flask Web Application](#flask_web_application)
  - [Using Play with Docker](#using_play_with_docker)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

# Features

- **Data Preprocessing**: Cleaning and preparing data for machine learning models.
- **Modeling**: Logistic Regression, SVM, and Random Forest models.
- **Evaluation**: Accuracy, precision, recall, F1-score, confusion matrix, ROC curve.
- **Prediction**: Predicting the likelihood of breast cancer.
- **Dockerized Environment**: Consistent setup using Docker.
- **Flask Web Application**: API or web interface, deployed in production using Docker.

# Environment Details

- **Python Version**: 3.10.12
- **Libraries**:
  - `numpy`: 1.26.4
  - `pandas`: 2.1.4
  - `seaborn`: 0.13.1
  - `scikit-learn`: 1.3.2
  - `ucimlrepo`

# Project Structure
```bash
Breast-cancer-prediction/
├── data/                         # Dataset directory
│   └── dataset.csv               # The dataset used for training and evaluation
├── notebooks/                    # Jupyter notebooks
│   └── breast_cancer_prediction.ipynb
├── flask_app/                    # Flask app directory
│   ├── app.py                    # Flask application
│   ├── templates/                # HTML templates for Flask
│   ├── model.pkl                 # Pre-trained machine learning model
│   ├── Dockerfile                # Docker configuration for Flask app
│   └── requirements.txt          # Python dependencies for Flask app
├── Dockerfile                    # Docker configuration for Jupyter Notebook
├── requirements.txt              # Python dependencies for Jupyter Notebook
└── README.md                     # Project documentation
```

# Installation

To get started with this project, clone the repository and install the necessary dependencies.

### Clone the Repository
```bash
git clone https://github.com/Ilagri/Breast-cancer-prediction.git
cd Breast-cancer-prediction
```

### Install Dependencies

This project relies on Python and several libraries. You can install the dependencies using pip:
```bash
pip install -r requirements.txt
```

If you don't have pip installed, you can follow the instructions [here](https://pip.pypa.io/en/stable/installation/) to install it.

# Usage
After installing the necessary dependencies, you can run the Jupyter Notebook to explore the code, run experiments, and view the results.

### Running Jupyter Notebook

To start the Jupyter Notebook server, run the following command:
```bash
jupyter notebook notebooks/breast_cancer_prediction.ipynb
```
This command will start the Jupyter Notebook server and open a new tab in your web browser where you can interact with the notebook.

# Docker

## Jupyter Notebook
Run the Jupyter Notebook:

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

## Flask Web Application
Run the Flask app:

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

Access the web app at http://localhost:5000.

## Using Play with Docker
1. Start a New Session on [Play with Docker](https://labs.play-with-docker.com/) and add an instance.
2. Clone the Repo:
```bash
git clone https://github.com/Ilagri/Breast-cancer-prediction.git
cd Breast-cancer-prediction
```
3. Build / Pull and Run the Docker container as described above.


# Contributing
Contributions are welcome! Please follow these steps:

1. **Fork the repository** on GitHub.
   
2. **Create a new branch**:
  ```bash
  git checkout -b feature-name
  ```
3. **Make your changes**.
   
4. **Commit your changes**:
  ```bash
  git commit -m 'Add some feature'
  ```
5. **Push to the branch**:
  ```bash
  git push origin feature-name
  ```
6. **Open a pull request** on GitHub.

# License
This project is licensed under the MIT License - see the [LICENCE](https://github.com/Ilagri/Breast-cancer-prediction/blob/main/LICENSE) file for details.

# Acknowledgements

- **Dataset:** The Breast Cancer Wisconsin (Diagnostic) Dataset was created by Dr. William H. Wolberg and is available from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+%28Diagnostic%29). 
- **Mentorship and Feedback:** Special thanks to Dr. Veronica Maidel for her invaluable feedback and mentoring.
