from database.database import create_tables
from agents.inventory_agent import ask_model

from tools.inventory_tools import change_stock_quantity

change_stock_quantity("Tomatoes", 5)
def main():
    create_tables()

    print("=== OpsPilot AI ===")

    user_message = input("You: ")

    response = ask_model(user_message)

    print("OpsPilot:", response)


if __name__ == "__main__":
    main()