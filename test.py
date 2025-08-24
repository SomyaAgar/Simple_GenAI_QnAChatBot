import os
from dotenv import load_dotenv

# Load .env
load_dotenv()

# Get key
api_key = os.getenv("LANGCHAIN_API_KEY")

if not api_key:
    raise ValueError("LANGCHAIN_API_KEY not found in .env file or environment")

print("API key loaded successfully")  # for debugging