from database.database import create_tables

from services.inventory_service import (
    add_inventory_item,
    get_low_stock_inventory
)


def main():
    create_tables()

    add_inventory_item("Chicken", 8, 10)
    add_inventory_item("Rice", 40, 15)
    add_inventory_item("Tomatoes", 5, 12)

    low_stock_items = get_low_stock_inventory()

    print("=== OpsPilot AI ===")
    print("Low stock items:")

    for item in low_stock_items:
        print(
            f"- {item[1]}: "
            f"{item[2]} remaining "
            f"(minimum: {item[3]})"
        )


if __name__ == "__main__":
    main()