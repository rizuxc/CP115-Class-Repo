#This is the number of items stored and given by user
Coffee = int(input("Coffee: "))
Muffin = int(input("Muffin: "))
Water = int(input("Water: "))

#This is the price of the items as well as the final total price
tCoffee = Coffee * 3.50
tMuffin = Muffin * 2.10
tWater = Water * 1.05
subtotal = tCoffee + tMuffin + tWater
tax = subtotal * 0.06
finalTotal = subtotal + tax

#This is the receipt
print(f"========== RECEIPT ==========\n"
      f"Item\tPrice\tQty\tTotal\n"
      f"Coffee\t$3.50\t{Coffee}\t${tCoffee: .2f}\n"
      f"Muffin\t$2.10\t{Muffin}\t${tMuffin: .2f}\n"
      f"Water\t1.05\t{Water}\t${tWater: .2f}\n"
      f"------------------------------\n"
      f"Subtotal\t\t${subtotal: .2f}\n"
      f"Tax (6%)\t\t${tax: .2f}\n"
      f"Total\t\t\t${finalTotal: .2f}\n")