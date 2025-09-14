def caltotalprice(cart):
    if len(cart) == 0:
        return "Cart is empty."

    total_price = 0
    for item, price in cart.items():
        total_price += price

    if len(cart) > 5:
        total_price *= 0.9 

    return f"Total Price: {int(total_price)}"

cart = {}
n = int(input("Enter number of items in your cart: "))

for i in range(n):
    item = input(f"Enter name of item {i+1}: ")
    price = int(input(f"Enter price of {item}: "))
    cart[item] = price

print(caltotalprice(cart))