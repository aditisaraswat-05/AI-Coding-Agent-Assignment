import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


class Modifier:

    def __init__(self):

        api_key = os.getenv("OPENROUTER_API_KEY")

        if not api_key:
            raise ValueError("OPENROUTER_API_KEY not found.")

        self.client = OpenAI(
            api_key=api_key,
            base_url="https://openrouter.ai/api/v1"
        )

    def generate_code(
        self,
        user_request,
        execution_plan,
        filename,
        original_code
    ):

        prompt = f"""
You are an expert software engineer.

User Request:
{user_request}

Execution Plan:
{execution_plan}

Target File:
{filename}

Original File Content:

{original_code}

Instructions:
1. Modify ONLY this file.
2. Preserve all existing functionality.
3. Implement the requested feature.
4. Return ONLY the complete updated source code.
5. Do NOT add explanations.
6. Do NOT use markdown.
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
                temperature=0.2,
            )

            code = response.choices[0].message.content.strip()

            # Remove markdown if the model returns it
            if code.startswith("```"):
                lines = code.splitlines()

                if lines[0].startswith("```"):
                    lines = lines[1:]

                if lines and lines[-1].startswith("```"):
                    lines = lines[:-1]

                code = "\n".join(lines)

            return code

        except Exception as e:

            print("\n========== MODIFIER ERROR ==========\n")
            print(e)

            return None