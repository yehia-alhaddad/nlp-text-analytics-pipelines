import pandas as pd

# ---- LOAD DATASET WITH CORRECT ENCODING ----
df = pd.read_csv("IMDB Dataset.csv", encoding="ISO-8859-1")

# ---- KEEP ONLY USEFUL COLUMNS ----
df = df[['review', 'sentiment']]   # keep only review + sentiment
df.columns = ['message', 'label']  # rename for clarity

# ---- BASIC DATA CHECKS ----
print("✅ Dataset Loaded Successfully")
print("Shape (rows, cols):", df.shape)
print("\nFirst 5 rows:")
print(df.head())

# ---- CHECK FOR MISSING VALUES ----
print("\nMissing values per column:")
print(df.isnull().sum())

# ---- CHECK FOR DUPLICATES ----
duplicates = df.duplicated().sum()
print("\nNumber of duplicate rows:", duplicates)

# ---- CLASS BALANCE ----
print("\nClass distribution:")
print(df['label'].value_counts())

# ---- OPTIONAL: REMOVE DUPLICATES ----
if duplicates > 0:
    df = df.drop_duplicates()
    print("\nDuplicates removed. New shape:", df.shape)

# ---- SAVE CLEAN DATASET ----
df.to_csv("imdb_clean.csv", index=False, encoding="utf-8")
print("\nClean dataset saved as imdb_clean.csv")
