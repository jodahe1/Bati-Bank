# Bati-Bank

This repository is dedicated to building predictive models and analytical tools to enhance the operations and services of Bati Bank. The project focuses on developing a **Credit Scoring Model** to enable a **buy-now-pay-later service** in collaboration with an eCommerce platform. The goal is to assess the creditworthiness of customers, minimize default risks, and provide optimal loan terms.

---

## Table of Contents

- [Introduction](#introduction)
- [Business Objective](#business-objective)
- [Key Insights and Analysis](#key-insights-and-analysis)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

---

## Introduction

The **Bati-Bank** project leverages data analytics and machine learning to build a **Credit Scoring Model** for Bati Bank. The model aims to:

1. **Assess Creditworthiness**: Predict the likelihood of customer defaults.
2. **Enable Buy-Now-Pay-Later Services**: Provide customers with the ability to purchase products on credit.
3. **Optimize Loan Terms**: Predict the optimal loan amount and duration for each customer.


The analysis includes **Exploratory Data Analysis (EDA)**, **Feature Engineering**, **Model Building**, and **Model Evaluation**.

---

## Business Objective

The primary business objective is to create a **Credit Scoring Model** for Bati Bank’s partnership with an eCommerce company. The specific goals include:

1. **Define a Proxy Variable**: Categorize users as **high-risk (bad)** or **low-risk (good)** based on their creditworthiness.
2. **Select Predictive Features**: Identify features that correlate with the proxy variable.
3. **Develop Risk Probability Model**: Assign a risk probability to each customer.
4. **Develop Credit Scoring Model**: Assign a credit score to each customer.
5. **Predict Optimal Loan Amount and Duration**: Determine the best loan terms for each customer.

By implementing this model, Bati Bank aims to make informed decisions, minimize default risks, and provide a reliable buy-now-pay-later service.

---

## Key Insights and Analysis

### 1. **Exploratory Data Analysis (EDA)**
   - **Dataset Overview**: 95,662 rows and 16 columns.
   - **Key Findings**:
     - Most transactions are from **Uganda** (Currency Code: UGX, Country Code: 256.0).
     - **ProductId 6** and **ProductCategory "financial_services"** are the most popular.
     - **ChannelId 3** is the predominant channel for transactions.
     - **FraudResult**: 95,469 transactions are non-fraudulent (FraudResult = 0).

### 2. **Feature Engineering**
   - **Aggregate Features**:
     - Total Transaction Amount
     - Average Transaction Amount
     - Transaction Count
     - Standard Deviation of Transaction Amounts
   - **Extracted Features**:
     - Transaction Hour, Day, Month, and Year to capture temporal trends.

### 3. **Model Building**
   - **Models Used**:
     - Logistic Regression
     - Decision Trees
     - Random Forest
     - Gradient Boosting Machines (GBM)
   - **Hyperparameter Tuning**: Grid Search and Random Search for optimal performance.

### 4. **Model Evaluation**
   - **Evaluation Metrics**:
     - Accuracy, Precision, Recall, F1 Score, ROC-AUC.
   - **Key Findings**:
     - Higher transaction amounts are moderately correlated with fraudulent transactions (Correlation Coefficient: 0.557).
     - Weak negative correlation between **Amount** and **PricingStrategy** (Correlation Coefficient: -0.0619).

---

## Installation

To get started with this project, clone the repository and install the required dependencies.

```bash
git clone https://github.com/jodahe1/Bati-Bank.git
cd Bati-Bank
```

---

## Usage

1. Navigate to the project directory.
2. Open the Jupyter Notebook files to explore the data analysis and model-building process.
3. Run the notebooks to reproduce the results or modify them for your own analysis.

---

## Project Structure

The project is structured into the following key phases:

1. **Data Loading and Exploration**:
   - Load datasets and perform initial checks (e.g., missing values, duplicates).
   - Explore basic statistics and data distributions.

2. **Exploratory Data Analysis (EDA)**:
   - Visualize key insights such as survival rates, transaction trends, and fraud detection.

3. **Feature Engineering**:
   - Create aggregate and extracted features to enhance model performance.

4. **Model Building**:
   - Train and evaluate machine learning models (e.g., Logistic Regression, Random Forest).

5. **Model Evaluation**:
   - Assess model performance using metrics like accuracy, precision, recall, and ROC-AUC.

6. **Credit Scoring and Risk Assessment**:
   - Develop a credit scoring model and predict optimal loan terms.

---

## Contributing

We welcome contributions to improve the project. To contribute, follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
