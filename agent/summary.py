class Summary:

    def __init__(self):
        self.modified_files = []

    def add_file(self, filename):
        """
        Add a modified file to the summary.
        """
        self.modified_files.append(filename)

    def print_summary(self):
        """
        Print the final summary.
        """

        print("\n" + "=" * 60)
        print("AI CODING AGENT SUMMARY")
        print("=" * 60)

        if not self.modified_files:
            print("\nNo files were modified.")
            return

        print("\nModified Files:\n")

        for file in self.modified_files:
            print(f"✔ {file}")

        print(f"\nTotal Files Modified : {len(self.modified_files)}")

        print("\nRepository updated successfully.")

        print("\nWorkflow Completed Successfully.")