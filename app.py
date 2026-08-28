


from db.session import init_db

if __name__ == "__main__":
    init_db()

    print("Database initialized successfully!")
    print("Database file: campus_companion.db")
    print("Tables created based on db/models.py")