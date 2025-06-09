import cohere
import os
from dotenv import load_dotenv

load_dotenv()

co = cohere.Client(os.getenv('COHERE_API_KEY'))

def generate_blog_content(key_word):
    prompt = f"generate a blog for keyword : {key_word}"
    response = co.generate(model='command', prompt=prompt, max_tokens=20, temperature=0.7)
    return response.generations[0].text