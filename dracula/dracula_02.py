# Open the existing 'dracula.txt' file and print each line
try:
    with open('dracula.txt', 'r', encoding='utf-8') as file:
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("The file 'dracula.txt' was not found in the current directory.")

