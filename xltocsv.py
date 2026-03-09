import pandas as pd

# Load Excel file
df = pd.read_excel("SELENITE RAPID FIRE QUIZ 2026: (Responses)")

# Select required columns
df = df[['Timestamp', 'Enter your name:', 'Score']]

# Rename columns
df.columns = ['timestamp', 'name', 'score']

# Convert score from "8/10" → 8
df['score'] = df['score'].astype(str).str.split('/').str[0].astype(int)

# Convert timestamp to datetime
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Sort by score (DESC) and timestamp (ASC) for tie-breaking
df = df.sort_values(by=['score', 'timestamp'], ascending=[False, True]).reset_index(drop=True)

# Assign rank
df['rank'] = df.index + 1

# Assign qualification status
df['status'] = df['rank'].apply(lambda x: "Qualified" if x <= 20 else "Not Qualified")

# Reorder columns for final output
result = df[['rank', 'name', 'score', 'timestamp', 'status']]

# Save to CSV
result.to_csv("results.csv", index=False)

print("CSV generated successfully: results.csv")