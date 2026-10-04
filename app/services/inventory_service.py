import csv

from models.inventory import InventoryItem


def load_inventory(file_path):
    inventory = []

    with open(file_path, mode="r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            item = InventoryItem(
                name=row["name"],
                quantity=int(row["quantity"]),
                minimum_stock=int(row["minimum_stock"])
            )

            inventory.append(item)

    return inventory

def get_low_stock_items(inventory):
    low_stock_items = []

    for item in inventory:
        if item.is_low_stock():
            low_stock_items.append(item)

    return low_stock_items