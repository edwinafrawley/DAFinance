# Create dict holding the data
import pandas as pd

data = {'Sym': ['APPL', 'APPL', 'APPL'],
        'Price': [105.00, 117.05, 289.80],
        'Date': ['2015/12/31', '2017/12/01', '2019/12/27']}

# Create DataFrame from the data
positions = pd.DataFrame(data=data)
print(positions)

# Make list of dictionaries
data = [{'Sym': 'APPL', 'Price': 105.00, 'Date': '2015/12/31'},
        {'Sym': 'APPL', 'Price': 117.05, 'Date': '2017/12/01'},
        {'Sym': 'APPL', 'Price': 289.80, 'Date': '2019/12/27'}]

# Create DataFrame from the list
positions = pd.DataFrame(data=data)
print(positions)

# Create a list of lists
data = [['APPL', 105.00, '2015/12/31'],
        ['APPL', 117.05, '2017/12/01'],
        ['APPL', 289.80, '2019/12/27']]

# Define the column names
columns = ['Sym', 'Price', 'Date']

# Create a DataFrame with the data and column names
df = pd.DataFrame(data=data, columns=columns)
print(df)

# Read the data
stocks = pd.read_csv('pcdg.csv')

# Look at the data
print(stocks)

# Select the Balance for October 2nd
print(ledger.loc['2020-10-02','Balance'])

# Select the Balance for October 3rd
print(ledger.loc['2020-10-03','Balance'])

# Cash and Securities for October 3rd
print(ledger.loc['2020-10-03', ['Cash', 'Securities']])

# Balance for October 1st and 3rd
print(ledger.loc[['2020-10-01', '2020-10-03'], 'Balance'])

# All columns for October 1st
print(ledger.loc['2020-10-01', :])

# Balance for all dates
print(ledger.loc[:, 'Balance'])

# Cell first row, Price column
print(positions.iloc[0, 3])

# Cell last row, Symbol column
print(positions.iloc[2, 0])

# Oldest two purchase dates
print(positions.iloc[0:2, 1])

# Newest purchase and quantity
print(positions.iloc[2, 1:3])

# Set 2020 quantity
positions.iloc[2, 2] = 15

print(positions)

# Set quantity
positions.iloc[:, 2] = 0

print(positions)

# Get the median of the opening prices
med_open = prices.loc[:, 'OPEN'].median()

# Get the median of the closing prices
med_close = prices.loc[:, 'CLOSE'].median()

if med_open < med_close:
    print("Trending down.")

# Use the list pcesv to create the column PCESV
pce['PCESV'] = pcesv

# Use the DataFrame pcnd to create the column PCND
pce['PCND'] = pcnd

# Create column for PCDG using Pandas read_csv
pce['PCDG'] = pd.read_csv('pcdg.csv', index_col='DATE')

# Create a column PCE by adding values from other columns
pce['PCE'] = pce['PCDG'] + pce['PCND'] + pce['PCESV']
pce.head()

columns_to_drop = ['PCDG', 'PCND', 'PCESV']

# Print the current columns of the DataFrame pce
print(pce.columns)

# Create new_pce by dropping columns_to_drop from pce
new_pce = pce.drop(columns=columns_to_drop)
# Print the columns of the new DataFrame
print(new_pce.columns)

# Drop the columns in_place in the original DataFrame
pce.drop(columns=columns_to_drop, inplace=True)


# Combine the source DataFrames into one
gdp = pd.concat([ge, gpdi, ne, pce], axis=1)

# Add the columns and create a new column with the result
gdp['GDP'] = gdp.apply(np.sum, axis=1)




