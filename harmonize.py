import openai
import os
from typing import List
import langchain

# Set up your OpenAI API credentials
key = os.getenv("OPENAI_API_KEY")
openai.api_key = key
# print(key)

def call_openai_api(prompt):
    # Define the parameters for the completion
    params = {
        'model': 'text-davinci-003',  # The model you want to use
        'prompt': prompt,
        'max_tokens': 3000  # The maximum number of tokens to generate
    }

    # Call the OpenAI API
    response = openai.Completion.create(**params)

    # Retrieve the generated text from the API response
    generated_text = response.choices[0].text.strip()

    return generated_text

# Example usage
prompt = "Once upon a time"
# print(call_openai_api(prompt))

import csv

def read_csv_first_n_lines(file_path: str, n: int) -> List[str]:
    lines: List[str] = []
    with open(file_path, 'r') as csv_file:
        for line in range(n):
            lines.append(csv_file.readline())
    return lines

# Example usage
csv_path = '../OpenClimate/harmonize/data/raw/C2ES_US_ghg_targets/US-states-c2es-targets.csv'
n_lines = 5
raw_5 = read_csv_first_n_lines('../OpenClimate/harmonize/data/raw/C2ES_US_ghg_targets/US-states-c2es-targets.csv', n_lines)
processed_5 = read_csv_first_n_lines('../OpenClimate/harmonize/data/processed/C2ES_US_ghg_targets/Target.csv', n_lines)


prompt = """
Hi, I have two datasets that have different data schemas and I want to harmonize them so that they use the same one. Can you provide python code that 
would turn Data Schema B into the same structure as Data Schema A, taking into account the field names, field descriptions and making sure that units 
and types of values are consistent?

Schema B's data is stored in '../OpenClimate/harmonize/data/raw/C2ES_US_ghg_targets/US-states-c2es-targets.csv'

The python code should read the the file for Schema B and write a new file that mimics schema A.
The python code should save the schemaA csv in the folder the script is running in.
Only output runnable python code.

The first {row_count} rows of Schema B are:
{raw}
The first {row_count} rows of Schema A are:
{processed}
""".format(row_count=n_lines, raw=''.join(raw_5), processed='\n'.join(processed_5))

print(prompt)
openai_response = call_openai_api(prompt)
print(openai_response)



def execute_python_code(code):
    try:
        exec(code)
        return "Execution successful"
    except Exception as e:
        return f"Execution failed: {str(e)}"

# Example usage
execution_result = execute_python_code(openai_response)
print(execution_result)
