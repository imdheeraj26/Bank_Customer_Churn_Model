# Example prediction
sample_data = X_test.iloc[0].values.reshape(1, -1)
predicted_churn = rf_clf.predict(sample_data)
print("Predicted Churn:", predicted_churn)
