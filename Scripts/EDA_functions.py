
import pandas as pd
def validate_data_quality(df):
   
    missing_values = df.isnull().sum().sum()

    # Check for duplicate entries
    duplicates = df.duplicated().sum()

    return {
        'missing_values': missing_values,
        'duplicates': duplicates
    }