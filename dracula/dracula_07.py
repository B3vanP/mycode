with open("./vampytimes.txt", "r", encoding="utf-8") as file:
    data = file.read()

# Remove any non-ASCII characters
cleaned_data = "".join(char for char in data if ord(char) < 128)

with open("./vampytimes_cleaned.txt", "w", encoding="utf-8") as file:
    file.write(cleaned_data)
