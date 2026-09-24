# 🛵 Blinkit Delivery Time Predictor

An end-to-end machine learning project for predicting quick-commerce delivery time using order, distance, preparation, traffic, weather, and courier-related features.

This project was built as a **self-learning project to understand the complete machine learning workflow** — from data preprocessing and feature engineering to model training, evaluation, explainability, and deployment.

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

Different regression approaches were explored, followed by hyperparameter tuning using `GridSearchCV`.

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

Since the original dataset represents food delivery, the project reframes the scenario as:

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
```

---

## 🧹 Data Preprocessing

The preprocessing pipeline includes:

- Handling missing values
- Median imputation for numerical features
- Mode imputation for categorical features
- Encoding categorical variables
- Preparing features for model training
- Maintaining consistent feature columns during inference

---

## ⚙️ Feature Engineering

A **Distance × Preparation Time** interaction feature was created to allow the model to capture the combined effect of:

- Delivery distance
- Order preparation time

This helps represent situations where both a longer distance and higher preparation time may contribute to increased delivery time.

---

## 🤖 Model Development

Different regression approaches were explored during development, including:

- Random Forest Regressor
- Gradient Boosting Regressor

The Random Forest model was further tuned using **GridSearchCV**.

The tuning process helped reduce the difference between training and test performance, improving the model's generalization compared with the initial model.

---

## 📈 Model Performance

The final model achieved the following evaluation results:

| Metric | Result |
|---|---:|
| **MAE** | ~7.43 minutes |
| **RMSE** | ~10.67 minutes |
| **R² Score** | ~0.77 |

### What these metrics mean

- **MAE (~7.43 min):** On average, the prediction differs from the actual delivery time by about 7.43 minutes.
- **RMSE (~10.67 min):** Gives more weight to larger prediction errors.
- **R² (~0.77):** The model explains approximately 77% of the variation in delivery time on the evaluation data.

> These results are based on this specific dataset and evaluation setup and should not be interpreted as production-level performance.

---

## 🔍 Explainability

Model explainability was added using **SHAP (SHapley Additive exPlanations)**.

SHAP helps answer questions such as:

- Which features influenced a prediction?
- Did a particular feature increase or decrease the predicted delivery time?
- Which features are generally most influential across the dataset?

This makes the model easier to interpret instead of treating it as a complete black box.

---

## 📊 Key Model Insight

In this dataset, **distance was one of the strongest predictors of delivery time**, followed by the interaction between distance and preparation time.

Other variables such as weather, traffic level, and vehicle type showed comparatively lower importance in the trained model.

However, these findings are **specific to the available dataset**. Since the project uses a food-delivery dataset adapted to a quick-commerce scenario, they should not be interpreted as conclusions about actual Blinkit operations.

---

## 🖥️ Application

The Streamlit application allows users to enter:

- Dark store → customer distance
- Picking / packing time
- Delivery partner experience
- Weather
- Traffic level
- Time of day
- Vehicle type

The application then displays:

- Predicted delivery time
- SLA status
- Feature importance
- Model insights

---

## 📸 Application Screenshots

Add your application screenshots here if they are uploaded to the repository.

Example:

```text
screenshots/
├── prediction-dashboard.png
├── feature-importance.png
└── shap-explanation.png
```
---

## 🚀 Try It Live

🌐 **Live Streamlit App:**

[Open Blinkit Delivery Time Predictor](https://blinkit-delivery-time-predictor-g2kbydywuxl7puxkhzrmt4.streamlit.app/)

💻 **GitHub Repository:**

[View the source code](https://github.com/radhikamahajan705-afk/blinkit-delivery-time-predictor)

---

## 💻 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/radhikamahajan705-afk/blinkit-delivery-time-predictor.git
```

### 2. Move into the project directory

```bash
cd blinkit-delivery-time-predictor
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 📁 Repository Structure

```text
blinkit-delivery-time-predictor/
│
├── app.py
├── requirements.txt
├── delivery_model.pkl
├── model_columns.pkl
├── README.md
│
└── screenshots/
    ├── prediction-dashboard.png
    ├── feature-importance.png
    └── shap-explanation.png
```

> Update the model filenames and folder structure above if your actual repository uses different filenames.

---

## 🔮 Future Improvements

The current project can be extended with:

- 🌦️ Real-time weather API integration
- 🚦 Real-time traffic data integration
- 📍 Real dark-store and customer geolocation data
- 📊 A larger and more representative dataset
- 🔄 Model monitoring and data-drift detection
- ⚡ FastAPI-based model serving
- 🐳 Docker containerization
- 📈 More detailed error analysis by distance, traffic, weather, and time of day
- 🧪 Cross-validation and additional model experiments
- 🎛️ What-if simulation for testing different delivery conditions

---

## 🎓 Learning Outcomes

This project helped me understand the practical machine learning workflow beyond simply training a model.

Through this project, I worked with:

- Data preprocessing
- Missing-value handling
- Feature engineering
- Categorical encoding
- Regression modeling
- Model comparison
- Hyperparameter tuning
- Model evaluation
- Feature importance
- SHAP explainability
- Model deployment
- Streamlit application development
- Git and GitHub

The main goal was to understand **how an ML model moves from raw data to a usable application**.

---

## 👩‍💻 Author

**Radhika Mahajan**

Engineering Student | Electronics & Telecommunication

Built as a **self-learning machine learning project** to explore an end-to-end ML workflow from data preprocessing to deployment.

---

## ⭐ Acknowledgement

This project was created for educational and portfolio purposes to understand machine learning concepts through a practical delivery-time prediction use case.
