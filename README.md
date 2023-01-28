# Prompt Gatherer

NOTE: this is a variant I deployed as a Google Cloud Function. It is mostly the same as the version on my master branch but instead of a api-key.txt file, it uses api-key.json in the format { "key": "your key" }. Currently, by default prompt_subjects is set to 'any' and hashtags are retrieved on each request.
Documentation/tutorial for deployment can be found here: https://cloud.google.com/functions/docs/tutorials/http 


Prompt Gatherer is a microservice python program that is used by my Promptu app for gathering AI-generated random discussion prompts. 

The microservice makes calls to OpenAI's Completions API and receives five questions related to social, philosophical, or economic subjects. The response 
data are extracted, reformatted and written to a local JSON file where they might be accessed by other programs. API requests are made to OpenAI's text-davinci-003 model. 


## Instructions

Usage of this microservice requires an OpenAI Secret API Key, which you will need to acquire on your own.

With a Python3 interpreter and pip installed on your system, in your terminal navigate to the directory containing this program. 
1. Execute 'pip install -r requirements.txt' to install dependencies.
2. Copy your OpenAI Secret API Key to a local JSON file called 'api-key.json'
3. Execute 'Python ./prompt_gatherer.py' to run the program.
4. (optional) Including a '-HT' tag in CLI execution will generate corresponding hashtags for each discussion prompt.

By default the microservice uses 'social, philosophical or economic' as the default subject used by the AI to generate questions.
You can override the default subject by including a string argument when executing the program in the terminal.
For example, executing 'Python ./prompt_gatherer.py sports or movies' would generate prompt questions related to sports or movies.

For different output, changes can be made to the prompt/request sent to the OpenAI API by manually editing prompt_gatherer.py.
Documentation on the OpenAI API can be found here: https://beta.openai.com/docs/api-reference/completions

