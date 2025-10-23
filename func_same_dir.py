def get_contents(filepath="./output/output_file.txt"):
    """This function will return the contents of the filepath."""
    with open(filepath, "r") as file:
        contents = file.readlines()
    return contents


def write_to_file(contents, filepath="./output/output_file.txt"):
    """This function will write the contents of the filepath."""
    with open(filepath, "w") as file:
        file.writelines(contents)


# Only execute from [functions.py]
# Not execute call from [maim.py]
if __name__ == "__main__":
    print("This is the main function")
    print(get_contents("../output/output_file.txt"))

print("This is the main function from module folder")
