# Breast Cancer Prediction

**Status: In Progress** 🚧

This project is currently under development. Contributions and feedback are welcome!

# Overview

This project utilizes machine learning techniques to predict the likelihood of breast cancer based on a dataset of features extracted from medical imaging. The project includes a Jupyter Notebook that covers data preprocessing, model training, evaluation, and predictions. The environment is fully Dockerized for ease of replication and deployment.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Environment Details](#environment-details)
- [Installation](#installation)
- [Usage](#usage)
- [Docker](#docker)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

# Features

- **Data Preprocessing**: Cleaning and preparing data for machine learning models.
- **Modeling**: Logistic Regression, SVM, and Random Forest models.
- **Evaluation**:
  - ***Metrics***: Accuracy, precision, recall, and F1-score.
  - ***Confusion Matrix***: Visual representation of the performance of the classification model.
  - ***ROC Curve***: Receiver Operating Characteristic curve to evaluate the model's ability to distinguish between classes.
- **Prediction**: Predicting the likelihood of breast cancer.
- **Dockerized Environment**: Consistent setup using Docker.

# Environment Details

- **Python Version**: 3.10.12
- **Libraries**:
  - `numpy`: 1.26.4
  - `pandas`: 2.1.4
  - `seaborn`: 0.13.1
  - `scikit-learn`: 1.3.2
  - `ucimlrepo`

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

### Running Jupyter Notebook

```bash
jupyter notebook notebooks/breast_cancer_prediction.ipynb
```

# Docker

### Prerequisites
A [Play with Docker](https://labs.play-with-docker.com/) account. No local Docker installation required.

### Steps to Run with Play with Docker

1. **Start a New Session**: Go to [Play with Docker](https://labs.play-with-docker.com/) and click "Start".

2. **Add a New Instance**: Click "ADD NEW INSTANCE".
   
3. **Clone the Repository**: 
```bash
git clone https://github.com/Ilagri/Breast-cancer-prediction.git
cd Breast-cancer-prediction
```

4. **Build the Docker Image**: 
```bash
docker build -t breast-cancer-prediction .
```

5. **Run the Docker Container**: 
```bash
docker run -p 8888:8888 breast-cancer-prediction
```

6. **Access Jupyter Notebook**:
- Click on the 8888 link in [Play with Docker](https://labs.play-with-docker.com/).
- Enter the Jupyter token from the terminal.
- Navigate to breast_cancer_prediction.ipynb to start working.

# Project Structure
```bash
Breast-cancer-prediction/
├── notebooks/                    # Jupyter notebooks
│   └── breast_cancer_prediction.ipynb
├── Dockerfile                    # Docker configuration
├── requirements.txt              # Python dependencies
└── README.md                     # Project documentation
```

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

- **Dataset:** The Breast Cancer Wisconsin (Diagnostic) Dataset by Dr. William H. Wolberg is available through the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+%28Diagnostic%29).
***Citation:*** W. H. Wolberg, W. N. Street, and O. L. Mangasarian. (1992). "Breast Cancer Wisconsin (Diagnostic) Data Set".
  
- **Mentorship and Feedback:** Special thanks to Dr. Veronica Maidel for her invaluable feedback and mentoring.
  
- **Tools and Libraries**: Thanks to the open-source community.
