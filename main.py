from curses.ascii import isalpha, isdigit
import re
from todoist import TodoistAPI
import config

choosedOptions = []
dictTypeNumber = {}
dictTypeDay = {}

breakfastMeals = "\n1 2 Toast, 2 Eggs\n2 100g Nuts, 2 Bananas\n3 3 Toast, 3 Plums, 100g Peanut Butter\n"
lunchMeals = "\n1 200g Buckwheat, 200g Cottage Cheese, 250g Broccoli\n2 200g Buckwheat, 200g Mozzarella, 1 Cucumber, 1 Tomato\n3 200g Quinoa, 200g Cheddah Cheese, 200g Broccoli\n4 300g Whole Grain Pasta, 2 Gherkins, 50g Chicken Meat Sausage, 60g Mayonnaise, 100g Yogurt, 50g Corn\n"
dinnerMeals = "\n1 250g Oatmeal Pithy, 1 Apple, 125g Frozen Fruit\n2 250g Oatmeal Pithy, 1 Apple, 1 Banana\n"

lWithAllOptions = {breakfastMeals: "breakfast",
                   lunchMeals: "lunch", dinnerMeals: "dinner"}

optionsBreakfast = []
optionsLunch = []
optionsDinner = []

lWithNumbers = []
lWithStrings = []

finalList = []


def parserTodoist(para, val):
    finalList = []
    for key, value in lWithAllOptions.items():
        if value == para:
            splittedPara = key[1:-1].split("\n")
            getCorrectOption = splittedPara[val-1]
            getAllItems = "".join(getCorrectOption[1:].split(","))
            nums = re.findall(r'\d+', getAllItems)
            lWithNumbers.append(nums)
            lWithNumbersFlatten = (
                [item for sublist in lWithNumbers for item in sublist])
            for i in range(len(lWithNumbersFlatten)):
                lWithNumbersFlatten[i] = int(
                    lWithNumbersFlatten[i]) * dictTypeDay[para]
    stringToAdd = ""
    splittedCorrectOption = getCorrectOption.split(",")
    for i in splittedCorrectOption:
        i = i.split(" ")
        for j in i:
            if any(char.isdigit() for char in j) == False:
                stringToAdd = stringToAdd + j + " "
        lWithStrings.append(stringToAdd.rstrip().lstrip())
        stringToAdd = ""
    for i in range(len(lWithNumbersFlatten)):
        if (lWithNumbersFlatten[i] > 50):
            lWithNumbersFlatten[i] = str(lWithNumbersFlatten[i]) + "g"
        finalList.append(str(lWithNumbersFlatten[i]) + " " + lWithStrings[i])
    return finalList


def addToTodoist(para):
    key = config.API_TOKEN
    api = TodoistAPI(key)
    api.sync()
    for i in para:
        try:
            task = api.add_item(content=i, project_id=config.PROJECT_ID_INIT)
        except Exception as error:
            print("Some error happened during the API call to Todoist.")


def todoist():
    for key, value in dictTypeNumber.items():
        result = parserTodoist(key, value)
    resultAsString = " ".join(result)
    print(
        "The following list will be added to the grocery list. [y/n] \n\n"+resultAsString)
    while (True):
        i = input()
        if i != "y" and i != "n" and i != "kill me":
            print("\nNo valid input.")
            continue
        elif i == "n" or i == "kill me":
            exit()
        addToTodoist(result)
        print("\nAdded items to Grocery list.")
        exit()


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
    while (True):
        try:
            input = getInput()
            if str(input) not in optionsBreakfast:
                print("\nNo valid input.")
                continue
        except ValueError as e:
            print("\nNo valid input.")
            continue
        dictTypeNumber.update({"breakfast": input})
        break


def lunch():
    while (True):
        try:
            input = getInput()
            if str(input) not in optionsLunch:
                print("\nNo valid input.")
                continue
        except ValueError as e:
            print("\nNo valid input.")
            continue
        dictTypeNumber.update({"lunch": input})
        break


def dinner():
    while (True):
        try:
            input = getInput()
            if str(input) not in optionsDinner:
                print("\nNo valid input.")
                continue
        except ValueError as e:
            print("\nNo valid input.")
            continue
        dictTypeNumber.update({"dinner": input})
        break


def getInput():
    i = input()
    if i == "kill me":
        exit()
    return int(i)


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
    while (True):
        try:
            input = getInput()
        except ValueError as e:
            print("\nNo valid input.")
            continue
        daysBreakfast = input
        dictTypeDay.update({"breakfast": daysBreakfast})
        print("\nHow many lunch meals do you want to shop?")
        break
    while (True):
        try:
            input = getInput()
        except ValueError as e:
            print("\nNo valid input.")
            continue
        daysLunch = input
        dictTypeDay.update({"lunch": daysLunch})
        print("\nHow many dinner meals do you want to shop?")
        break
    while (True):
        try:
            input = getInput()
        except ValueError as e:
            print("\nNo valid input.")
            continue
        daysDinner = input
        dictTypeDay.update({"dinner": daysDinner})
        break
    chooseMeal(daysBreakfast, daysLunch, daysDinner)


if __name__ == "__main__":
    parser()
    start()
