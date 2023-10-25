from flask import Flask, request, Response
import requests
from bs4 import BeautifulSoup
import io
import zipfile
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return handle_post_request()
    return """<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Image Downloader</title>
    <style>
      body {
        font-family: Arial, sans-serif;
        background-color: #f7f8fa;
        height: 100vh;
        display: flex;
        align-items: center;
        justify-content: center;
      }
      form {
        background-color: #fff;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        width: 350px;
        text-align: center;
      }
      label,
      input {
        width: 100%;
        margin-bottom: 10px;
      }
      input[type="submit"] {
        background-color: #007bff;
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
        cursor: pointer;
        transition: background-color 0.2s;
      }
      input[type="submit"]:hover {
        background-color: #0056b3;
      }
    </style>
  </head>
  <body>
    <form action="/" method="post">
      <label for="url">URL:</label>
      <input type="text" id="url" name="url" required />
      <br />
      <input type="submit" value="Download Images as ZIP" />
    </form>
  </body>
</html>
"""

def handle_post_request():
    url = request.form['url']
    links = extract_image_links_from_url(url)

    zip_file = create_zip_file(links)
    return send_zip_file(zip_file)

def create_zip_file(links):
    memory_file = io.BytesIO()
    with zipfile.ZipFile(memory_file, 'w') as zf:
        for i, link in enumerate(links, 1):
            image_data = download_image(link)
            file_ext = os.path.splitext(link)[1] or '.jpg'
            zf.writestr(f'image_{i}{file_ext}', image_data)
    memory_file.seek(0)
    return memory_file

def send_zip_file(zip_file):
    return Response(zip_file, mimetype='application/zip', 
                    headers={'Content-Disposition': 'attachment;filename=images.zip'})

def extract_image_links_from_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    parent_div = soup.find('div', class_='thumb-list')

    img_tags = parent_div.find_all('img')
    src_links = filter_images(img_tags)

    return src_links

def filter_images(img_tags):
    allowed_extensions = ['.jpeg', '.jpg', '.png', '.gif', '.bmp']
    src_links = [img['src'] for img in img_tags 
                 if 'src' in img.attrs 
                 and any(ext in img['src'] for ext in allowed_extensions) 
                 and 'video' not in img['src'].lower()]
    for index, link in enumerate(src_links):
        src_links[index] = src_links[index][:-14]
    return src_links

def download_image(link):
    response = requests.get(link)
    response.raise_for_status()
    return response.content

if __name__ == '__main__':
    app.run(debug=True)

