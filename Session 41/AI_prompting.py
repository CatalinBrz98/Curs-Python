from openai import OpenAI

client = OpenAI(
    api_key='API_KEY')

messages = [{'role': 'system', 'content': 'Esti un poet programator in devenire.'},
            {'role': 'user', 'content': 'Scrie un haiku despre Python.'}]

response = client.chat.completions.create(
    model='gpt-5-nano',
    messages=messages
)

print(response.choices[0].message.content)
