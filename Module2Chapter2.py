# Assign a value to cash.
cash = 19.11

# Check if cash is equal to securities
print(cash == non_cash)

# Assign the value of securities to cash
cash = non_cash

# Check if cash is equal to securities
print(cash == non_cash)

# Check dividend is greater than zero
print(d2 > 0)

# Is dividend 1 is greater than dividend 2?
print(d1 > d2)

# Check dividend 1 is at least 100
print(d1 >= 100)

# Check dividend 2 is at least as much dividend 1
print(d1 <= d2)

# Print the given variables
print(is_investment_account)
print(balance_positive)

# Decide if this account is cantidate for trading advice
potential_trade = is_investment_account and balance_positive

# Print if this represents a potential trade
print(potential_trade)

# Assign a default action if no input
action = input_action or "Hold"

# Print the action
print(action)

# Assign action only if trades can be made
do_action = is_trading_day and action

# Print the action to do
print(do_action)

print(closing_prices)

# Assigning True if we need to get the prices
not_prices = not closing_prices

print(not_prices)

# Get prices if market is closed and we don't have prices
get_prices = not (market_closed and not_prices)

print(get_prices)

# Get number of purchases
num_purchases = len(purchases)
# Get number of sales
num_sales = len(sales)

# Check if more sales than purchases
if num_purchases < num_sales:
    print('buy more')

    # Get number of purchases
    num_purchases = len(purchases)
    # Get number of sales
    num_sales = len(sales)

    # Check if fewer sales than purchases
    if num_sales < num_purchases:
        print('sell more')

# Get number of purchases
num_purchases = len(purchases)
# Get number of sales
num_sales = len(sales)

# Check if both lists are empty
if not (purchases or sales):
    print('No sales or purchases')

    # Get the symbol value
    symbol = trn['symbol']

    # Check if Apple stock
    if symbol == 'APPL':
        appl.append(trn)

    # Get the symbol value
symbol = trn['symbol']

# Get the symbol value
symbol = trn['symbol']

# Check if Apple stock
if symbol == 'APPL':
    appl.append(trn)
# Check if Tesla stock
elif symbol == 'TSLA':
    tsla.append(trn)
# Check if Amazon stock
elif symbol == 'AMZN':
    amzn.append(trn)

# Get the symbol value
symbol = trn['symbol']

# Check if Apple stock
if symbol == 'APPL':
    appl.append(trn)
# Check if Tesla stock
elif symbol == 'TSLA':
    tsla.append(trn)
# Check if Amazon stock
elif symbol == 'AMZN':
    amzn.append(trn)
# Handle other companies
else:
    print(symbol)

    # Loop through buys
for buy in buys:
    print('Buying ' + buy['symbol'])
    new_balance = balance - buy['total_cost']
    balance = new_balance

print(balance)

for buy in buys:
    print('Buying ' + buy['symbol'])
    new_balance = balance - buy['total_cost']
    if new_balance < 0:
        print('Unable to finish buys')
        break
    balance = new_balance

print(balance)

# Loop while true
while True:
    net_exports = nea.get(query_date, -1)
    query_date = datetime(query_date.year - 1, 1, 1)
    # Skip if net exports are not positive
    if net_exports < 0:
        continue
    surplus_years.append(query_date)
    # Check if 5 years have been collected
    if len(surplus_years) == 5:
        # Stop the loop
        break
print(surplus_years)










