def discounted(price, discount, max_discount = 20):
    try:
        if price > 0:
            return float(price)
        if discount > 0:
            return float(discount)
        if max_discount > 0:
            return int(max_discount)
        else:
            raise TypeError
    except TypeError:
        print ('Не верный тип данных')
    except ValueError:
        print ('Не верный велью данных!')
    if max_discount >=100:
        raise ValueError('Слишком большая максимальная скидка')
    if discount >=max_discount: 
        price_with_discount =  price 
    else:
        price_with_discount = price - (price * discount / 100)
    return price_with_discount     
   
print(discounted(100,10))
