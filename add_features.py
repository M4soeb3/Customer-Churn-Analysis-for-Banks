# Feature Engineering Examples

# Calculate the account balance-to-salary ratio
data["BalanceSalaryRatio"] = data["AccountBalance"] / data["EstimatedSalary"]

# Binarize age to identify younger vs older customer segments
data["IsYoung"] = (data["Age"] < 30).astype(int)

# Drop unnecessary columns (e.g., CustomerID)
data = data.drop(columns=["CustomerID"])
