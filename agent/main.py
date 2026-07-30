from pathlib import Path

from explorer import RepositoryExplorer
from planner import Planner
from modifier import Modifier
from validator import Validator
from summary import Summary


def main():

    print("=" * 60)
    print("AI CODING AGENT")
    print("=" * 60)

    # --------------------------------------------
    # USER INPUT
    # --------------------------------------------

    user_request = input("\nEnter Product Requirement:\n\n> ").strip()

    if not user_request:
        print("\nRequirement cannot be empty.")
        return

    print("\nUser Request:")
    print(user_request)

    # --------------------------------------------
    # STEP 1 - Explore Repository
    # --------------------------------------------

    explorer = RepositoryExplorer("../target-repo")

    repository_files = explorer.list_files()

    print("\nRepository scanned successfully.")
    print(f"Files found : {len(repository_files)}")

    # --------------------------------------------
    # STEP 2 - Create Execution Plan
    # --------------------------------------------

    planner = Planner()

    plan = planner.create_plan(
        user_request,
        repository_files
    )

    if not plan:
        print("\nPlanner failed.")
        return

    print("\nPlanner Completed.")

    # --------------------------------------------
    # STEP 3 - Files to Modify
    # --------------------------------------------

    important_files = [
        "app/models/note.model.js",
        "app/controllers/note.controller.js",
        "app/routes/note.routes.js"
    ]

    modifier = Modifier()
    validator = Validator()
    summary = Summary()

    print("\nStarting Code Generation...")

    # --------------------------------------------
    # STEP 4 - Generate Code
    # --------------------------------------------

    for file in important_files:

        print("\n" + "=" * 60)
        print(f"Processing : {file}")
        print("=" * 60)

        original_code = explorer.read_file(file)

        if original_code is None:
            print("Unable to read file.")
            continue

        updated_code = modifier.generate_code(
            user_request=user_request,
            execution_plan=plan,
            filename=file,
            original_code=original_code
        )

        if not updated_code:
            print("Code generation failed.")
            continue

        # ---------------- Validation ----------------

        errors = validator.validate(file, updated_code)

        is_valid = validator.print_result(file, errors)

        if not is_valid:
            print("\nSkipping file because validation failed.")
            continue

        # ---------------- Save Generated Copy ----------------

        filename = Path(file).name

        explorer.save_generated_file(
            filename,
            updated_code
        )

        # ---------------- Update Repository ----------------

        explorer.write_file(
            file,
            updated_code
        )

        print(f"Repository Updated : {file}")

        summary.add_file(file)

    # --------------------------------------------
    # STEP 5 - Final Summary
    # --------------------------------------------

    summary.print_summary()


if __name__ == "__main__":
    main()