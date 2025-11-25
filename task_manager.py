class Menu:

    def __init__(self, order_id, food_menu, price):
        """
        Initializing the Menu class with food menus.
        """
        self.food_menu = food_menu
        self.order_id = order_id
        self.price = price


# Sample food menu dictionary
food_menu = [
    Menu(1, "Burger", 75.00),
    Menu(2, "Pizza", 80.00),
    Menu(3, "Pasta", 50.00),
    Menu(4, "Salad", 30.00),
]


def display_food_menu():
    """
    Function to display food menu items and their prices.
    """

    print("\n-----Food Menu-------:\n")
    # Loop through the food menu and print each item
    # with its price
    for item in food_menu:
        print(
            f"Order ID: {item.order_id}, Food Item: {item.food_menu}, "
            f"Price: R{item.price:.2f}"
        )
    print()


def create_order(new_id, food_item, new_price):
    """
    Function to create a new order with order ID and and add
    it to the food menu.
    """
    new_id = len(food_menu) + 1
    new_price = 130.00
    food_item = Menu(new_id, "Ribs and Wings", new_price)
    food_menu.append(food_item)

    print(f"\nOrder {new_id} created successfully!\n")


def read_order(order_id):
    """
    Function to read and display the current order items
    based on the order_id.
    """
    for item in food_menu:
        if item.order_id == order_id:
            print(
                f"\nOrder found - ID: {item.order_id}, Food Item: "
                f"{item.food_menu}, Price: R{item.price:.2f}\n"
            )
            return
    print(f"\nOrder with ID {order_id} not found.\n")


def update_order(order_id, new_food_item, new_price):
    """
    Function to update the food items and prices of the food menu
    based on their order ID.
    """
    for item in food_menu:
        if item.order_id == order_id:
            item.food_menu = new_food_item
            item.price = new_price
            print("\nOrder updated successfully!\n")
            return
    print(f"\nOrder with ID {order_id} not found.\n")


def delete_order(order_id):
    """
    Function to delete an order based on its order ID.
    """
    for i, item in enumerate(food_menu):
        if item.order_id == order_id:
            del food_menu[i]
            print("\nOrder deleted successfully!\n")
            return
    print(f"\nOrder with ID {order_id} not found.\n")


# Demonstrate CRUD operations
display_food_menu()
create_order(5, "Oyster", 60.00)
display_food_menu()
read_order(2)
update_order(3, "Chicken strips", 35.00)
display_food_menu()
delete_order(4)
display_food_menu()
