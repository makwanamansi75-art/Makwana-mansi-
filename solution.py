print("Flower Shop")

flowers = ["Rose", "Lily", "Lotus"]
price = [50, 80, 100]

flower = input("Enter flower: ")
qty = int(input("Enter qty: "))   # convert to integer

if flower in flowers:
    index = flowers.index(flower)
    total = price[index] * qty

    if total > 300:
        discount = total * 0.05
    else:
        discount = 0

    final_amount = total - discount

    print("Flower:", flower)
    print("Total:", total)
    print("Discount:", discount)
    print("Final Amount:", final_amount)

    for i in range(3):
        print("Sold")

else:
    print("Flower not available")

print("End")