A simple python application that uses LLm to generate summaries from ascii(.adoc) documents.
the project provides a small streamlit web intterface where the users can upload AsciiDoc file, clean its contents, generate an Ai powered summary , and then download the results as text file.

Technologies:

Python,
OpenAI API,
Streamlit,
Docker,
Docker compose,
python-dotenv,
AsciiDoc.

Docker Compose is used to manage the application container and its environment configuration.


Installation:

1. Clone the repository

git clone https://github.com/brahimelhainouni-ui/llm-doc-summarizer.git

cd llm-doc-summarizer

2. Create a virtual environment

python -m venv venv

Activate it on Git Bash:

source venv/Scripts/activate


3. Install dependencies

pip install -r requirements.txt

API Key Setup

The application requires an OpenAI API key.

Create a .env file in the project directory:

OPENAI_API_KEY= here your key

The .env file is excluded from Git using .gitignore.

dont commit your API key to GitHub.

Run the Application:

Start the Streamlit application with:

streamlit run app.py

Streamlit will open the application in your browser.

Then:

Upload an .adoc file.

Click Summarize.

Wait for the generated summary.

Download the summary if needed.



project Goal:

This project was built as a practical introduction to:

Python application development

LLM API integration

Document preprocessing

Environment variable management

Streamlit web applications

Building and documenting a small end-to-end AI application.
