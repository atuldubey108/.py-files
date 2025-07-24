# Program to create 'sample.txt' if it doesn't exist,
# and then read and print its contents line by line
# with proper error handling.

def create_sample_file_if_missing(filename):
    try:
        with open(filename, 'x') as f:  # 'x' mode creates the file, raises error if it exists
            f.write("Hello, world!\nThis is a sample file.\nPython is awesome!\n")
            print(f"File '{filename}' created with sample content.\n")
    except FileExistsError:
        # File already exists – do nothing
        pass

def read_file_line_by_line(filename):
    try:
        with open(filename, 'r') as file:
            print("File content:")
            for line in file:
                print(line.strip())  # Removes extra newlines
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Main execution
file_name = 'sample.txt'
create_sample_file_if_missing(file_name)
read_file_line_by_line(file_name)

