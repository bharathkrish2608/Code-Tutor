import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('GEMINI_API_KEY')
print(f"API Key found: {bool(api_key)}")

genai.configure(api_key=api_key)

# The user's list showed 'models/gemini-2.5-flash', etc.
test_models = [
    'gemini-1.5-flash',
    'gemini-1.5-pro',
    'gemini-2.0-flash',
    'gemini-2.5-flash',
    'gemini-pro'
]

for name in test_models:
    print(f"Testing {name}...")
    try:
        model = genai.GenerativeModel(name)
        response = model.generate_content("Hello", generation_config={"max_output_tokens": 5})
        print(f"  SUCCESS: {name} -> {response.text}")
        break  # Found one!
    except Exception as e:
        print(f"  FAIL: {name} -> {str(e)[:150]}")
