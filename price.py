def discounted(price, discount, max_discount = 20):
    price = abs(price)
    discount = abs(discount)
    max_discount = abs (max_discount)
    if max_discount >=100:
        raise ValueError ('Идите нафиг, господа!')
    if discount >=max_discount: 
        price_with_discount = price 
    else:
        price_with_discount = price - (price * discount / 100)
    return price_with_discount

print(discounted(100, 50, 220))
print(discounted(100, 50))
print(discounted(100, 50, 60 ))