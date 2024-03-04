# Create a tuple containing the names of menu sections:

menu_sections = ("Drinks", "snacks", "Appetizers ", "Entrees", "specials", "Desserts")
# snacks, meals, drinks, and dessert.
# Print the tuple.
print(menu_sections)

# Create a list of items for one of the menu sections.
drinks = ["Orange juice", "Wine", "Water", "Milk"]

# Create a list of prices for each of the menu items in the previous list.
drinks_prices = [4.30, 8.99, 3.99, 5.25]

# Ask a user to input a new item and append it to the relevant list.
drinks.append(input("What drink would you like to add? "))


# Ask a user to input the price of the new item, referenced using list indexing
# and append it to the relevant list.
drinks_prices.append(float(input(f"What is the price of {drinks[-1]}? ")))

# Print the menu and prices.
print(drinks)
print(drinks_prices)

# Ask the user which item to remove from the menu.
remove_item = input("Which item would you like to remove from the menu? ")


# Find the index of the item and save it as a variable.
index = drinks.index(remove_item)

# Remove the item from the menu list using remove().
drinks.remove(remove_item)

# Remove the item from the prices list using pop().
drinks_prices.pop(index)

# Print the menu and prices again to confirm removal.
print(drinks)
print(drinks_prices)

# Find the most expensive price on the menu.
print(f"Most expensive price: {max(drinks_prices)}")

# Find the cheapest price on the menu.
print(f"Cheapest price: {min(drinks_prices)}")

# Find the cost if someone bought every item on the menu.
print(f"Total cost: {sum(drinks_prices)}")

# Confirm that the menu and prices lists are the same length.
print(
    f"Length of menu is {len(drinks)} and the prices length is "
    + str(len(drinks_prices))

)