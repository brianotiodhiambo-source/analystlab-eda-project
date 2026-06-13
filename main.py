import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

# =============================
# 1. SETUP + FILE CHECK
# =============================
print("CURRENT FOLDER:")
print(os.getcwd())

print("\nFILES:")
print(os.listdir())

# =============================
# 2. LOAD DATASETS
# =============================
titanic = pd.read_csv("Titanic-Dataset.csv")
house = pd.read_csv("Housing.csv")

# =============================
# 3. QUICK PREVIEW
# =============================
print("\nTITANIC PREVIEW")
print(titanic.head())

print("\nHOUSING PREVIEW")
print(house.head())

# =============================
# 4. MISSING VALUES CHECK (BEFORE)
# =============================
print("\nMISSING VALUES (TITANIC BEFORE)")
print(titanic.isnull().sum())

print("\nMISSING VALUES (HOUSING BEFORE)")
print(house.isnull().sum())

# =============================
# 5. DATA INFO
# =============================
print("\nTITANIC INFO")
print(titanic.info())

print("\nHOUSING INFO")
print(house.info())

# =============================
# 6. DUPLICATES CHECK
# =============================
print("\nDUPLICATES TITANIC:", titanic.duplicated().sum())
print("DUPLICATES HOUSING:", house.duplicated().sum())

# =============================
# 7. DATA CLEANING
# =============================

# Titanic cleaning
titanic["Age"] = titanic["Age"].fillna(titanic["Age"].median())
titanic["Embarked"] = titanic["Embarked"].fillna(titanic["Embarked"].mode()[0])
titanic.drop(columns=["Cabin"], inplace=True)

# Housing cleaning (ensure numeric types)
house["price"] = house["price"].astype(float)
house["area"] = house["area"].astype(float)

# =============================
# 8. AFTER CLEANING CHECK
# =============================
print("\nMISSING VALUES (TITANIC AFTER)")
print(titanic.isnull().sum())

print("\nMISSING VALUES (HOUSING AFTER)")
print(house.isnull().sum())

print("\nCLEANING COMPLETE ✔")

# =============================
# 9. SUMMARY STATISTICS
# =============================
print("\nTITANIC STATISTICS")
print(titanic.describe())

print("\nHOUSING STATISTICS")
print(house.describe())

# =============================
# 10. UNIVARIATE VISUALS
# =============================

# Age distribution
plt.figure()
plt.hist(titanic["Age"], bins=20)
plt.title("Age Distribution (Titanic)")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()

# Price distribution
plt.figure()
plt.hist(house["price"], bins=20)
plt.title("House Price Distribution")
plt.xlabel("Price")
plt.ylabel("Count")
plt.show()

# Boxplot (outliers)
plt.figure()
plt.boxplot(house["price"])
plt.title("House Price Outliers")
plt.show()

# =============================
# 11. BIVARIATE ANALYSIS
# =============================

# Survival vs Gender
plt.figure()
sns.barplot(x="Sex", y="Survived", data=titanic)
plt.title("Survival Rate by Gender")
plt.show()

# Survival vs Class
plt.figure()
sns.barplot(x="Pclass", y="Survived", data=titanic)
plt.title("Survival Rate by Class")
plt.show()

# Age vs Survival
plt.figure()
sns.boxplot(x="Survived", y="Age", data=titanic)
plt.title("Age vs Survival")
plt.show()

# Price vs Area
plt.figure()
plt.scatter(house["area"], house["price"])
plt.title("Price vs Area")
plt.xlabel("Area")
plt.ylabel("Price")
plt.show()

# =============================
# 12. CORRELATION HEATMAP
# =============================
plt.figure(figsize=(8,6))
sns.heatmap(house.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Housing Correlation Heatmap")
plt.show()