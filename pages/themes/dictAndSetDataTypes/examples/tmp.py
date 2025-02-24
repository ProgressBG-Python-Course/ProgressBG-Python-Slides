### Get max value in list:
numbers = [2.50, 2.43, 3.50]
print( max(numbers) )

prices = {
    "apples": 2.50,
    "oranges": 2.43,
    "bananas": 3.50
}
### Get max value in a dict
print( max(prices.values()) )

### Get the key of max value in a dict
print( max(prices, key=prices.get) )