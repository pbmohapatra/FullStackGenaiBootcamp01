
import os
from dotenv import load_dotenv

load_dotenv(".env")

huggingfacehub_api_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")
google_api_key = os.getenv("GOOGLE_API_KEY")
openai_api_key = os.getenv("OPENAI_API_KEY")
anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")
groq_api_key = os.getenv("GROQ_API_KEY")
openrouter_api_key = os.getenv("OPENROUTER_API_KEY")

print("Hugging Face Hub API Token:", huggingfacehub_api_token)
print("Google API Key:", google_api_key)
print("OpenAI API Key:", openai_api_key)
print("Anthropic API Key:", anthropic_api_key)
print("Groq API Key:", groq_api_key)
print("OpenRouter API Key:", openrouter_api_key)

