# Program to write user input to a file, append more data, and display the final content

def write_to_file(filename):
    user_input = input("Enter some text to write to the file: ")
    with open(filename, 'w') as file:
        file.write(user_input + '\n')
    print(f"Data written to '{filename}'.")

def append_to_file(filename):
    additional_input = input("Enter additional text to append: ")
    with open(filename, 'a') as file:
        file.write(additional_input + '\n')
    print("Additional data appended to the file.")

def read_and_display_file(filename):
    print("\nFinal content of the file:")
    with open(filename, 'r') as file:
        for line in file:
            print(line.strip())

# Main execution
file_name = 'output.txt'
write_to_file(file_name)
append_to_file(file_name)
read_and_display_file(file_name)
