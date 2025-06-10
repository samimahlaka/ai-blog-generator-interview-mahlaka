import cohere
import os
from dotenv import load_dotenv

load_dotenv()

co = cohere.Client(os.getenv('COHERE_API_KEY'))

def generate_blog_content(key_word):
    prompt = f""" Write a detailed, SEO-friendly blog post about: {key_word}.

                Include:

                1. A clear title.
                2. An introduction.
                3. Several sections with headings.
                4. At least one section recommending related products or services.
                5. Placeholder affiliate links in markdown format, e.g. [Product Name](https://example.com/affiliate-link).
                6. A conclusion with a call to action.

                Make it engaging and easy to read.
                """

    
    response = co.generate(model='command', prompt=prompt, max_tokens=40, temperature=0.7)
    return response.generations[0].text