# Peak at top five rows
alphabet.head(5)


# Peak at top seven rows.
alphabet.head(7)

# Peak at last row.
alphabet.tail(1)

# Get stats for all numeric columns
alphabet.describe()

# Get stats for integer columns only
alphabet.describe(include='int')

# Stats with percentiles for %30, %50, and %60
alphabet.describe(percentiles=[.3, .5, .6])

# Mask for large enough daily high
high_mask = alphabet.high > 500

# Filter using the mask
alphabet.loc[high_mask]

# Mask for specific volume
volume_mask = alphabet.volume == 1771271

# Filter using the mask
alphabet.loc[volume_mask]

# Mask rows whose volume is not 1997999
volume_mask = alphabet.volume != 1997999

# Filter using the mask
alphabet.loc[volume_mask]

# Calculate the mask for one week
mask = (alphabet['date'] >= start_date) & (alphabet['date'] <= end_date)

# Use the mask to get the data for one week
df = alphabet[mask]

# Look at result
print(df)

# Plot the daily high price
alphabet2w.plot(y = 'high')

# Plot the daily high price
alphabet2w.plot(y='high', rot=90)

# Plot the daily high price
alphabet2w.plot(y='high', rot=90, title='High Daily Prices')

# Plot daily trade volume
alphabet2w.plot(y='volume', rot=90, title='Alphabet Daily Volume')

# Plot daily trade volume
alphabet2w.plot(y='volume', kind='bar', title='Alphabet Daily Volume')

# Plot daily trade volume
alphabet2w.plot(y='volume', kind='hist', title='Alphabet Daily Volume')




