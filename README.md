# Medical Insurance Cost Prediction

## Overview
This project aims to predict medical insurance costs based on demographic and lifestyle factors using supervised machine learning models. The focus is on building an interpretable and deployable prediction system with a Streamlit dashboard.

---

## 1. Objective & Research Questions
**Objective:**  
Develop a predictive model to estimate individual medical insurance costs and identify key drivers.

**Research Questions:**
- What demographic and lifestyle factors most influence insurance costs?
- How accurately can machine learning models predict insurance charges?
- How can model interpretability (SHAP) help explain predictions to stakeholders?

---

## 2. Data Description
**Data Source:**  
- Dataset: Medical Insurance Dataset (commonly used in ML tutorials)  
- Records: ~1,300 individuals  
- Features: Age, Sex, BMI, Children, Smoker, Region, Charges  

**Data Quality:**  
- No major missing values  
- Mix of categorical and numerical features  
- Target variable: `charges` (continuous)

---

## 3. Key Steps
- **Data Cleaning:** Handle categorical encoding (sex, smoker, region).  
- **Feature Engineering:** Scale numerical features (BMI, age).  
- **EDA:** Visualize correlations between BMI, smoking status, and charges.  
- **Model Building:** Train multiple models (Logistic Regression, Random Forest, XGBoost).  
- **Interpretability:** Use SHAP to explain feature contributions.  

---

## 4. Methodology & Algorithms
- **Algorithms:** Logistic Regression, Random Forest, XGBoost  
- **Reasoning:**  
  - Logistic Regression → baseline linear model  
  - Random Forest → ensemble with interpretability  
  - XGBoost → high‑performance gradient boosting  
- **Interpretability:** SHAP values to visualize feature importance  

---

## 5. Evaluation Metrics
- Accuracy, Precision, Recall, F1‑score (for classification tasks)  
- RMSE, MAE, R² (for regression tasks)  
- SHAP plots for interpretability  

---

## 6. Visualization & Dashboard
- **Streamlit Dashboard:** Interactive input form + prediction output  
- **SHAP Summary Plot:** Shows contribution of features (e.g., smoker, BMI, age)  
- **Boxplots & Scatterplots:** Explore relationships between features and charges  

---

## 7. Limitations & Challenges
- Small dataset size (~1,300 records) may limit generalization.  
- Regional bias (only 4 regions in dataset).  
- BMI and smoking status dominate predictions → risk of overfitting.  

---

## 8. Future Work / Recommendations
- Collect larger, more diverse datasets.  
- Add additional health indicators (exercise, diet, medical history).  
- Deploy model via API for integration with insurance systems.  

---

## 9. Business Impact
- **Healthcare Providers:** Identify high‑risk individuals for preventive programs.  
- **Insurance Companies:** Price policies more accurately and fairly.  
- **Customers:** Understand lifestyle factors influencing insurance costs.  

---

## 10. Tools & Environment
**Python Libraries (berurutan sesuai proses):**

1. ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white) 
   → **Data preprocessing & manipulasi** (load dataset, cleaning, transformasi numerik & kategorikal)

2. ![YData Profiling](https://img.shields.io/badge/YData%20Profiling-%23FF6F61.svg?style=for-the-badge&logo=pandas&logoColor=white)  
   → **Exploratory Data Analysis (EDA)** otomatis (profiling dataset, deteksi outlier, distribusi fitur)

3. ![PyCaret](https://img.shields.io/badge/PyCaret-%230080FF.svg?style=for-the-badge&logo=pycaret&logoColor=white)  
   → **Benchmarking awal** (eksplorasi model otomatis, perbandingan baseline)

4. ![Scikit-Learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)  
   → **Model training & evaluasi** (GradientBoostingRegressor, RandomForest, KNN, pipeline, evaluasi R², RMSE, CV)

5. `https://img.shields.io/badge/Optuna-%2366CCFF.svg?style=for-the-badge&logo=optuna&logoColor=white`  
   `https://img.shields.io/badge/GridSearchCV-%23FFD700.svg?style=for-the-badge&logo=scikit-learn&logoColor=black`  
   → **Hyperparameter tuning** (Optuna untuk optimasi canggih, GridSearchCV untuk baseline)

6. `https://img.shields.io/badge/SHAP-%23FF7043.svg?style=for-the-badge&logo=shap&logoColor=white`  
   → **Model interpretability** (summary plot, bar chart, force plot, dependence plot)

7. `https://img.shields.io/badge/matplotlib-%230076A8.svg?style=for-the-badge&logo=plotly&logoColor=white`  
   `https://img.shields.io/badge/seaborn-%2300B4D8.svg?style=for-the-badge&logo=plotly&logoColor=white`  
   → **Visualisasi hasil evaluasi & interpretasi**

8. `https://img.shields.io/badge/joblib-%2300A86B.svg?style=for-the-badge&logo=python&logoColor=white`  
   → **Model packaging & deployment** (save & load pipeline GBR Optuna)

---

**Environment:**  
- Jupyter Notebook for experimentation   
- GitHub for version control  

---
