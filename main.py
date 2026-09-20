with open("example.adoc", "r", encoding="utf-8") as file:
    lines = file.readlines()

clean_text = ""

for line in lines:
    line = line.strip()

    # Skip empty lines
    if line == "":
        continue

    # Remove AsciiDoc heading symbols at the start of lines
    if line.startswith("="):
        line = line.lstrip("=").strip()

    clean_text += line + "\n"

print(clean_text)
