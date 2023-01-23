import functions_framework
import json
import prompt_gatherer

@functions_framework.http
def http_prompts_gatherer(request):

        if request.method == 'GET':
            prompt_gatherer.main()

            data = open('prompts.json')
            prompts = json.load(data)
            data.close()

            return prompts
        else:
            return "Not appropiate HTTP method. Try HTTP GET."
