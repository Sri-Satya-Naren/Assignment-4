with open("output.txt", "w") as file:
    data = input("Enter text to write into the file: ")
    file.write(data + "\n")

print("Data written to output.txt successfully.")
with open("output.txt", "a") as file:
    extra_data = input("Enter additional text to append: ")
    file.write(extra_data + "\n")

print("Additional data appended to output.txt successfully.")
with open("output.txt", "r") as file:
    content = file.read()

print("\nFinal content of output.txt:")
print(content)