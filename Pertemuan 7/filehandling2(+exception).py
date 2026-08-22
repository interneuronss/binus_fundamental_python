# WRITE
def write_to_file(filename, content):
    
    try:
        with open(filename, 'w') as file:
            file.write(content)
            file.write("\n")
        print(f"Content successfully written to {filename}")
    except IOError as e:
        print(f"Error writing to file: {e}")

# READ
def read_from_file(filename):
    
    try:
        with open(filename, 'r') as file:
            print(f"\nContent of {filename}:")
            print(file.read())
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
    except IOError as e:
        print(f"Error reading from file: {e}")

# APPEND
def append_to_file(filename, content):
    
    try:
        with open(filename, 'a') as file:
            file.write(content)
            file.write("\n") # Add a newline for readability if appending multiple times
        print(f"Content successfully appended to {filename}")
    except IOError as e:
        print(f"Error appending to file: {e}")

# MAIN
def run_file():
    
    while True:
        print("\n--- File Manager Menu ---")
        option = input("Choose an option (write/read/append/close): ").lower()

        if option == 'close':
            print("Exiting file manager. Goodbye!")
            break
        elif option in ['write', 'read', 'append']:
            filename = input("Enter the filename: ")
            if option == 'write':
                data = input("Enter the content to write: ")
                write_to_file(filename, data)
            elif option == 'read':
                read_from_file(filename)
            elif option == 'append':
                data = input("Enter the content to append: ")
                append_to_file(filename, data)
        else:
            print("Invalid option. Please choose from write, read, append, or close.")

# START
run_file()
