import string
import sys

list_unit = {"piece", "size", "ml", "l", "kg", "g"}
list_size = ["tiny", "small", "medium", "large", "huge"]
list_action = ["chop"]
list_ingredients = []
list_recipes = []

string_help = "------------------------------\n"\
              "0 - for generating random recipe\n" \
              "1 - interact with recipes\n" \
              "  11 - add new recipe\n" \
              "  12 - edit recipe\n" \
              "  13 - delete recipe\n" \
              "2 - interact with ingredients\n" \
              "  22 - add new recipe\n" \
              "  23 - edit recipe\n" \
              "  24 - delete recipe\n" \
              "h - display detailed help\n" \
              "e - exit app\n" \
              "------------------------------"


class Ingredient:
    def __init__(self, name, unit):
        self.name = name
        self.unit = unit

    def delete_ingredient(self):
        self.delete_ingredient()


class Recipe:
    def __init__(self, name):
        self.recipe_name = name
        self.recipe_ingredients_list = []
        self.recipe_notes = ""
        self.recipe_steps = []

    def save_note(self, notes):
        self.recipe_notes = notes


def check_ingredient_already_in_list(string_name):
    for item in list_ingredients:
        if item.name == string_name:
            return False
    return True


# loads ingredients from file to dict
def read_ingredients():
    f = open("src/ingredients.txt", "r")
    items = f.read().split(";")
    for item in items:
        if item == "":
            continue
        name, unit = item.split(":")
        name = name.replace("_", " ")
        if check_ingredient_already_in_list(name):
            continue
        if unit not in list_unit:
            print("error in file to load with following unit: " + unit)
            exit(0)

        list_ingredients.append(Ingredient(name, unit))
    f.close()


# add new ingredient to file and dict
def new_ingredient():
    f = open("src/ingredients.txt", "a")

    name = input("name: ")
    if check_ingredient_already_in_list(name):
        print("ingredient already exists")
        return

    unit = input("unit: ")
    if unit not in list_unit:
        unit = input("unit fix: ")

    list_ingredients.append(Ingredient(name, unit))

    name = name.replace(" ", "_")
    strint_to_add = name + ":" + unit + ";"
    f.write(strint_to_add)
    f.close()


def save_recipe_to_dict(passed_string):
    print(passed_string)
    name, ingredients, steps, notes = passed_string.split(";")
    name = name[1:(len(name)-1)]
    ingredients = ingredients[1:(len(ingredients)-1)]
    steps = steps[1:(len(steps)-1)]
    notes = notes[1:(len(notes)-1)]

    print("name: "+name)
    print("ingredients: " + ingredients)
    print("steps: " + steps)
    print("notes: " + notes)
    print("----------- exited saving -----------")


# loads recipes from file to dict
def read_recipe():
    f = open("src/recipes.txt", "r")
    lines = f.read().split("!")
    lines.remove("")
    for recipe in lines:
        save_recipe_to_dict(recipe)
    f.close()


def new_recipe():
    pass


def process_action(action_string):
    match action_string:
        case "0":
            print("selected valid")
            return
        case "1":
            print("selected valid")
            return
        case "11":
            print("selected valid")
            return
        case "12":
            print("selected valid")
            return
        case "13":
            print("selected valid")
            return
        case "2":
            print("selected valid")
            return
        case "22":
            new_ingredient()
            return
        case "23":
            print("selected valid")
            return
        case "24":
            print("selected valid")
            return
        case "H":
            print(string_help)
            return
        case "E":
            print("bye!")
            exit(0)
        case _:
            print("Try again. " + string_help + "was not valid input")
            return


if __name__ == '__main__':
    print("WELCOME!")
    read_ingredients()
    print("Ingredients loaded ...")
    read_recipe()
    print("Recipes loaded ...")

    looped = True
    while looped:
        action = input("Choose next action [0 - display random recipe, 1 - recipe, 2 - ingredient, h - detailed help]: ")
        action = action.upper()
        process_action(action)

print("some wierd exit")
exit(0)
