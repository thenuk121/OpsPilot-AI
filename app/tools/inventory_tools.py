from services.inventory_service import (
    get_low_stock_inventory,
    update_inventory_quantity
)


def check_low_stock():
    """Return inventory items that are at or below minimum stock."""

    items = get_low_stock_inventory()

    if not items:
        return "All inventory items have sufficient stock."

    results = []

    for item in items:
        name = item[1]
        quantity = item[2]
        minimum_stock = item[3]

        results.append(
            f"{name}: {quantity} remaining "
            f"(minimum required: {minimum_stock})"
        )

    return "\n".join(results)


def change_stock_quantity(name, new_quantity):
    """Update the current quantity of an inventory item."""

    if new_quantity < 0:
        return "Quantity cannot be negative."

    update_inventory_quantity(name, new_quantity)

    return f"{name} stock updated to {new_quantity}."