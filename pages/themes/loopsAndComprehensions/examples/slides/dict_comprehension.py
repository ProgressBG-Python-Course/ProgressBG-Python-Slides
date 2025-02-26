from pprint import pprint # needed for preaty print

# #Example: Counting word frequency in a text
# text = "apple banana apple apple banana plum"
# words = text.split()

# word_frequency = {word: words.count(word) for word in set(words)}
# print(word_frequency)
# # {'apple': 3, 'banana': 2, 'plum': 1}

# #Example: Converting API response data to a more useful format
# api_response = [
#     {"product_id": "P123", "price": 59.99, "stock": 120},
#     {"product_id": "P456", "price": 29.99, "stock": 300},
#     {"product_id": "P789", "price": 14.99, "stock": 50}
# ]

# inventory = {item["product_id"]: {"price": item["price"], "stock": item["stock"]}
#              for item in api_response}

# pprint(inventory, indent=4)

# Filtering sales data for a quarterly report
sales_data = {
    'Q1': {'Jan': 10000, 'Feb': 12000, 'Mar': 15000},
    'Q2': {'Apr': 14000, 'May': 16000, 'Jun': 18000},
    'Q3': {'Jul': 17000, 'Aug': 19000, 'Sep': 21000},
    'Q4': {'Oct': 20000, 'Nov': 22000, 'Dec': 25000}
}
# Get quarters with average sales above 18000
high_performing_quarters = {q: sum(months.values())/len(months)
                            for q, months in sales_data.items()
                            if sum(months.values())/len(months) > 18000}
pprint(high_performing_quarters, indent=4)
