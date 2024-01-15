import pandas as pd

# Create a DataFrame from the given dataset
df=pd.read_csv("metadata.tsv", sep="\t")

# Split the Gene_bal column into separate columns for each gene
genes = df["Gene_bal"].str.get_dummies(sep=", ")

# Concatenate the ID column with the separated genes columns
result = pd.concat([df["ID"], genes], axis=1)

# Fill NaN values with 0 and convert all columns to integers
#result = result.fillna(0).astype(int)

# Print the resulting DataFrame
print(result)

result.to_csv("out.csv", sep=',', index=False, encoding='utf-8')

