from services.inventory_service import (
    load_inventory,
    get_low_stock_items
)


def main():

    inventory = load_inventory("data/inventory.csv")

    low_stock_items = get_low_stock_items(inventory)

    print("=== OpsPilot AI ===")
    print("Items requiring attention:")

    for item in low_stock_items:
        print(
            f"- {item.name}: "
            f"{item.quantity} remaining "
            f"(minimum: {item.minimum_stock})"
        )


if __name__ == "__main__":
    main()