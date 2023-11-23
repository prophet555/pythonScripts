import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup

def extract_all_text(epub_file_path):
    # Open the EPUB file
    book = epub.read_epub(epub_file_path)

    # Initialize an empty string to store all text
    all_text = ''

    # Iterate through all items in the EPUB book
    for item in book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
        # Extract text content from the item
        content = item.get_content().decode('utf-8')

        # Use BeautifulSoup to parse HTML content
        soup = BeautifulSoup(content, 'html.parser')

        # Append the text of each item to the all_text string
        all_text += soup.get_text() + '\n'

    return all_text

# Replace 'your_epub_file.epub' with the path to your EPUB file
epub_file_path = r'C:\Users\mrbig\Documents\Walter Isaacson - Elon Musk-Simon & Schuster (2023).epub'

# Call the function with the specified EPUB file path
all_text = extract_all_text(epub_file_path)

# Replace 'output.txt' with the desired output file path
output_file_path = 'output.txt'
with open(output_file_path, 'w', encoding='utf-8') as file:
    file.write(all_text)

print(f"All text extracted and saved to {output_file_path}")

