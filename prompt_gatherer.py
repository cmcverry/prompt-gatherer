import json
import requests
import sys

# Retrieves API secret key from txt file
def get_api_key():
    with open('api-key.txt') as f:
        lines = f.readlines() 
        f.close()
    return (lines[0])


# makes a call to get_api_key() and makes an HTTP post request to OpenAI's completions API
# receives five questions from the OpenAI API, extracts them from the JSON response, and returns an array of strings of the 5 questions
def get_prompts(prompt_subject):
    api_key = get_api_key()
    subject = "social, philosophical, or economic"
    if prompt_subject:
        subject = prompt_subject

    prompt = f'one deep, probing and fun question about {subject}. ask what, why, or how. long question'
    url = "https://api.openai.com/v1/completions"
    payload= {'model': 'text-davinci-003', 'prompt': prompt, "max_tokens": 500, 'temperature': 0.9, 'n': 5}
    headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {api_key}'}

    r = requests.post(url, headers=headers, data=json.dumps(payload))
    print("status code:", r.status_code)
    response = json.loads(r.text)
    prompts = []
    for i in response["choices"]:
        prompts.append(i["text"].strip())
    
    print(prompts)
    return prompts

# Receives an array of strings (5 questions), encapsulates the array inside a dictionary and writes it to a json file
def export_prompts(arr):
    temp = {'prompt_list': arr}
    with open("prompts.json", "w") as out_file:
        json.dump(temp, out_file)
        out_file.close()


if __name__ == "__main__":
    prompt_subject = None
    if len(sys.argv) > 1:
        prompt_subject = sys.argv[1]

    prompts = get_prompts(prompt_subject)
    export_prompts(prompts)
    