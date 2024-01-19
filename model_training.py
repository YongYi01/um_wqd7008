# Step 6: Model Training
def model_training():
    print("Step 6: Model Training")
    # Fit and transform the imputer on the training data
    X_train_imputed = imputer.fit_transform(X_train)
    # Transform the test data using the trained imputer
    X_test_imputed = imputer.transform(X_test)
    # Train the Random Forest Classifier on the imputed training data
    rf_model.fit(X_train_imputed, y_train)
    # Predict on the imputed test data
    y_pred_imputed = rf_model.predict(X_test_imputed)

model_training(X_train, y_train, X_test, y_test, rf_model, imputer)
