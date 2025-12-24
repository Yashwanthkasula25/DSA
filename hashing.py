class DictHashTable:
    def __init__(self):
        self.table = {}  # Using built-in dictionary

    def insert(self, key, value):
        self.table[key] = value  # Insert or update

    def get(self, key):
        return self.table.get(key, None)  # Returns None if key not found

    def display(self):
        print("\nHash Table Contents:")
        for key, value in self.table.items():
            print(f"{key} → {value}")


# --- Main Program ---
ht = DictHashTable()

while True:
    print("\n--- MENU ---")
    print("1. Insert")
    print("2. Get value")
    print("3. Display table")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        key = input("Enter key: ")
        value = input("Enter value: ")
        ht.insert(key, value)
        print("Inserted successfully.")
    elif choice == '2':
        key = input("Enter key to search: ")
        val = ht.get(key)
        if val is not None:
            print("Value:", val)
        else:
            print("Key not found.")
    elif choice == '3':
        ht.display()
    elif choice == '4':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Try again.")
            