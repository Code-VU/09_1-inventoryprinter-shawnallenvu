stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'ring': 1, 'apple': 12}

def displayInventory(inventory):
    # your code goes here

    item_total = 0      # Variable for counting total of inventory items
    
    print("Inventory:") # Start of print statement

    # Iterate through each inventory item and display the count then the item name
    for key in inventory:
        print(inventory[key], key)

        item_total += inventory[key] # Adding each item's quantity to a total

    print(f"Total number of items: {item_total}") # Displays the total number of inventory items

if __name__ == "__main__":
    displayInventory(stuff)
