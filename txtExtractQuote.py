import re

def extract_text_from_txt(txt_file_path):
    # Read the content of the text file
    with open(txt_file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Use regular expression to find all quotes inside double quotation marks
    quotes = re.findall(r'“(.*?)”', content)

    return quotes

def save_to_txt(file_path, extracted_text):
    with open(file_path, 'w', encoding='utf-8') as file:
        for text in extracted_text:
            file.write('- ' + text + '\n')

# Replace 'your_text_file.txt' with the path to your text file
txt_file_path = 'output.txt'
result = extract_text_from_txt(txt_file_path)

# Print the extracted quotes
for quote in result:
    print(quote)

# Replace 'quotesFromEpub.txt' with the desired output file path
output_file_path = 'quotesFromEpub.txt'
save_to_txt(output_file_path, result)

print(f"All quotes extracted and saved to {output_file_path}")


print(f"Extracted quotes saved to {output_file_path}")
