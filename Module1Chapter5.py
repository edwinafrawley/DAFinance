# First four items of names
print(names[0:4])

# Print information on last company
print(names[-1])
print(prices[-1])
print(earnings[-1])
print(sectors[-1])

# Import numpy as np
import numpy as np

# Convert lists to arrays
prices_array = np.array(prices)
earnings_array = np.array(earnings)

# Calculate P/E ratio
pe = prices_array/earnings_array
print(pe)

# Create boolean array
boolean_array = (sectors == 'Information Technology')

# Subset sector-specific data
it_names = names[boolean_array]
it_pe = pe[boolean_array]

# Display sector names
print(it_names)
print(it_pe)

# Create boolean array
boolean_array = (sectors == 'Consumer Staples')

# Subset sector-specific data
cs_names = names[boolean_array]
cs_pe = pe[boolean_array]

# Display sector names
print(cs_names)
print(cs_pe)

# Calculate mean and standard deviation
it_pe_mean = np.mean(it_pe)
it_pe_std = np.std(it_pe)

print(it_pe_mean)
print(it_pe_std)

# Calculate mean and standard deviation
cs_pe_mean = np.mean(cs_pe)
cs_pe_std = np.std(cs_pe)

print(cs_pe_mean)
print(cs_pe_std)

import matplotlib.pyplot as plt

# Make a scatterplot
plt.scatter(it_id, it_pe, color='red', label='IT')
plt.scatter(cs_id, cs_pe, color='green', label='CS')

# Add legend
plt.legend()

# Add labels
plt.xlabel('Company ID')
plt.ylabel('P/E Ratio')
plt.show()

# Import matplotlib.pyplot with the alias plt
import matplotlib.pyplot as plt

# Plot histogram
plt.hist(it_pe, bins = 8)

# Add x-label
plt.xlabel('P/E ratio')

# Add y-label
plt.ylabel('Frequency')

# Show plot
plt.show()

# Identify P/E ratio within it_pe that is > 50
outlier_price = it_pe[it_pe > 50]

# Identify the company with PE ratio > 50
outlier_name = it_names[it_pe > 50]

# Display results
print("In 2017, " + str(outlier_name[0]) + " had an abnormally high P/E ratio of " + str(round(outlier_price[0], 2)) + ".")

