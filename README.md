# House Price Prediction Project

## Overview

This project implements a House Price Prediction system that employs a linear regression model to estimate the price of a house based on essential factors, including the area, number of bedrooms, and the age of the house. The project is split into two main components: a Jupyter Notebook for model development and a Python script for user input and price prediction using a joblib model.

## Table of Contents

- [Introduction](#introduction)
- [Project Components](#project-components)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Data](#data)
- [Linear Regression Model](#linear-regression-model)


## Introduction

The House Price Prediction Project simplifies the process of estimating house prices, making it accessible to both potential homebuyers and real estate professionals. It allows users to input essential property details and receive accurate price estimates, enhancing their decision-making process.

## Project Components

1. **Jupyter Notebook (Model Development):** 
    - The `HousePricePrediction.ipynb` file contains the Jupyter Notebook that covers the development of the linear regression model. It includes explanations, code, and visualization of the model training process.

2. **Python Script (User Interface):**
    - The `main.py` script provides a user-friendly interface for entering property details. It loads the pre-trained model using joblib and generates house price predictions based on user input.

## Prerequisites

Before using this project, ensure you have the following prerequisites:

- Python 3.6+
- Required Python libraries (specified in the requiremnts.txt file)
- Jupyter Notebook for model development

## Installation

1. Clone or download this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/house-price-prediction.git
   ```

2. Navigate to the project directory:

   ```bash
   cd house-price-prediction
   ```

## Usage

1. **Model Development (Jupyter Notebook):**
    - Open the Jupyter Notebook, `HousePricePrediction.ipynb`, using Jupyter Notebook or Jupyter Lab. Follow the step-by-step guide within the notebook for model development.

2. **User Interface (Python Script):**
    - Run the Python script, `main.py`, which provides a user-friendly interface for entering property details. The script loads the pre-trained model using joblib and generates house price predictions based on user input.

## Data

The project utilizes a dataset that includes information about various properties, such as area, number of bedrooms, house age, and actual sale prices. This dataset is used for training the linear regression model.

## Linear Regression Model

The House Price Prediction model is based on linear regression, a machine learning algorithm that analyzes relationships between property features and sale prices. The model's predictions are based on the coefficients learned during the training process.


