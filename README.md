# Breast Cancer Prediction (In progress)
This project uses machine learning techniques to predict breast cancer based on a dataset of features extracted from medical imaging. The project includes a Jupyter Notebook that details the data preprocessing, model training, evaluation, and predictions.

# Overview

This project utilizes machine learning techniques to predict the likelihood of breast cancer based on a dataset of features extracted from medical imaging. The project includes a Jupyter Notebook that covers data preprocessing, model training, evaluation, and predictions. The environment is fully Dockerized for ease of replication and deployment.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Docker](#docker)
  - [Prerequisites](#prerequisites)
  - [Steps to Run with Docker](#steps-to-run-with-docker)
  - [Pull from Docker Hub](#pull-from-docker-hub)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Features

- **Data Preprocessing**: Clean and prepare data for machine learning models.
- **Modeling**: Implementation of various machine learning models including Logistic Regression, Support Vector Machine (SVM), and Random Forest.
- **Evaluation**: Model evaluation using accuracy, precision, recall, and F1-score.
- **Prediction**: Predict the likelihood of breast cancer using trained models.
- **Dockerized Environment**: Simplified setup using Docker for consistent and reproducible results.

## Installation

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

If you don't have pip installed, you can follow the instructions here (https://pip.pypa.io/en/stable/installation/) to install it.

## Usage

After installing the necessary dependencies, you can run the Jupyter Notebook to explore the code, run experiments, and view the results.

### Running Jupyter Notebook
To start the Jupyter Notebook server, run the following command:

```bash
jupyter notebook notebooks/breast_cancer_prediction.ipynb
```

This command will start the Jupyter Notebook server and open a new tab in your web browser where you can interact with the notebook.

### Docker
To simplify running the project and avoid dependency issues, you can use Play with Docker [Play with Docker](https://labs.play-with-docker.com/).

### Prerequisites
Ensure you have a Play with Docker account. No local Docker installation is necessary.

### Steps to Run with Play with Docker

#### 1. Build the Docker Image
Build the Docker image using the provided Dockerfile:

```bash
docker build -t breast-cancer-prediction .
```
#### 2. Run the Docker Container
```bash
docker run -p 8888:8888 breast-cancer-prediction
```
#### 3. Access Jupyter Notebook
Open your browser and navigate to http://localhost:8888. You should see the Jupyter Notebook interface where you can navigate to and open the breast_cancer_prediction.ipynb file.

## Project Structure
```bash
Breast-cancer-prediction/
├── notebooks/                    # Jupyter notebooks
│   └── breast_cancer_prediction.ipynb
├── Dockerfile                    # Docker configuration
├── requirements.txt              # Python dependencies
└── README.md                     # Project documentation
```

## Contributing
Contributions are welcome! Please follow these steps to contribute:

1. ***Fork the repository***: Click the "Fork" button at the top-right corner of this page to create a copy of this repository under your GitHub account.
2. ***Create a new branch***:
  ```bash
  git checkout -b feature-name
  ```
3. ***Make your changes***: Implement your changes or additions.
4. ***Commit your changes***:
  ```bash
  git commit -m 'Add some feature'
  ```
5. ***Push to the branch***:
  ```bash
  git push origin feature-name
  ```
6. ***Open a pull request***: Go to your forked repository on GitHub, click on the "Pull Request" button, and provide a description of your changes.

## License
This project is licensed under the MIT License - see the LICENSE [LICENCE](https://github.com/Ilagri/Breast-cancer-prediction/blob/main/LICENSE) file for details.

## Acknowledgements

- **Dataset:** The Breast Cancer Wisconsin (Diagnostic) Dataset was created by Dr. William H. Wolberg, a physician at the University of Wisconsin-Madison, and it has been widely used for research and educational purposes. The dataset is publicly available through the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+%28Diagnostic%29).
- **Citation:** W. H. Wolberg, W. N. Street, and O. L. Mangasarian. (1992). "Breast Cancer Wisconsin (Diagnostic) Data Set". UCI Machine Learning Repository.

- **Mentorship and Feedback:** A special thanks to Dr. Veronica Maidel for her invaluable feedback and mentoring throughout this project.

- Special thanks to the open-source community for providing the tools and libraries that made this project possible.
- Inspiration and guidance were drawn from various tutorials, research papers, and online courses.

