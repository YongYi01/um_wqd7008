# Step 2: Data Preprocessing
def data_preprocessing():
    data = '/home/ubuntu/project/um_wqd7008/hourly_weather.csv'
    df = pd.read_csv(data)
    print("Step 2: Data Preprocessing")
    # Convert 'date' to datetime format
    df['date'] = pd.to_datetime(df['date'])
    # Set 'date' as the index
    df.set_index('date', inplace=True)
    # Check the range and frequency of the time series
    print(df.index.min(), df.index.max())
    print(df.index.freq)
    # Check for missing values
    print(df.isnull().sum())
    # Decide on a strategy for handling missing values
    # Since Kuala Lumpur has a relatively consistent climate, fill missing values with the mean
    df.fillna(method='ffill', inplace=True)
