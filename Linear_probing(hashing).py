class LinearProbingHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        for i in range(self.size):
            probe_index = (index + i) % self.size
            if self.table[probe_index] is None or self.table[probe_index][0] == "<deleted>":
                self.table[probe_index] = (key, value)
                print(f"Inserted: {key} → {value} at index {probe_index}")
                return
            elif self.table[probe_index][0] == key:
                self.table[probe_index] = (key, value)
                print(f"Updated: {key} → {value} at index {probe_index}")
                return
        print("Hash table is full! Cannot insert.")

    def search(self, key):
        index = self._hash(key)
        for i in range(self.size):
            probe_index = (index + i) % self.size
            if self.table[probe_index] is None:
                break
            if self.table[probe_index][0] == key:
                return self.table[probe_index][1]
        return None

    def delete(self, key):
        index = self._hash(key)
        for i in range(self.size):
            probe_index = (index + i) % self.size
            if self.table[probe_index] is None:
                break
            if self.table[probe_index][0] == key:
                self.table[probe_index] = ("<deleted>", None)
                print(f"Deleted: {key} at index {probe_index}")
                return
        print(f"Key '{key}' not found.")

    def display(self):
        print("\nHash Table:")
        for i, item in enumerate(self.table):
            print(f"{i}: {item}")


def main():
    size = int(input("Enter size of the hash table: "))
    ht = LinearProbingHashTable(size)

    while True:
        print("\n----- Menu -----")
        print("1. Insert")
        print("2. Search")
        print("3. Delete")
        print("4. Display Table")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            key = input("Enter key: ")
            value = input("Enter value: ")
            ht.insert(key, value)

        elif choice == "2":
            key = input("Enter key to search: ")
            result = ht.search(key)
            if result is not None:
                print(f"Found: {key} → {result}")
            else:
                print("Key not found.")

        elif choice == "3":
            key = input("Enter key to delete: ")
            ht.delete(key)

        elif choice == "4":
            ht.display()

        elif choice == "5":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
