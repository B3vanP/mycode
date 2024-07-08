# Open the existing 'dracula.txt' file, count lines containing the word 'vampire', and write them to 'vampytimes.txt'
vampire_count = 0

try:
    with open('dracula.txt', 'r', encoding='utf-8') as dracula_file, open('vampytimes.txt', 'w', encoding='utf-8') as vampy_file:
        for line in dracula_file:
            if 'vampire' in line.lower():
                vampy_file.write(line)
                vampire_count += 1
    print(f"Number of lines containing the word 'vampire': {vampire_count}")
except FileNotFoundError:
    print("The file 'dracula.txt' was not found in the current directory.")

