# GroceryAutomation

## What?
Python CLI for automating grocery lists in Todoist. The available menu looks like this:

`breakfastMeals = "\n1 2 Toast, 2 Eggs\n2 100g Nuts, 2 Bananas\n"`
`lunchMeals = "\n1 200g Buckwheat, 200g Cottage Cheese, 250g Broccoli\n2 200g Buckwheat, 200g Mozzarella, 1 Cucumber, 1 Tomato\n"`
`dinnerMeals = "\n1 250g Oatmeal Pithy, 1 Apple, 100g Frozen Grapefruit\n2 250g Oatmeal Pithy, 1 Apple, 1 Banana\n"`

New menus can be added via changing the respective variables:

`breakfastMeals = "\n1 2 Toast, 2 Eggs\n2 100g Nuts, 2 Bananas\n3 100g Of New Items\n"`

## Future and possible improvements

Menus can be only extended with the variables `breakfastMeals, lunchMeals, DinnerMeals`. It would be easier to handle with the creation of an Google spreadsheet where its possible to input desired menus. The data from the spreadsheets could be imported into the script via API call.

## Dependencies

`Todoist API --> pip3 install todoist-python`

`Python 3.9.10`