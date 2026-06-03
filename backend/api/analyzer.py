import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

class CodeAnalyzer:
    def __init__(self):
        self.api_key = os.environ.get("GEMINI_API_KEY")
        if self.api_key:
            genai.configure(api_key=self.api_key)
            # Use gemini-2.5-flash as it is available and has quota
            self.model = genai.GenerativeModel('gemini-2.5-flash')
        else:
            self.model = None

    def analyze_code(self, code_snippet: str) -> str:
        if not self.model:
            return "Error: Gemini API key is not configured. Please set the GEMINI_API_KEY in your backend .env file."

        system_prompt = """You are an expert AI Coding Tutor. Your goal is to analyze user-submitted code and provide highly structured, beginner-friendly feedback.
You MUST format your response exactly matching the following 6 sections. Do not deviate from this format.

1. **Code Analysis**
   * Summary of what the code is trying to do.

2. **Mistakes Found**
   * List each issue with explanation. If there are no mistakes, explicitly say "No mistakes found".

3. **Beginner Explanation**
   * Simple explanation of why the mistake happens. Avoid complex technical jargon. Provide step-by-step explanations.

4. **Corrected Code**
   * Provide improved working code in a markdown block.

5. **Key Concept**
   * Mention the main programming concept involved.

6. **Practice Exercises**
   * Generate 2-3 small exercises related to the mistake to help the user learn.
   * Exercises should gradually increase in difficulty.
   * Include hints but not full solutions.
"""
        
        full_prompt = f"{system_prompt}\n\nPlease analyze the following code:\n\n```python\n{code_snippet}\n```"

        try:
            response = self.model.generate_content(
                full_prompt,
                generation_config=genai.types.GenerationConfig(
                    temperature=0.7,
                    max_output_tokens=1500,
                )
            )
            return response.text
        except Exception as e:
            return f"An error occurred while analyzing the code: {str(e)}"
