def discounted(price, discount, max_discount = 20):
    price = abs(price)
    discount = abs(discount)
    max_discount = abs (max_discount)
    if max_discount >=100:
        raise ValueError ('Слишком большая максимальная скидка!')
    if discount >=max_discount: 
        price_with_discount = price 
    else:
        price_with_discount = price - (price * discount / 100)
    return price_with_discount

print(discounted(100, 50, 20))
print(discounted(100, 20, 20))
print(discounted(100, 50, 600 ))