# Mathlete: AI Math Tutor

A simple Python package that uses the OpenAI API to implement an AI-powered math tutor answering elementary level math questions. You can choose to either run an interactive tutoring session or evaluate the AI based on a pre-set list of questions.

## Prerequisites

- Python 3.6 or later
- OpenAI Python client `openai`
- Update your Open AI key in the `app.py` file

Before running the application, please make sure to install all necessary packages using the following command: \
`pip install -r requirements.txt`

## Usage

1. Interactive mode:
`python src/app.py interactive`

2. Evaluation mode:
`python src/app.py evaluate`

The evaluate mode will use the `questions.txt` file to evaluate the AI. Ensure that the `questions.txt` file is formatted correctly, with each line containing a dictionary with 'question' and 'answer' keys.
