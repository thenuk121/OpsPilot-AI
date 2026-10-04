from database.database import create_tables


def main():
    create_tables()

    print("OpsPilot database initialized successfully!")


if __name__ == "__main__":
    main()