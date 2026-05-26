# Insurance Risk Analytics

End-to-end insurance risk analytics and predictive modeling project for AlphaCare Insurance Solutions (ACIS).

## Project Objectives

- Exploratory Data Analysis (EDA)
- Statistical Hypothesis Testing
- Risk Modeling
- Premium Optimization
- Model Explainability using SHAP
- Data Version Control (DVC)

## Project Structure

## Data Pipeline (DVC)

Data files are tracked with DVC and NOT stored in Git.

### Reproduce the pipeline
1. pip install -r requirements.txt
2. dvc pull
3. python src/data_loader.py

### Data versions
- data/MachineLearningRating_v3.txt - raw dataset
- data/insurance_cleaned.csv - cleaned dataset
