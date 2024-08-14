import os

def create(name):
    if os.path.exists(name):
        print(f"Error: The file '{name}' already exists!")
        return
    with open(name, "x") as file:
        pass

def save(name, content):
    if not os.path.exists(name):
        print(f"Error: The file '{name}' isn't in your folder :(")
        return
    with open(name, "w") as file:
        file.write(content)

def getFileContent(name):
    if not os.path.exists(name):
        print(f"Error: The file '{name}' isn't in your folder :(")
        return None
    with open(name, "r") as file:
        output = file.read()
    return output