def receipt_formatter(name, quantity, price):
    quantity = int(quantity)
    price = float(price)

    subtotal = quantity * price
    tax = round(subtotal * 0.075, 2)
    total = round(subtotal + tax, 2)

    return (
        f"Customer: {name}\n"
        f"Subtotal: {subtotal:.1f}\n"
        f"Tax: {tax}\n"
        f"Total: {total}"
    )


print(receipt_formatter("Ada", 2, 100))
