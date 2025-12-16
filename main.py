"""
Name: Ahamid Adam, Kenneth Gomez, Ngor Ruot
Date: Dec 10, 2025

Main runner for Car Inventory Application.
Loads saved data, shows menu, and routes user actions.
"""

from function import *

load_data()

print("Welcome to the cars inventory system\n")

while True:
    choice = show_menu()

    if choice == "1":
        run_add()
    elif choice == "2":
        run_search()
    elif choice == "3":
        run_edit()
    elif choice == "4":
        run_remove()
    elif choice == "5":
        run_print()
    elif choice == "6":
        save_data()
    elif choice == "0":
        break
