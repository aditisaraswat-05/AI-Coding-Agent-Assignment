import re


class Validator:

    def validate(self, file_name, code):

        errors = []

        if not code:
            errors.append("Empty response received from LLM.")

        if "```" in code:
            errors.append("Markdown code block detected.")

        if "I'm sorry" in code:
            errors.append("LLM returned explanation instead of code.")

        if "Here is the updated" in code:
            errors.append("LLM returned explanation instead of code.")

        # Detect broken .then syntax
        if re.search(r"\nthen\s*\(", code):
            errors.append("Broken '.then()' syntax detected.")

        if file_name.endswith(".js"):

            if "module.exports" not in code and "exports." not in code:
                errors.append("No exports found.")

        return errors

    def print_result(self, file_name, errors):

        print()
        print("=" * 60)
        print(file_name)
        print("=" * 60)

        if len(errors) == 0:

            print("Validation Passed")
            return True

        print("Validation Failed\n")

        for error in errors:
            print("-", error)

        return False