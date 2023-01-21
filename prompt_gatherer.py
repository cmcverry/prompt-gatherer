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


# makes requests to OpenAI's completions API to pair a string of hashtags to each previously generated discussion prompt
# returns array of tuples containing prompt questions and corresponding hashtags
def get_hashtags(prompts):
    api_key = get_api_key()
    prompts_w_hashtags = []

    for i in prompts:
        prompt = f'Create one to three hashtags related to this question: {i}'
        url = "https://api.openai.com/v1/completions"
        payload= {'model': 'text-davinci-003', 'prompt': prompt, "max_tokens": 100, 'temperature': 0.3}
        headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {api_key}'}

        r = requests.post(url, headers=headers, data=json.dumps(payload))
        print("status code:", r.status_code)
        response = json.loads(r.text)
        print(response)
        prompts_w_hashtags.append((i, response["choices"][0]["text"]))

    return prompts_w_hashtags


# Receives an array of strings (5 questions), encapsulates the array inside a dictionary and writes it to a json file
def export_prompts(arr):
    temp = {'prompt_list': arr}
    with open("prompts.json", "w") as out_file:
        json.dump(temp, out_file)
        out_file.close()


if __name__ == "__main__":
    prompt_subject = None
    hashtags = False

    if len(sys.argv) > 1:
        if sys.argv[1] and sys.argv[1] != "-HT":
            if len(sys.argv) > 2 and sys.argv[2] == "-HT":
                hashtags = True
            prompt_subject = sys.argv[1]

        elif sys.argv[1] == "-HT":
            hashtags = True
        
    prompts = get_prompts(prompt_subject)

    if hashtags:
        prompts = get_hashtags(prompts)
        
    export_prompts(prompts)
    