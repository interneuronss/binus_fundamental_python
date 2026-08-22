def read_biodata_from_file():
  with open("Biodata.txt", "r") as file:
    text = file.read()
    print(text)

def write_biodata_to_file():
  with open("Biodata.txt", "w") as file:
    name = input("Your name: ")
    age = input("Your age: ")
    address = input("Your address: ")
    email = input("Your email: ")
    file.write(f"Name: {name}\n")
    file.write(f"Age: {age}\n")
    file.write(f"Address: {address}\n")
    file.write(f"Email: {email}\n")

option = input("Choose an option (read/write): ")

if option == "read":
  read_biodata_from_file()
elif option == "write":
  write_biodata_to_file()
