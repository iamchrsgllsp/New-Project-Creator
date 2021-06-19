import os

def create_project(path, project_name):
    os.mkdir(path)
    with open(f"{path}\main.py", "w") as f:
        f.write("!usr/bin/python")
    with open(f"{path}\README.md", "w") as f:
        f.write(f"Project name: {project_name}")
    os.popen(f"code {path}")
    os.popen(f"cd {path}")
    

def files():
    filepath = input("Please select filepath....\n")
    if os.path.isdir(filepath):
        project_name = input("Please enter project name...\n")
        if " " in project_name:
            project_name =project_name.replace(" ", "_")
            
        newpath = filepath + "\\" + project_name    
        if os.path.isdir(newpath):
            print("Filepath already exists, please reselect filepath for project")
            files()  
        else:
            print("Filepath doesn't exist")
            create_project(newpath, project_name)
            print(f"New project started {newpath}")

def os_check():
    if os.name == "nt":
        print("Windows machine")
        files()
    else:
        print("Sorry, Currently unsupported OS")

os_check()