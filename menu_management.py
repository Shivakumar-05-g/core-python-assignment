def add_item(menu, item):
    if item not in menu:
        menu.append(item)

def remove_item(menu, item):
    if item in menu:
        menu.remove(item)
    else:
        print(f"{item} is not in the menu.")

def check_item(menu, item):
    if item in menu:
        return f"{item} is available"
    else:
        return f"{item} is not available"

menu = []
size = int(input("Enter number of initial menu items: "))
for i in range(size):
    item = input(f"Enter menu item {i+1}: ")
    menu.append(item)

a_item = input("Enter item to add: ")
r_item = input("Enter item to remove: ")
c_item = input("Enter item to check availability: ")

add_item(menu, a_item)
remove_item(menu, r_item)
availability = check_item(menu, c_item)


print("Updated menu:", menu)
print("Availability:", availability)
