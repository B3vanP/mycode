# Open the existing 'dracula.txt' file and print lines containing the word 'vampire'
try:
    with open('dracula.txt', 'r', encoding='utf-8') as file:
        for line in file:
            if 'vampire' in line.lower():
                print(line.strip())
except FileNotFoundError:
    print("The file 'dracula.txt' was not found in the current directory.")

