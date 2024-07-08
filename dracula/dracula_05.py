# Open the existing 'dracula.txt' file and count lines containing the word 'vampire'
vampire_count = 0

try:
    with open('dracula.txt', 'r', encoding='utf-8') as file:
        for line in file:
            if 'vampire' in line.lower():
                print(line.strip())
                vampire_count += 1
    print(f"\nNumber of lines containing the word 'vampire': {vampire_count}")
except FileNotFoundError:
    print("The file 'dracula.txt' was not found in the current directory.")

