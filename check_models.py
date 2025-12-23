from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

# Paste your AIzaSy... key directly here if .env isn't working
KEY = "AIzaSyAprV8tWdA6kNutS-gpOzN1OrXslMkQocw" 

client = genai.Client(api_key=KEY)
print("Checking available models...")
for m in client.models.list(config={"query_base": True}):
    print(m.name)
