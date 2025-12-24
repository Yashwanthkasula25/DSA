# File Handling in Python - All operations in one code



# -------- 1. Writing to a file (w mode) --------
# This will create the file if it doesn't exist, or overwrite it if it does
with open("example.txt", "w") as file:
   file.write("Hello, World!\n")
   file.write("This is written using 'w' mode.\n")




# -------- 2. Reading from a file (r mode) --------
# Opens the file for reading and prints its content
with open("example.txt", "r") as file:
   content = file.read()
   print("Reading from file:\n", content)




# -------- 3. Appending to a file (a mode) --------
# Adds new lines to the end of the file without deleting existing content
with open("example.txt", "a") as file:
   file.write("This line is appended.\n")
   file.write("Appending another line using 'a' mode.\n")




# -------- 4. Reading file line by line --------
# Read lines one by one using readline() and readlines()
with open("example.txt", "r") as file:
   print("\nUsing readline():")
   print(file.readline())  # Reads one line

   print("Using readlines():")
   lines = file.readlines()  # Reads all remaining lines into a list
   for line in lines:
       print(line.strip())




# -------- 5. Checking file properties --------
# Showing the file name, mode, and whether it is closed
with open("example.txt", "r") as file:
   print("\nFile name:", file.name)
   print("File mode:", file.mode)
   print("Is file closed?", file.closed)

print("Is file closed after 'with' block?", file.closed)  # Should be True




# -------- 6. Deleting a file --------
# Use os module to remove a file
import os

filename = "example_to_delete.txt"

# Creating the file to demonstrate deletion
with open(filename, "w") as file:
   file.write("This file will be deleted.\n")

# Deleting the file
if os.path.exists(filename):
   os.remove(filename)
   print(f"\nFile '{filename}' deleted.")
else:
   print(f"\nFile '{filename}' not found.")




# -------- 7. Handling file not found error --------
try:
   with open("non_existent.txt", "r") as file:
       print(file.read())
except FileNotFoundError:
   print("\nError: The file does not exist.")



