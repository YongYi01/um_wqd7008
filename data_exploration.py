# Step 1: Data Exploration
def data_exploration():
    print("Step 1: Data Exploration")
    #Target variable: weather_code (since it indicates different weather condition
    data = '/home/ubuntu/project/um_wqd7008/hourly_weather.csv'
    df = pd.read_csv(data)
    # Display basic information about the dataset
    print(df.info())
    # Display the first few rows of the dataset
    print(df.head())

data_exploration()
