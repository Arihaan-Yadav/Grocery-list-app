def main_func():
    grocery_list = [] # The original list
    while True:
        grocery_item = input("Add grocery item (q to quit): ").strip().lower() # Asks for grocery item
        if grocery_item == "q":
            break # To quit
        if not grocery_item:
            print("Item can't be empty!")
            continue
        while True:
            validation = input("Are you sure? [(y)es/(n)o]: ").strip().lower() # To valid if user really wants to add the product
            if validation == "y":
                grocery_list.append(grocery_item)
                break
            elif validation == "n":
                break
            else:
                print("Invalid!")
        print(f"Your current list: {grocery_list}") # Responds with the current list
        removal = input("Wanna remove an item? [(y)es/(n)o]: ").strip().lower() # To remove an item from the list
        if removal == "y":
            if not grocery_list:
                print("Your list is empty, nothing to remove!")
                continue
            while True:
                remove_what = input("What item to remove? (q to cancel): ").strip().lower()
                if remove_what == "q":
                    break
                elif remove_what in grocery_list:
                    grocery_list.remove(remove_what)
                    break
                print("Invalid!")
            print(f"Your current list: {grocery_list}")
        elif removal == "n":
            continue
        else:
            print("Invalid!")

if __name__ == "__main__":
    main_func()