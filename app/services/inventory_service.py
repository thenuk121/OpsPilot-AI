from database.database import get_connection


def add_inventory_item(name, quantity, minimum_stock):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT OR IGNORE INTO inventory
        (name, quantity, minimum_stock)
        VALUES (?, ?, ?)
        """,
        (name, quantity, minimum_stock)
    )

    connection.commit()
    connection.close()


def get_all_inventory():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, name, quantity, minimum_stock
        FROM inventory
    """)

    rows = cursor.fetchall()
    connection.close()

    return rows


def get_low_stock_inventory():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, name, quantity, minimum_stock
        FROM inventory
        WHERE quantity <= minimum_stock
    """)

    rows = cursor.fetchall()
    connection.close()

    return rows


def update_inventory_quantity(name, new_quantity):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE inventory
        SET quantity = ?
        WHERE name = ?
        """,
        (new_quantity, name)
    )

    connection.commit()
    connection.close()