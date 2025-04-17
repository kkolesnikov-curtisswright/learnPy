# Write your Python program below

def read_file_contents(file_path):
    try:
        with open(file_path, 'r') as file:
            print("File opened")
    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")