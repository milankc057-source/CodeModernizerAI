import os
import openai

# Set your OpenAI API key (if you have one)
openai.api_key = os.getenv("OPENAI_API_KEY", None)

PROJECTS_DIR = "uploaded_projects"
MODERNIZED_DIR = "modernized_projects"

os.makedirs(PROJECTS_DIR, exist_ok=True)
os.makedirs(MODERNIZED_DIR, exist_ok=True)

def mock_modernize_code(old_code, level="light"):
    """
    A smarter mock modernization function for testing without OpenAI.
    """
    lines = old_code.splitlines()
    new_lines = []

    for line in lines:
        # Remove old comments
        if line.strip().startswith("#"):
            continue
        # Fix indentation: replace tabs with 4 spaces
        line = line.replace("\t", "    ")
        new_lines.append(line)

    # Add modernized header
    modernized_code = f"# Smart mock modernized code\n# Level: {level}\n\n"
    modernized_code += "\n".join(new_lines)
    return modernized_code


def process_project(project_name, level="light", use_mock=False):
    input_file = os.path.join(PROJECTS_DIR, f"{project_name}.txt")
    output_file = os.path.join(MODERNIZED_DIR, f"{project_name}_modernized.txt")

    if not os.path.exists(input_file):
        print(f"Error: {input_file} does not exist!")
        return

    with open(input_file, "r", encoding="utf-8") as f:
        old_code = f.read()

    if use_mock or not openai.api_key:
        # Use mock modernization
        modernized_code = mock_modernize_code(old_code, level=level)
    else:
        # Use OpenAI modernization
        prompt = f"""
You are a code modernization AI. Update the following Python code to modern standards,
fix obvious bugs, improve structure, and keep the same functionality.
Modernization level: {level}

Old code:
{old_code}

Provide only the updated code.
"""
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=1500,
            temperature=0
        )
        modernized_code = response.choices[0].text.strip()

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(modernized_code)

    print(f"Project {project_name} has been modernized and saved to {output_file}")
