import ebooklib
from ebooklib import epub
import re

def extract_text_inside_quotes(epub_file_path):
    # Open the EPUB file
    book = epub.read_epub(epub_file_path)

    # Initialize an empty list to store extracted text
    extracted_text = []

    # Iterate through all items in the EPUB book
    for item in book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
        # Extract text content from the item
        content = item.get_content().decode('utf-8')

        # Use regular expression to find text inside double quotation marks
        matches = re.findall(r'"([^"]*)"', content)

        # Add the matched text to the extracted_text list
        extracted_text.extend(matches)

    return extracted_text

# Replace 'your_epub_file.epub' with the path to your EPUB file
epub_file_path = 'your_epub_file.epub'
result = extract_text_inside_quotes(epub_file_path)

# Print the extracted text
for text in result:
    print(text)
