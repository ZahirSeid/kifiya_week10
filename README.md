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
