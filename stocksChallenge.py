stockDict = {
    "GM": "General Motors",
    "CAT":"Caterpillar",
    "EK":"Eastman Kodak"
}

purchases = [
    ( 'GE', 100, '10-sep-2001', 48 ),
    ( 'CAT', 100, '1-apr-1999', 24 ),
    ( 'GE', 200, '1-jul-1998', 56 )
]

# Create a purchase history report that computes the full purchase price 
# (shares times dollars) for each block of stock and uses the stockDict to 
# look up the full company name. This is the basic relational database join 
# algorithm between two tables.

# for purchase in purchases:
    # print(f"I purchased {stockDict[purchase[0]]} stock for ${purchase[1] * purchase[3]}")

# Example output for one block: I purchased General Electric stock for $4800

# Create a second purchase summary that which accumulates total investment by 
# ticker symbol. In the above sample data, there are two blocks of GE. These 
# can easily be combined by creating a dict where the key is the ticker and 
# the value is the list of blocks purchased. The program makes one pass through 
# the data to create the dict. A pass through the dict can then create a report 
# showing each ticker symbol and all blocks of stock.

portfolio = {}

for purchase in purchases:
    if portfolio.get(purchase[0]):
        portfolio[purchase[0]].append([purchase[1], purchase[2], purchase[3]])
    else:
        portfolio[purchase[0]] = [[purchase[1], purchase[2], purchase[3]]]

        for (key, value) in portfolio.items():
            print(f"------ {key} ------")

    totalValue = 0
    for item in value:
        totalValue += item[0] * item[2]
        print(f"{item[0]} shares at {item[2]} dollars each on {item[1]}")
        print(f"\nTotal value of stock in portfolio: ${totalValue}")
# Example output:

# ------ GE ------
# 100 shares at 48 dollars each on 01-jul-1998
# 200 shares at 56 dollars each on 10-sep-2001

# Total value of stock in portfolio: $16000