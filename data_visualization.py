# Plot the distribution of the target variable
sns.countplot(x='Exited', data=data)
plt.title('Distribution of Churn')
plt.show()

# Correlation heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(data.corr(), annot=True, fmt='.2f', cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()
