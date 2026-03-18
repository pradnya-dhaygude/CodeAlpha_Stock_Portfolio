# Stock Portfolio Tracker

# Step 1: Dictionary with stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "AMZN": 130
}

total_value = 0

print("Stock Portfolio Tracker")

# Step 2: Ask number of stocks
n = int(input("How many stocks do you want to enter? "))

# Step 3: Loop for user input
for i in range(n):

    stock_name = input("Enter stock name: ").upper()
    quantity = int(input("Enter quantity: "))

    # Check if stock exists
    if stock_name in stock_prices:

        price = stock_prices[stock_name]
        value = price * quantity
        total_value += value

        print("Value of", stock_name, "=", value)

    else:
        print("Stock not found!")

# Step 4: Display total investment
print("\nTotal Investment Value =", total_value)

# Step 5: Save result to file
save = input("Do you want to save result to file? (yes/no): ")

if save == "yes":

    file = open("portfolio_result.txt", "w")
    file.write("Total Investment Value: " + str(total_value))
    file.close()

    print("Result saved in portfolio_result.txt")