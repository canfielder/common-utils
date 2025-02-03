import os

def find_project_root(root_file = "root.txt"):
    """Find the project root directory by locating a specified file."""
    # Find current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # iteratue up through project structure, looking for root file
    while current_dir != os.path.dirname(current_dir):  # Stop at filesystem root
        if root_file in os.listdir(current_dir):
            return current_dir
        current_dir = os.path.dirname(current_dir)
        
    raise FileNotFoundError(f"{root_file} not found in any parent directory.")