# 🛵 Blinkit Delivery Time Predictor

An end-to-end machine learning project for predicting quick-commerce delivery time using order, distance, preparation, traffic, weather, and courier-related features.

The project was built as a **self-learning project to understand the complete machine learning workflow** — from data preprocessing and feature engineering to model training, evaluation, explainability, and deployment.

---

## 📌 Overview

Quick-commerce platforms depend on accurate delivery-time estimates to provide customers with realistic delivery expectations.

This project explores how machine learning can be used to predict delivery time based on order-level conditions such as:

- 📍 Distance between dark store and customer
- ⏱️ Preparation / picking-packing time
- 🛵 Delivery partner experience
- 🌦️ Weather conditions
- 🚦 Traffic level
- 🕐 Time of day
- 🚲 Vehicle type

The trained regression model is integrated into an interactive **Streamlit web application**, where users can enter order conditions and receive an estimated delivery time.

The application also provides model insights through feature importance and SHAP-based explainability.

> **Note:** This is an educational project inspired by a Blinkit-style quick-commerce scenario. The model is **not an official Blinkit model** and does not use Blinkit's internal operational data.

---

## ✨ Features

### 🎯 Delivery Time Prediction
Predicts estimated delivery time in minutes based on the provided order conditions.

### ⚠️ SLA Status
Compares the predicted delivery time with a 30-minute delivery promise and indicates whether a delay may be expected.

### 🔍 SHAP Explainability
Uses SHAP to understand how individual features influence model predictions.

### 📊 Feature Importance Analysis
Shows which input features have the greatest influence on the trained model.

### 🌐 Interactive Streamlit Application
Provides a simple interface where users can enter order details and instantly receive a prediction.

### 🧩 Feature Engineering
Includes a **Distance × Preparation Time** interaction feature to capture the combined effect of delivery distance and preparation time.

### 🤖 Model Comparison & Tuning
Multiple regression approaches were explored, followed by hyperparameter tuning using `GridSearchCV`.

---

## 🗂️ Dataset

The model was trained using a **food-delivery dataset containing 1,000 orders**.

The dataset includes:

| Feature | Description |
|---|---|
| `Distance_km` | Distance between the delivery location and source |
| `Weather` | Weather condition |
| `Traffic_Level` | Traffic condition |
| `Time_of_Day` | Time period of the order |
| `Vehicle_Type` | Delivery vehicle |
| `Preparation_Time_min` | Time required to prepare the order |
| `Courier_Experience_yrs` | Delivery partner experience |
| `Delivery_Time_min` | Target variable — actual delivery time |

### Quick-Commerce Adaptation

Since the original dataset represents food delivery, the project reframes the delivery scenario as:

**Restaurant → Dark Store**  
**Customer delivery distance → Dark Store-to-customer distance**

This allows the dataset to be used for learning and demonstrating a quick-commerce delivery prediction workflow.

> The results should therefore be interpreted as **dataset-specific machine learning findings**, not as actual operational insights about Blinkit.

---

## 🛠️ Tech Stack

| Category | Technologies |
|---|---|
| Programming | Python |
| Data Processing | Pandas, NumPy |
| Machine Learning | Scikit-learn |
| Models | Random Forest, Gradient Boosting |
| Hyperparameter Tuning | GridSearchCV |
| Explainability | SHAP |
| Web Application | Streamlit |
| Development | Google Colab |
| Deployment | Streamlit Cloud |
| Version Control | Git, GitHub |

---

## 🔄 Machine Learning Workflow

```text
Raw Dataset
     ↓
Data Cleaning
     ↓
Missing Value Handling
     ↓
Feature Encoding
     ↓
Feature Engineering
     ↓
Train / Test Split
     ↓
Model Comparison
     ↓
Hyperparameter Tuning
     ↓
Model Evaluation
     ↓
SHAP Explainability
     ↓
Streamlit Deployment

## 🚀 Try It Live

🌐 **Live Streamlit App:**

https://blinkit-delivery-time-predictor-g2kbydywuxl7puxkhzrmt4.streamlit.app/


