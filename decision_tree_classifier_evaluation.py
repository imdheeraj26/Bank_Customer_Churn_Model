y_pred_tree_clf = tree_clf.predict(X_test)
print("Decision Tree Accuracy:", accuracy_score(y_test, y_pred_tree_clf))
print(confusion_matrix(y_test, y_pred_tree_clf))
print(classification_report(y_test, y_pred_tree_clf))
