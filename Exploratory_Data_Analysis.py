import matplotlib.pyplot as plt
import seaborn as sns

# Distribution of churned vs retained customers
sns.countplot(x="Exited", data=data)
plt.title("Churned vs Retained Customers")
plt.show()

# Correlation heatmap to see relationships between features
plt.figure(figsize=(10, 8))
sns.heatmap(data.corr(), annot=True, cmap="coolwarm")
plt.title("Feature Correlations")
plt.show()
