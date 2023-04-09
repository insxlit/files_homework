import os


def read_file(print_data=False):
    """
    Function for reading file with cookbook
    :param print_data: input True to print cookbook in the terminal
    :return: dictionary of cookbook
    """

    # Reading the file
    with open("recipes.txt", "rt") as file:
        cookbook = {}
        for line in file:
            dish = line.strip()
            ingr_number = int(file.readline().strip())
            composition = []
            for ingredient in range(ingr_number):
                ingredient_name, quantity, measure = file.readline().strip().split(" | ")
                composition.append({
                    "ingredient_name": ingredient_name, "quantity": quantity, "measure": measure
                })
            file.readline()
            cookbook[dish] = composition

    # Print cookbook in the terminal
    if print_data:
        from pprint import pprint
        pprint(cookbook)

    return cookbook


def get_shop_list_by_dishes(dishes, person_count, print_data=False):
    """
    Function for making a shopping list
    :param dishes: list of dishes
    :param person_count: number of persons
    :param print_data: input True to print shopping list in the terminal
    :return: dictionary of shopping list
    """

    # Making the shopping list
    cookbook = read_file()
    shopping_list = {}
    for dish in dishes:
        if dish in cookbook:
            for ingredient in cookbook[dish]:
                if ingredient["ingredient_name"] not in shopping_list:
                    shopping_list[ingredient["ingredient_name"]] = {
                        "quantity": int(ingredient["quantity"]) * person_count,
                        "measure": ingredient["measure"]
                    }
                else:
                    shopping_list[ingredient["ingredient_name"]]["quantity"] \
                        += int(ingredient["quantity"]) * person_count

    # Print shopping list in the terminal
    if print_data:
        from pprint import pprint
        pprint(shopping_list)

    return shopping_list


if __name__ == "__main__":
    get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2, True)
