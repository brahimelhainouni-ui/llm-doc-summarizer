import os

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

client = OpenAI()


def clean_adoc(filename):
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()

    clean_text = ""

    for line in lines:
        line = line.strip()

        if line == "":
            continue

        if line.startswith("="):
            line = line.lstrip("=").strip()

        clean_text += line + "\n"

    return clean_text


def summarize(text):
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
