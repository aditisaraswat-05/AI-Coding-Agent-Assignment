from pathlib import Path


class RepositoryExplorer:

    def __init__(self, repo_path):
        self.repo_path = Path(repo_path)


    # Scan Repository


    def list_files(self):

        files = []

        ignore_folders = {
            ".git",
            "node_modules",
            "venv",
            "__pycache__",
            ".idea",
            ".vscode"
        }

        for file in self.repo_path.rglob("*"):

            if any(folder in file.parts for folder in ignore_folders):
                continue

            if file.is_file():
                files.append(file.relative_to(self.repo_path))

        return files

  
    # Read File

    def read_file(self, file_path):

        path = self.repo_path / file_path

        try:

            with open(path, "r", encoding="utf-8") as f:
                return f.read()

        except Exception as e:

            print(f"Error reading {file_path}")
            print(e)

            return None

    
    # Write Back To Repository
    

    def write_file(self, file_path, content):

        path = self.repo_path / file_path

        try:

            path.parent.mkdir(parents=True, exist_ok=True)

            with open(path, "w", encoding="utf-8") as f:
                f.write(content)

            print(f"Repository Updated : {file_path}")

        except Exception as e:

            print(f"Error writing {file_path}")
            print(e)

    
    # Save Generated Copy

    def save_generated_file(self, filename, content):

        generated_folder = Path("generated")

        generated_folder.mkdir(exist_ok=True)

        output_file = generated_folder / filename

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"Generated file saved : {output_file}")