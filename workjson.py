import json
import PyPDF2
import re
import os
def extract_links(pdf_file):
    a = PyPDF2.PdfReader(pdf_file)
    links = []
    for page_num in range(len(a.pages)):
        b = a.pages[page_num].extract_text()
        links.extend(re.findall(r'https?://\S+', b))
    return links
if __name__ == '__main__':
    folder_path = r'C:\Users\sarth\OneDrive\Desktop\folder'
    all_links = []
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.pdf'):
            pdf_file = os.path.join(folder_path, file_name)
            links = extract_links(pdf_file)
            all_links.extend(links)
    json_string = json.dumps(all_links)
    json_file_path = os.path.join(folder_path, 'output1.json')
    with open(json_file_path, 'w') as json_file:
        json_file.write(json_string)
    print(f'JSON data saved to {json_file_path}')
