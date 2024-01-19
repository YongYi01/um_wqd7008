# Step 3: Feature Engineering
def feature_engineering():
    print("Step 3: Feature Engineering")
    # Extract temporal features
    df['hour'] = df.index.hour
    df['day'] = df.index.day
    df['month'] = df.index.month
    df['year'] = df.index.year
    # Display the updated dataset
    print(df.head())
    # Create lag features for relevant variables
    lag_variables = ['temperature_2m', 'wind_speed_10m', 'precipitation', 'pressure_msl']
    for var in lag_variables:
        for i in range(1, 6):  # Create lags up to 5 hours
            df[f'{var}_lag{i}'] = df[var].shift(i)
    # Display the updated dataset with lag features
    print(df.head())
