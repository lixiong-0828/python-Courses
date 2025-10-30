import os

# FILEPATH = "./output/output_file.txt"
FILEPATH = "output_file.txt"

def make_file():
    print("Making file...")
    with open(FILEPATH,"w") as file:
        pass

def get_contents(filepath=FILEPATH):
    if os.path.exists(filepath) == False:
        # print("File doesn't exist")
        make_file()
    """This function will return the contents of the filepath."""
    with open(filepath, "r") as file:
        contents = file.readlines()
    return contents


def write_to_file(contents, filepath=FILEPATH):
    if os.path.exists(filepath) == False:
        make_file()
    """This function will write the contents of the filepath."""
    with open(filepath, "w") as file:
        file.writelines(contents)


# Only execute from [functions.py]
# Not execute call from [maim.py]
if __name__ == "__main__":
    print("This is the main function")
# print("This is the main function from module folder")
