# Import the Argparse package for later
import argparse

# Trigger a string output from the terminal
print('Hello from the command line!')

# Instatiate the Argparse package
parser = argparse.ArgumentParser()
# Create an argument called name
parser.add_argument("--name", help="Creates a new name.")
args = parser.parse_args()

# Output the name within the terminal calling argument
if args.name:
    print(f"My name is {args.name}.")