# Notes
'''
functions which need to be fullfilled 
    1. selecting meals
    2. selecting amount of meals 
    3. create entries in todoist
    4. Make it usable for others

flow of the app
    1. Print how the app works
    2. User selects amount of meals for each category (breakfast, lunch, dinner). 0 if no meals for a categeory 
    3. menues are displayed and user needs to choose from one 
    4. if done user needs to confirm and items are automatically added to todoist

detailed flow of app (if not possible input gets typed in --> "No possible input." and new line gets displayed)
    1. run script
    2. Description gets displayed (with exit option == kill me)
        - You can exit the program at every time. Just type "kill me" without brackets.
    3. Display meal amount options (user needs to input something for next result 0 if 0 meals. If 0 meals choosen respond with "No meals choosen." and exit program). 
        1. How many breakfast meals do you wanna shop?
        2. How many lunch meals do you wanna eat?
        3. How many Dinner meals do you wanna eat?
    4. Display "Now choose meal." (displays now in the hyrarchy B,L,D meals. based on if certain option was choosen (Example: B=0,L=2,D=3 displays L,D but no B because not choosen))
    5. 
    
    Breakfast
        1. 2 Toast, 2 Eggs
        2. 100g nuts, 2 Bananas

    Lunch
        1. 200g Buckwheat, 200g Cottage Cheese, 250g Broccoli
        2. 200g Buckwheat, 200g Mozzarella, 1 Cucumber, 1 Tomato
    
    Dinner
        1. 250g Oatmeal Pithy, 1 Apple, 100g Frozen Grapefruit 
        1. 250g Oatmeal Pithy, 1 Apple, 1 Banana

    6. Confirm that you wish. y will add items to Todoist. n will exit the program.
        Breakfast: X times
        Lunch: X times
        Dinner: X times

        [y/n]

    7. if yes call Api and add amount of items to shopping list


    Create README at the end and create file with all dependencies


'''
numberBreakfast = 0
numberLunch = 0
numberDinner = 0

breakfastMeals = "\n1 2 Toast, 2 Eggs\n2 100g nuts, 2 Bananas\n"
lunchMeals =  "\n1 200g Buckwheat, 200g Cottage Cheese, 250g Broccoli\n2 200g Buckwheat, 200g Mozzarella, 1 Cucumber, 1 Tomato\n"
dinnerMeals =  "\n1 250g Oatmeal Pithy, 1 Apple, 100g Frozen Grapefruit\n2 250g Oatmeal Pithy, 1 Apple, 1 Banana\n"

optionsBreakfast = []
optionsLunch = []
optionsDinner = []


def test():
    l = ["1", "2"]
    if 1 in l:
        print("sss")

def parser():
    splittedBreakfast = breakfastMeals[1:-1].split("\n")
    for i in splittedBreakfast:
        optionsBreakfast.append(i[0])

    splittedLunch = lunchMeals[1:-1].split("\n")
    for i in splittedLunch:
        optionsLunch.append(i[0])
    
    splittedDinner = dinnerMeals[1:-1].split("\n")
    for i in splittedDinner:
        optionsDinner.append(i[0])

def breakfast():
    while(True):
        try:
            input = getInput()
            if str(input) not in optionsBreakfast:
                print("\nNo valid input.")
                continue
        except ValueError as e:
            print("\nNo valid input.")
            continue
        numberBreakfast = input
        break

def lunch():
    while(True):
        try:
            input = getInput()
            if str(input) not in optionsLunch:
                print("\nNo valid input.")
                continue
        except ValueError as e:
            print("\nNo valid input.")
            continue
        numberLunch = input
        break

def dinner():
    while(True):
        try:
            input = getInput()
            if str(input) not in optionsDinner:
                print("\nNo valid input.")
                continue
        except ValueError as e:
            print("\nNo valid input.")
            continue
        numberDinner = input
        break

def getInput():
    i = input()
    if i == "kill me":
        exit()
    return int(i)

def todoist():
    print("")

def chooseMeal(daysBreakfast, daysLunch, daysDinner):
    print("\nNow choose meal.")
    if daysBreakfast != 0 and daysLunch != 0 and daysDinner != 0:
        print("\nBreakfast:" + breakfastMeals)
        breakfast()
        print("\nLunch:" + lunchMeals)
        lunch()
        print("\nDinner:" + dinnerMeals)
        dinner()
    elif daysBreakfast != 0 and daysLunch != 0 and daysDinner == 0:
        print("\nBreakfast:" + breakfastMeals)
        breakfast()
        print("\nLunch:" + lunchMeals)
        lunch()
    elif daysBreakfast != 0 and daysLunch == 0 and daysDinner == 0:
        print("\nBreakfast:" + breakfastMeals)
        breakfast()
    elif daysBreakfast == 0 and daysLunch == 0 and daysDinner != 0:
        print("\nDinner:" + dinnerMeals)
        dinner()
    elif daysBreakfast == 0 and daysLunch != 0 and daysDinner != 0:
        print("\nLunch:" + lunchMeals)
        lunch()
        print("\nDinner:" + dinnerMeals)
        dinner()
    elif daysBreakfast != 0 and daysLunch == 0 and daysDinner != 0:
        print("\nBreakfast:" + breakfastMeals)
        breakfast()
        print("\nDinner:" + dinnerMeals)
        dinner()
    elif daysBreakfast == 0 and daysLunch != 0 and daysDinner == 0:
        print("\nLunch:" + lunchMeals)
        lunch()
    else:
        print("No meals choosen.")
        exit()
    todoist()

def start():
    daysBreakfast = 0 
    daysLunch = 0 
    daysDinner = 0 
    print("This is a script for automating your grocery planning.\nYou can exit the program at every time. Just type 'kill me' without quotation marks and hit enter.\n\nHow many breakfast meals do you want to shop?")
    while(True):
        try:
            input = getInput()
        except ValueError as e:
            print("\nNo valid input.")
            continue
        daysBreakfast = input
        print("\nHow many lunch meals do you want to shop?")
        break
    while(True):
        try:
            input = getInput()
        except ValueError as e:
            print("\nNo valid input.")
            continue
        daysLunch = input
        print("\nHow many dinner meals do you want to shop?")
        break
    while(True):
        try:
            input = getInput()
        except ValueError as e:
            print("\nNo valid input.")
            continue
        daysDinner = input
        break
    chooseMeal(daysBreakfast, daysLunch, daysDinner)

if __name__ == "__main__":
    parser()
    start()





    