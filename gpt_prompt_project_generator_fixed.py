import os
import openai

# Define prompts mapped to file paths
prompt_map = {
    "main.py": """# Create a FastAPI app with a /health endpoint that returns JSON""",
    "requirements.txt": """# Required packages for FastAPI and running locally""",
    "Dockerfile": """# Dockerfile to run FastAPI app""",
    ".github/workflows/ci.yml": """# GitHub Actions workflow to build and test a FastAPI app""",
    "terraform/main.tf": """# Terraform to create an S3 bucket with tags and a random suffix""",
    "README.md": """# FastAPI + GitHub Actions + Terraform demo generated using GitHub Copilot"""
}

# Set your OpenAI API key (use environment variable or replace directly)
openai.api_key = ""

# Create folders and generate files based on prompts
for filepath, prompt in prompt_map.items():
    print(f"Generating {filepath} from prompt: {prompt[:60]}...")
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )
    code = response['choices'][0]['message']['content']

    # Ensure directory exists (skip if root)
    dir_path = os.path.dirname(filepath)
    if dir_path:
        os.makedirs(dir_path, exist_ok=True)

    with open(filepath, "w", encoding="utf-8") as file:
        file.write(code.strip())

print("✅ Project structure generated using prompts.")
