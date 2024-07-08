import requests

# URL of the Dracula novel on Project Gutenberg
url = 'https://www.gutenberg.org/files/345/345-0.txt'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Get the content of the response
    dracula_text = response.text
    
    # Save the content to a file
    with open('dracula.txt', 'w', encoding='utf-8') as file:
        file.write(dracula_text)
    
    print("Dracula novel has been downloaded and saved as 'dracula.txt'.")
else:
    print(f"Failed to download the novel. Status code: {response.status_code}")

