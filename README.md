# 📊 Data Cleaning & Exploratory Data Analysis (EDA) Project

##  Overview
This project was completed as part of the AnalystLab Africa Data Science Internship Program.  
It focuses on **data cleaning, exploratory data analysis (EDA), and visualization** using Python.

Two real-world datasets were analyzed:
- Titanic Dataset (Survival Analysis)
- Housing Price Dataset (Price Prediction Insights)

---

##  Objectives
- Load and inspect real-world datasets
- Handle missing values and data inconsistencies
- Perform data cleaning and preprocessing
- Conduct exploratory data analysis (EDA)
- Visualize patterns and relationships in data
- Extract meaningful insights for decision-making

---

##  Datasets Used

###  Titanic Dataset
- Passenger information from the Titanic disaster
- Goal: Identify factors influencing survival

### 🏠 Housing Dataset
- House features and prices
- Goal: Understand factors affecting property prices

---

##  Tools & Technologies
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook / VS Code

---

##  Data Cleaning Process

### Titanic Dataset:
- Filled missing `Age` values using median
- Filled missing `Embarked` values using mode
- Removed `Cabin` column due to excessive missing values

### Housing Dataset:
- Verified and corrected data types
- Ensured dataset consistency

---

##  Exploratory Data Analysis (EDA)

### Univariate Analysis:
- Age distribution
- House price distribution
- Outlier detection using boxplots

### Bivariate Analysis:
- Survival rate by gender
- Survival rate by passenger class
- Age vs survival relationship
- House price vs area relationship

### Correlation Analysis:
- Identified relationships between numerical features
- Visualized using heatmaps

---

##  Key Insights

###  Titanic Dataset:
- Females had a higher survival rate than males
- Passengers in first class had higher survival chances
- Most passengers did not survive the disaster

###  Housing Dataset:
- House price increases with area size
- Bathrooms and bedrooms positively affect price
- Features like air conditioning increase property value

---

##  Results
The analysis successfully revealed important patterns in both datasets and demonstrated how data preprocessing improves data quality for machine learning tasks.

---

##  Project Structure
project_folder/
│
├── main.py
├── Titanic-Dataset.csv
├── Housing.csv
├── cleaned_titanic.csv
├── cleaned_housing.csv
└── README.md