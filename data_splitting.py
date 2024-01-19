# Step 4: Data Splitting
def data_splitting():
    print("Step 4: Data Splitting")
    # Import necessary libraries for data splitting
    from sklearn.model_selection import train_test_split
    # Define features and target variable
    features = df.drop('weather_code', axis=1)  # Exclude the target variable 'weather_code'
    target = df['weather_code']
    # Split the data into training and testing sets
    # Adjust the test_size and random_state as needed
    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)
    # Display the shapes of the training and testing sets
    print("Training set shape:", X_train.shape, y_train.shape)
    print("Testing set shape:", X_test.shape, y_test.shape)
