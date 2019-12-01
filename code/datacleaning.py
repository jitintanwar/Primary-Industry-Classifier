import pandas as pd

df = pd.read_excel('../data/bd_ic_new.xlsx')
# [48601 rows x 3 columns]>

# Ignore the rows having company type as acquired
df = df[df['CompanyType'] != 'Acquired']

# Ignore the rows having company type as acquired
df = df[df['BusinessDescription'] != '-']

# Ignore the rows having company type as acquired
df = df[df['PrimaryIndustry'] != 0]

# Note: Only 36840/48601 rows left after applying above filetration/data cleaning.

# convert IC dtype to category
df['PrimaryIndustry'] = df['PrimaryIndustry'].astype('category')

# create a new column with category codes
df['Category'] = df.PrimaryIndustry.cat.codes

# uncomment the below line to see mappings of IC
cat_mapping = dict(enumerate(df.PrimaryIndustry.cat.categories))
# for key in cat_mapping:
# 	print key, cat_mapping[key]

# Write clean data into a file
writer = pd.ExcelWriter('../data/clean_data.xlsx', engine='xlsxwriter')
df.to_excel(writer,'Sheet1')
writer.save()
