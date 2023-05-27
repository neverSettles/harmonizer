import openai

# Set up your OpenAI API credentials
openai.api_key = os.getenv("OPENAI_API_KEY")

def call_openai_api(prompt):
    # Define the parameters for the completion
    params = {
        'model': 'text-davinci-003',  # The model you want to use
        'prompt': prompt,
        'max_tokens': 100  # The maximum number of tokens to generate
    }

    # Call the OpenAI API
    response = openai.Completion.create(**params)

    # Retrieve the generated text from the API response
    generated_text = response.choices[0].text.strip()

    return generated_text

# Example usage
prompt = "Once upon a time"
generated_text = call_openai_api(prompt)
print(generated_text)