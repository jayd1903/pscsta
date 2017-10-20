#Define variables
population = 0
city_name = ""
generation = 0
economy_condition = 0
satisfaction = 0
game_still_on = True
#Starting loop
name_ask = raw_input("Welcome to City Simulator! Name your city! >>> ")
city_name = name_ask
print("-------------------------------\nYou are now the proud mayor of " + city_name + "!")
while game_still_on == True:
    choice = raw_input("-------------------------------\nYou are on generation " + str(generation) + ".\nYour population is "+ str(population) + ".\nWhat would you like to do?\n1. Build more houses.\n2. Increase Taxes\n3. Decrease Taxes\n4. Trade with other cities.")
