from pprint import pprint

stock = [
    {'name': 'iPhone 12 Plus', 'stock': 24, 'price': 65432.1, 
     'recomended': ['Samsung Galaxy S21', 'iPhone 12']},
    {'name': 'samsung galaxy s21', 'stock': 8, 'price': 50000.0, 'discount':5000},
    {'name': 'xiaomi mi11','stock': 42, 'price': 38000.5}
]
print(type(stock))
print(type(stock[0]))
print(type(stock[0]['recomended']))