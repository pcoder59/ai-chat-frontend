# AI Chat Frontend

A Simple Frontend for Ollama written in python

# Requirement

- Ollama should be hosted on the system: refer [Ollama Github](https://github.com/ollama/ollama)
- Ollama python module: refer [ollama-python Github](https://github.com/ollama/ollama-python)

# Usage

- Run main.py and enter the model you want to use. By default it uses first model found on host if not enetered
- Enter /list at the prompt for a list of models already pulled
- If a model not on the list is entered, will try to pull it via ollama
- Type the prompt and wait for the response