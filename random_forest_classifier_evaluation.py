y_pred_rf_clf = rf_clf.predict(X_test)
print("Random Forest Accuracy:", accuracy_score(y_test, y_pred_rf_clf))
print(confusion_matrix(y_test, y_pred_rf_clf))
print(classification_report(y_test, y_pred_rf_clf))
