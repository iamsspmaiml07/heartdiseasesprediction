# Heart Disease Prediction App

This repository contains a heart disease prediction application built using FastAPI for the backend and Streamlit for the frontend. The application uses a machine learning model to predict the presence of heart disease based on user inputs.

## Table of Contents

- [Overview](#overview)
- [Dataset](#dataset)
- [Model](#model)
- [Installation](#installation)
- [Usage](#usage)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

## Overview

This application predicts the likelihood of heart disease based on various medical parameters. It consists of:
- **Backend**: FastAPI to serve the machine learning model.
- **Frontend**: Streamlit to provide an interactive user interface.

## Dataset

The model is trained on the [Cleveland Heart Disease dataset](https://archive.ics.uci.edu/ml/datasets/heart+Disease) from the UCI Machine Learning Repository.

## Model

A logistic regression model is used for prediction. The model is trained on the dataset and saved using `joblib`.

## Installation

### Prerequisites

Ensure you have the following installed:
- Python 3.8 or higher
- pip (Python package installer)

### Steps

1. Clone this repository:
   ```sh
   git clone https://github.com/yourusername/heart-disease-prediction.git
   cd heart-disease-prediction
