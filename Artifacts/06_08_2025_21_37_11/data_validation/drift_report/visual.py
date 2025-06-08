import yaml
import matplotlib.pyplot as plt

# Step 1: Load your report.yaml
yaml_file = "report.yaml"  # Replace with your path if needed

with open(yaml_file, "r") as file:
    drift_data = yaml.safe_load(file)

# Step 2: Extract data for plotting
features = list(drift_data.keys())
p_values = [drift_data[feature]["p_value"] for feature in features]
drift_flags = [drift_data[feature]["drift_status"] for feature in features]
colors = ["red" if drift else "green" for drift in drift_flags]

# Step 3: Plot the data
plt.figure(figsize=(10, 6))
bars = plt.bar(features, p_values, color=colors)
plt.axhline(y=0.05, color="black", linestyle="--", label="Drift Threshold (p=0.05)")
plt.title("Data Drift Visualization")
plt.ylabel("p-value")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()
