# Step 7: Evaluate Model on Imputed Data
def evaluate_model_imputed(y_test, y_pred_imputed):
    print("\nStep 7: Evaluate Model on Imputed Data")
    from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
    accuracy_imputed = accuracy_score(y_test, y_pred_imputed)
    classification_report_result_imputed = classification_report(y_test, y_pred_imputed)
    conf_matrix_imputed = confusion_matrix(y_test, y_pred_imputed)
    # Display evaluation metrics for the imputed data
    print("Accuracy on Imputed Data:", accuracy_imputed)
    print("\nClassification Report on Imputed Data:\n", classification_report_result_imputed)
    print("\nConfusion Matrix on Imputed Data:\n", conf_matrix_imputed)

# Call the function with the relevant parameters
evaluate_model_imputed(y_test, y_pred_imputed)
