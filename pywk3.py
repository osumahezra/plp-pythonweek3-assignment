def calculate_discount(price, discount_percent):
    """
    Calculate the discount amount and the final price after applying the discount.

    :param price: Original price of the item
    :param discount_percent: Discount percentage to apply
    :return: Tuple containing the discount amount and the final price
    """
    
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
    else:
        discount_amount = 0
        final_price = price
    return final_price

price = float(input("What is the price of the item "))
percentage_discount =float(input("What is the discount "))
final_price = calculate_discount(price, percentage_discount)
print(f"pay the sum of ${final_price:.2f} at the counter")
