import pandas as pd

# Load the CSV file
file_path = '~/csv-files/test.csv'
df = pd.read_csv(file_path)

# Replace NaN values with 0 and remove non-numeric characters (excluding commas)
df_cleaned = df.copy()
df_cleaned['followers'] = df_cleaned['followers'].fillna('0')  # Replace NaN with '0'
df_cleaned['followers'] = df_cleaned['followers'].str.replace('[^0-9]', '', regex=True)

# Convert the 'followers' column to numeric
df_cleaned['followers'] = pd.to_numeric(df_cleaned['followers'], errors='coerce')

# Save the cleaned dataframe to a new CSV file
cleaned_file_path = '~/csv-out/test.csv'
df_cleaned.to_csv(cleaned_file_path, index=False)

print(f"Cleaned data saved to {cleaned_file_path}")

