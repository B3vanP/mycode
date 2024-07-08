import os
import re

def find_word_in_files_and_filenames(search_word):
    result_files = []
    search_pattern = re.compile(re.escape(search_word), re.IGNORECASE)
    dir_count = 0

    for dirpath, _, filenames in os.walk('/'):
        dir_count += 1
        if dir_count % 100 == 0:
            print(f"Scanning directory: {dirpath}")

        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            try:
                # Check if the search word is in the filename
                if search_pattern.search(filename):
                    result_files.append(file_path)
                    continue  # Skip reading the file if the filename matches

                # Check if the search word is inside the file contents
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                    for line in file:
                        if search_pattern.search(line):
                            result_files.append(file_path)
                            break  # Stop searching the file after finding the word
            except (OSError, IOError) as e:
                print(f"Error opening/reading file: {file_path}. Error: {e}")

    return result_files

if __name__ == "__main__":
    word_to_find = input("Enter the word to search for in filenames and file contents: ")
    
    results = find_word_in_files_and_filenames(word_to_find)
    results_file_path = os.path.join(os.path.dirname(__file__), 'bff_results.txt')
    
    with open(results_file_path, 'w') as f:
        f.write(str(results))
    
    print(f"Results have been saved to {results_file_path}")
    
    if results:
        print("Files with the word in their name or contents:")
        for result in results:
            print(result)
    else:
        print("No files found with the word in their name or contents.")

