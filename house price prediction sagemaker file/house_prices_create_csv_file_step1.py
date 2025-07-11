import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Number of samples
num_samples = 500

# Generate synthetic data with consistent lengths
data = {
    "square_feet": np.random.randint(500, 5000, size=num_samples),  # Size in square feet
    "num_bedrooms": np.random.randint(1, 6, size=num_samples),      # Number of bedrooms
    "num_bathrooms": np.random.randint(1, 4, size=num_samples),     # Number of bathrooms
    "garage": np.random.randint(0, 2, size=num_samples),            # Garage (1 = yes, 0 = no)
    "year_built": np.random.randint(1950, 2023, size=num_samples),  # Year built
    "price": np.random.randint(50000, 500000, size=num_samples)     # House price
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("house_prices.csv", index=False)
print("Synthetic house_prices.csv generated!")
