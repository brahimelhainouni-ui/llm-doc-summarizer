import os

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

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

        if line == "":
            continue

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
