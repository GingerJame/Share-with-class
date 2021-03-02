priceList = {
    'V' : 7.35, # vandas
    'M' : 9.80, # miltonia
    'C' : 10.00 # cattleya
}
while True:
    member = input("Are you a member? (Say no if you're a traitor). [Y] or [N] > " )
    if member.upper() == 'Y':
        member = True
        break
    elif member.upper() == 'N':
        member = False
        break
    else:
        print("Please enter Y or N")
while True:
    orchid = input("Which Orchid would you like? theyre all pretty good tbh but, [V]andas, [M]iltonia, or [C]attleya > ")
    if orchid.upper() not in ['V','M','C']:
        print("Pretty please enter V, M or C thank you thanks")
    else:
        break
print("Member status:",member)
print("Chosen orchid:",orchid)
# TO DO Quantity input, finalPrice calculation

# while True:
#     amoun = input("How many do youwannt Orchid would you like? (Between 0-20): ")
#     if amoun not in range(0,20):
#         print("Please enter a number between 0 and 20 PLEASE PELASE PLEASE")
#     else:
#         price = quantity * priceList[orchid]
#         if member:
#             price *= 0.90
#         if quantity >= 5:
#             price *= 0.95
#             break
# print("Your final price is > $", format(price, ' .2f'))
# This was my first attempt at calculating and printing the final price. I encountered an error
# Where the terminal continually told me to enter a number between 0 and 20, both before and after an input was entered.

while True:
    try:
        quantity = int(input("hey hi hello how many flowah you want? (Between 1 and 20)> "))
        if quantity < 0 or quantity > 21:
            print("Hello make between 1 and 20 please and thank you thanks")
        else:
            price = quantity * priceList[orchid]
            if member == True:
                price *= 0.90
            if quantity >= 5:
                price *= 0.95
            price = round(price,2)
            break
    except ValueError:
        print("I asked for a number here, dummy.")

print("Your final price is ALOT probably! $",format(price,'.2f'))
