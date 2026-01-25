class ChainingHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [{} for _ in range(size)]  # Each chain is now a dict
#####
    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        self.table[index][key] = value  # insert or update
        print(f"Inserted/Updated: {key} → {value}")

    def get(self, key):
        index = self._hash(key)
        return self.table[index].get(key, None)

    def delete(self, key):
        index = self._hash(key)
        if key in self.table[index]:
            del self.table[index][key]
            print(f"Deleted: {key}")
            return True
        else:
            print(f"Key '{key}' not found.")
            return False

    def display(self):
        print("\nHash Table:")
        for i, chain in enumerate(self.table):
            print(f"{i}: {chain}")


# ==== Main ====

def main():
    size = int(input("Enter size of hash table: "))
    ht = ChainingHashTable(size)

    while True:
        print("\nMenu:")
        print("1. Insert")
        print("2. Get value by key")
        print("3. Delete")
        print("4. Display")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            key = input("Enter key: ")
            value = input("Enter value: ")
            ht.insert(key, value)

        elif choice == "2":
            key = input("Enter key to search: ")
            value = ht.get(key)
            if value is not None:
                print(f"Found: {key} → {value}")
            else:
                print("Key not found.")

        elif choice == "3":
            key = input("Enter key to delete: ")
            ht.delete(key)

        elif choice == "4":
            ht.display()

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
