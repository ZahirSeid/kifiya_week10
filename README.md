# kifiya_week10

# Task 1: Change Point Analysis on Brent Oil Prices

## Overview

This task focuses on detecting change points in Brent oil prices using statistical modeling. The dataset contains daily oil prices, along with derived features such as returns, log returns, volatility, and momentum.

### Data Summary

### The preprocessed dataset (preprocessed_data.csv) consists of 8,990 entries with the following columns:

    Date: Timestamp of the record.
    Price: Daily Brent oil price.
    Returns: Daily percentage change in price.
    Log_Returns: Logarithmic transformation of returns.
    Volatility: Rolling standard deviation of log returns, measuring market fluctuations.
    Momentum: Price movement trend over a given period.

### Statistical Insights

    Average oil price: $48.49 (min: $9.10, max: $143.95)
    Volatility range: 0.0035 to 0.2064, mean: 0.0213
    Momentum variation: From -28.04 to 25.94, indicating significant price shifts.
    Maximum daily return: +50.98%, while the largest drop was -47.46%

### Methodology

    Data Preprocessing:
        Converted raw price data into log returns and computed rolling volatility.
        Standardized momentum indicators to assess price trends.

    Change Point Detection:
        Used statistical methods to identify structural changes in price trends.
        Evaluated shifts in mean and variance of returns.

    Visualization & Interpretation:
        Graphs were generated to visualize detected change points.
        Key events and anomalies were analyzed based on price movements. 

# Tasks 2 & 3 – Advanced Modeling and Interactive Dashboard

## Task 2: Advanced Analysis & Integration of Economic Indicators

### Objective:
Enhance the baseline oil price analysis by incorporating key macroeconomic indicators to improve understanding and forecasting of Brent oil prices.

### What We Did:

- **Data Integration:**
    - Converted wide-format GDP growth and inflation datasets (1980–2024) into long format.
    - Merged these economic indicators with the Brent oil price data on a common year field.

- **Advanced Modeling:**
    - Developed multivariate models (e.g., VAR, regime-switching models) to capture relationships between oil prices and macroeconomic trends.
    - Explored machine learning techniques (e.g., LSTM networks) to model complex non-linear dynamics.

- **Model Evaluation:**
    - Evaluated model performance using extended metrics: **RMSE**, **MAE**, **MAPE**, and **Recency RMSE**.
    - Final evaluation metrics (for **Price**, **Returns**, **Log_Returns**, **Volatility**, and **Momentum**) guided improvements in feature engineering and parameter tuning.


## Task 3: Interactive Dashboard Development

### Objective:
Create an intuitive and responsive dashboard that allows stakeholders to explore the analysis and model results interactively.

### What We Did:

- **Backend (Flask):**
    - Developed APIs to serve preprocessed data, model forecasts, and evaluation metrics.
    - Enabled integration of real-time or updated data sources.

- **Frontend (React):**
    - Built interactive visualizations (time series, event overlays, filterable date ranges) for oil prices and economic indicators.
    - Implemented features to allow users to compare model forecasts and review key performance metrics.

- **User Experience:**
    - Ensured the dashboard is responsive across devices and provides clear, actionable insights.
    - The dashboard empowers users to drill down into specific events or trends affecting Brent oil prices.

