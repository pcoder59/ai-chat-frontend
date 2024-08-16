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
        print('An Error Occured!')

def pullmodel(model_to_pull):
    try:
        ollama.pull(model_to_pull)
        return True
    except ollama.ResponseError as e:
        print('Error Pulling Model!')
        return False

def getmodelnames():
    modelnames = []
    models = ollama.list()
    models = models['models']
    for model in models:
        modelnames.append(model['name'].replace(':latest', ''))
    return modelnames

def selectmodel(models):
    print("Enter /list for list of installed models")
    print("Enter name of uninstalled model to try pulling it")
    model_selected = input(f'Enter Model to Use (default: {models[0]}): ')
    if model_selected == '':
        return models[0]
    if model_selected == '/list':
        i = 1
        print('Models Installed:')
        for model in models:
            print(f'{i}. {model}')
            i += 1
        return selectmodel(models)
    elif model_selected not in models:
        print('Model Not Found! Trying to Pull Model...')
        success = pullmodel(model_selected)
        if success:
            print(f'Model Pulled Successfully. Using {model_selected}')
            return model_selected
        else:
            selectmodel(models)
    else:
        return model_selected

def modelnotfound():
    model_to_pull = input('Enter Model to Pull: ')
    success = pullmodel(model_to_pull)
    if success:
        return [model_to_pull]
    else:
        print('Model Not Found!')
        modelnotfound()

model_selected = ''

models = getmodelnames()

if len(models) == 0:
    print('No Models Found!')
    models = modelnotfound()
else:
    model_selected = models[0]
    model_selected = selectmodel(models)

while True:
    content = input('Enter your prompt (/bye to exit): ')

    if content == '/bye':
        exit(0)

    chat(model_selected, content)