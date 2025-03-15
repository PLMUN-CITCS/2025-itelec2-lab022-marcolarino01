# LARINO MARCO ANTONIO M.
# ITELECT2
# Laboratory #22 - Guided Coding Exercise:
# Variables, Literals, and Case-Sensitivity in Python 

def display_menu():
    print("Menu:")
    print("1. Greet User")
    print("2. Check Even/Odd")
    print("3. Exit")
    print("Enter your choice (1-3): ", end='')
    
def handle_menu_choice(choice: int) -> bool:
    if choice == 1:
        greet_user()
    elif choice == 2:
        even_odd_checker_action()
    elif choice == 3:
        print("Exciting program. Goodbye!")
        return True
    else:
        print("Invald choice. Please enter a number between 1 and 3.")
    return False

def greet_user():
    print("Hello! Welcome!")

def even_odd_checker_action():