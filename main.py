import os

from dotenv import load_dotenv
from openai import OpenAI


# Load environment variables from the .env file.
load_dotenv()

# Create the OpenAI client using the API key from the environment.
client = OpenAI()


def clean_adoc_text(text):
    """
    Clean AsciiDoc text before sending it to the AI.

    Removes empty lines and AsciiDoc heading markers
    such as "=" and "==".
    """
    cleaned_text = ""

    for line in text.splitlines():
        line = line.strip()

        # Skip empty lines.
        if line == "":
            continue

        # Remove AsciiDoc heading markers.
        if line.startswith("="):
            line = line.lstrip("=").strip()

        cleaned_text += line + "\n"

    return cleaned_text


def clean_adoc(filename):
    """
    Read an AsciiDoc file and clean its contents.
    """
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()

    return clean_adoc_text(text)


def summarize(text):
    """
    Send document text to the OpenAI API and return a summary.
    """
    response = client.responses.create(
        model="gpt-4o-mini",
        instructions="You summarize documents. Write a short, clear summary.",
        input=f"Summarize the following document:\n\n{text}",
    )

    return response.output_text


if __name__ == "__main__":
    text = clean_adoc("example.adoc")

    print("Document:")
    print(text)

    print("\nSUMMARY:")
    summary = summarize(text)
    print(summary)