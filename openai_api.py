import os
from dotenv import load_dotenv
import openai

load_dotenv()

openai_key = os.getenv("OPENAI_API_KEY")

def get_openai_response(prompt, purpose):
    try:
        purposes = {
            'explain': "Explain the following code:",
            'debug': "Debug the following code and explain the issues:",
            'code': "Write code to accomplish the following task:"
        }

        complete_prompt = f"{purposes[purpose]}\n\n{prompt}"
        
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": complete_prompt}
            ],
            max_tokens=1000,
            n=1,
            temperature=0.5,
        )
        
        return response.choices[0].message.content
    except Exception as e:
        print("Error interacting with openai API:", e)
        return str(e)