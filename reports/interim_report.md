# Interim Report — AlphaCare Insurance Risk Analytics

**Author:** funnali  
**Date:** May 2026

---

## 1. Business Understanding

AlphaCare Insurance Solutions (ACIS) needs evidence-driven strategies to optimize
marketing investments and refine pricing models in the South African auto-insurance market.
This project analyses 18 months of historical claim data (Feb 2014 – Aug 2015).

Two key metrics anchor all analysis:
- **Loss Ratio** = TotalClaims / TotalPremium
- **Margin** = TotalPremium − TotalClaims

---

## 2. Data Overview

| Property | Value |
|----------|-------|
| Total records | 1,000,098 |
| Total columns | 52 |
| Date range | Oct 2013 – Aug 2015 |

---

## 3. Data Quality Findings

| Column | Missing % | Action |
|--------|-----------|--------|
| NumberOfVehiclesInFleet | 100% | Dropped |
| CrossBorder | 99.9% | Dropped |
| CustomValueEstimate | 78% | Impute with median |
| WrittenOff / Rebuilt / Converted | 64% | Fill with Unknown |
| Gender | 0.95% | Keep, flag as Not specified |

---

## 4. Key EDA Findings

### 4.1 Claims Distribution
TotalClaims is zero-inflated and heavily right-skewed. Nearly 1 million policies
have zero claims. A small number exceed R400,000. This requires a two-stage
modeling approach: classify whether a claim occurs, then predict its amount.

### 4.2 Geographic Risk

| Province | Loss Ratio | Status |
|----------|-----------|--------|
| Gauteng | 1.22 | Unprofitable |
| KwaZulu-Natal | 1.08 | Unprofitable |
| Western Cape | 1.06 | Unprofitable |
| North West | 0.79 | Profitable |
| Northern Cape | 0.28 | Highly profitable |

**Recommendation:** Apply premium surcharges in Gauteng, KZN, and Western Cape.
Expand marketing in Northern Cape.

### 4.3 Vehicle Type Risk

| Vehicle Type | Loss Ratio |
|-------------|-----------|
| Heavy Commercial | 1.63 |
| Passenger Vehicle | 1.05 |
| Light Commercial | 0.23 |
| Bus | 0.14 |

**Recommendation:** Increase Heavy Commercial premiums urgently. Aggressively
market Light Commercial and Bus segments.

### 4.4 Gender Risk

| Gender | Loss Ratio |
|--------|-----------|
| Not specified | 1.06 |
| Male | 0.88 |
| Female | 0.82 |

**Recommendation:** Make gender a mandatory field. Apply surcharge for unspecified.

### 4.5 Vehicle Make Risk
- **Highest avg claim:** Suzuki (R~420), JMC, Hyundai
- **Lowest avg claim:** Foton, Ford, Chevrolet

### 4.6 Temporal Trends
Portfolio experienced a severe underwriting crisis peaking April 2015 (loss ratio ~1.38),
triggered by aggressive customer acquisition in late 2014 without adequate risk controls.

---

## 5. DVC Pipeline Setup

Two data versions are tracked with DVC:
1. `data/MachineLearningRating_v3.txt` — raw dataset (1,000,098 rows)
2. `data/insurance_cleaned.csv` — cleaned dataset (dropped 2 high-missing columns,
   imputed remaining, added LossRatio/Margin/HasClaim features)

To reproduce:
```bash
pip install -r requirements.txt
dvc pull
python src/data_loader.py
```

---

## 6. Next Steps
- Task 3: Statistical hypothesis testing (provinces, zip codes, gender)
- Task 4: Predictive modeling with Linear Regression, Random Forest, XGBoost