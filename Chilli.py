print("Hello Welcome to Chilli's Bakery\nWhat is your name")

name = input()

print("It's nice to meet you " + name + " please have a seat")

menu = "Pizza, Biscuits, Cake, Bread"

print("What would you like from our menu?\nToday we are serving " + menu)

order = input()

print("Sounds good " + name + " your " + order + " will be ready in a moment.")

payment_method = input("Are you paying in cash or with a card\n")

if payment_method.lower() == "cash" :
    print("Your bill will be available when you are ready to leave")

elif payment_method.lower() == "card" :
    print("Since you will be paying with card you can scan the qr code stand on your table when leaving")

else:
    print("Invalid Payment Method")

input()

print("Thanks for coming\nSee you next time")