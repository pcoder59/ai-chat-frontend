import ollama

def chat(model_selected, content):
    print('Waiting for response...')

    try:
        response = ollama.chat(model=model_selected, messages=[
            {
                'role': 'user',
                'content': content,
            },
        ]) 

        print(response['message']['content'])
    except ollama.ResponseError as e:
        if e.status_code == 404:
            print('Model Not Found! Trying to Pull Model...')
            try:
                ollama.pull(model_selected)
                chat(model_selected, content)
            except ollama.ResponseError as e:
                print('Model Selected Does Not Exist!')
                exit(-1)
        else:
            print('An Error Occured!')

model_selected = input('Enter Model to Use (default: llama2-uncensored): ')

if model_selected == '':
    model_selected = 'llama2-uncensored'

while True:
    content = input('Enter your prompt (/bye to exit): ')

    if content == '/bye':
        exit(0)

    chat(model_selected, content)