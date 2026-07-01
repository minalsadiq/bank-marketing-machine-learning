# 🏦 Bank Marketing Subscription Prediction using Machine Learning

## 📌 Project Overview

This project develops an end-to-end Machine Learning pipeline to predict whether a customer will subscribe to a bank term deposit. The solution follows the complete Data Science workflow, including data profiling, exploratory data analysis (EDA), preprocessing, feature engineering, model training, evaluation, cross-validation, hyperparameter tuning, and experiment tracking.

The goal is to help financial institutions improve the efficiency of their marketing campaigns by identifying customers who are most likely to subscribe to a term deposit.

---

# 🎯 Business Problem

Banks spend significant time and resources contacting customers during marketing campaigns. However, only a small percentage of customers subscribe to a term deposit.

By using Machine Learning, banks can identify high-potential customers before launching campaigns, reducing operational costs while increasing marketing efficiency and conversion rates.

---

# 📊 Dataset Information

**Dataset:** UCI Bank Marketing Dataset

**Source:** https://archive.ics.uci.edu/ml/datasets/bank+marketing

**Number of Records:** 41,188

**Number of Features:** 20 Predictor Variables + 1 Target Variable

**Target Variable**

```
y

yes = Customer subscribed
no  = Customer did not subscribe
```

---

# 🚀 Project Workflow

## 📒 Notebook 01 — Data Profiling

Performed:

- Dataset inspection
- Shape analysis
- Data types
- Missing value analysis
- Duplicate analysis
- Statistical summary
- Target variable analysis
- Numerical feature distributions
- Categorical feature distributions
- Correlation analysis
- Data profiling report generation

---

## 📒 Notebook 02 — Data Preprocessing

Performed:

- Removed duplicate records
- Removed duration feature
- Handled unknown categories
- Label encoding
- Feature scaling
- Train-Test Split
- Saved processed dataset
- Saved scaler
- Saved feature names
- Saved training/testing datasets

---

## 📒 Notebook 03 — Model Building

Implemented:

- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier

Evaluation Metrics:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC AUC
- Confusion Matrix
- Classification Report

Feature Importance Analysis:

- Random Forest Feature Importance
- Top 10 Important Features

---

## 📒 Notebook 04 — Advanced Machine Learning Models

Implemented:

- XGBoost
- LightGBM
- CatBoost

Compared:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC AUC

Selected the best-performing advanced model.

---

## 📒 Notebook 05 — Cross Validation + MLflow + Hyperparameter Tuning

Implemented:

- Stratified K-Fold Cross Validation
- MLflow Experiment Tracking
- Optuna Hyperparameter Tuning
- Best Parameter Selection
- Best Model Saving
- Trial History Saving

---

# 📈 Machine Learning Models Used

### Traditional Models

- Logistic Regression
- Decision Tree
- Random Forest

### Advanced Models

- XGBoost
- LightGBM
- CatBoost

---

# 📏 Evaluation Metrics

The following metrics were used for model evaluation:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC AUC Score
- Cross Validation Accuracy

---

# ⚙️ Technologies Used

## Programming Language

- Python 3.11

## Libraries

- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- XGBoost
- LightGBM
- CatBoost
- Optuna
- MLflow
- Joblib
- YData Profiling

---

# 📂 Project Structure

```
bank_marketing_project/
│
├── data/
│   └── raw/
│       └── bank-additional/
│
├── notebooks/
│   ├── 01 Data Profiling.ipynb
│   ├── 02 Data Preprocessing.ipynb
│   ├── 03 Model Building.ipynb
│   ├── 04 Advanced Machine Learning Models.ipynb
│   └── 05 Cross Validation + MLflow + Hyperparameter Tuning.ipynb
│
├── reports/
│   ├── figures/
│   ├── bank_marketing_profile.html
│   ├── feature_importance.csv
│   ├── model_comparison.csv
│   ├── model_comparison_advanced.csv
│   ├── best_parameters.csv
│   └── optuna_trials.csv
│
├── src/
│   ├── data/
│   │   └── processed/
│   │       ├── bank_clean.csv
│   │       └── bank_ml_dataset.csv
│   │
│   └── models/
│       ├── logistic_regression.pkl
│       ├── decision_tree.pkl
│       ├── random_forest.pkl
│       ├── scaler.pkl
│       ├── feature_names.pkl
│       └── best_model.pkl
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ▶️ How to Run the Project

## Clone Repository

```bash
git clone <repository_link>
```

## Navigate to Project Folder

```bash
cd bank_marketing_project
```

## Create Virtual Environment

```bash
python -m venv .venv
```

## Activate Virtual Environment

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Launch Jupyter Notebook

```bash
jupyter notebook
```

Run the notebooks in the following order:

1. 01 Data Profiling
2. 02 Data Preprocessing
3. 03 Model Building
4. 04 Advanced Machine Learning Models
5. 05 Cross Validation + MLflow + Hyperparameter Tuning

---

# 📊 Project Outputs

The project generates:

- Data Profiling Report
- Processed Dataset
- Trained Machine Learning Models
- Feature Importance Report
- Model Comparison Report
- Hyperparameter Tuning Report
- MLflow Experiment Logs
- Best Model File

---

# 🔮 Future Improvements

The project can be further enhanced by adding:

- Stacking Ensemble Learning
- SHAP Explainability
- LIME Explainability
- Streamlit Web Application
- Docker Deployment
- FastAPI Model Serving
- CI/CD Pipeline using GitHub Actions

---

# 👨‍💻 Author

**Muhammad Minu**

Machine Learning Project

2026

---

# ⭐ Acknowledgements

Dataset provided by the **UCI Machine Learning Repository**.

This project was developed for educational purposes to demonstrate an end-to-end Machine Learning workflow following industry best practices.