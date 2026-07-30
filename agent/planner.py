import os

from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()


class Planner:
    def __init__(self):
        api_key = os.getenv("OPENROUTER_API_KEY")

        if not api_key:
            raise ValueError("OPENROUTER_API_KEY not found in .env file.")

        self.client = OpenAI(
            api_key=api_key,
            base_url="https://openrouter.ai/api/v1"
        )

    def create_plan(self, user_request, repository_files):
        """
        Creates an execution plan for implementing the user's request.
        """

        # Convert repository file list into text
        repository_summary = "\n".join(
            str(file) for file in repository_files
        )

        # Prompt for the LLM
        prompt = f"""
You are a Senior Software Architect.

You are given a list of files from an existing software project.

Repository Files:
{repository_summary}

User Request:
{user_request}

Your task is to create a short execution plan.

Requirements:
- Preserve existing functionality.
- Make only the necessary changes.
- Prefer minimal modifications over creating new modules.
- Identify which existing files are likely to be modified.
- Return only a numbered execution plan.
"""

        try:
            response = self.client.chat.completions.create(
                model="google/gemma-4-26b-a4b-it:free",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.3,
            )

            plan = response.choices[0].message.content

            print("\n========== EXECUTION PLAN ==========\n")
            print(plan)

            return plan

        except Exception as e:
            print("\n========== LLM ERROR ==========\n")
            print(str(e))
            return None