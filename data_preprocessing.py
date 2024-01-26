# Step 2: Data Preprocessing

def data_preprocessing(df):
    print("\nStep 2: Data Preprocessing")
    
    # Convert 'date' to datetime format
    df['date'] = pd.to_datetime(df['date'])
    
    # Set 'date' as the index
    df.set_index('date', inplace=True)
    
    # Check the range and frequency of the time series
    print("Time Series Range:", df.index.min(), "-", df.index.max())
    print("Time Series Frequency:", df.index.freq)
    
    # Check for missing values
    print("\nMissing Values:")
    print(df.isnull().sum())
    
    # Decide on a strategy for handling missing values
    # Since Kuala Lumpur has a relatively consistent climate, fill missing values with the mean
    df.fillna(method='ffill', inplace=True)

# Call the function with the DataFrame
data_preprocessing(df)
