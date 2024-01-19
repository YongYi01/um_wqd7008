# Step 5: Model Selection
def model_selection():
    print("Step 5: Model Selection")
    # Import the Random Forest Classifier
    from sklearn.ensemble import RandomForestClassifier
    # Initialize the Random Forest Classifier
    rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
    # Display the model parameters
    print(rf_model)
    # Import the SimpleImputer for handling missing values
    from sklearn.impute import SimpleImputer
    # Initialize the imputer
    imputer = SimpleImputer(strategy='mean')
