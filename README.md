# Image Downloader App

This repository contains the code for a web application designed to download images from a specified URL and deliver them as a ZIP file to the user. This app is implemented in both Flask (Python) and Node.js (JavaScript). Below you'll find details on the application's functionality, installation, and usage for both versions.

**Live Demo:** A live demo is available at [https://ais.mendescr.com/alibaba-image-scraper/](https://ais.mendescr.com/alibaba-image-scraper/)

## Features

- **Web Interface:** Simple and user-friendly web form where users can submit a URL.
- **Image Download:** Downloads all images from the specified URL and packages them into a ZIP file.
- **Image Filtering:** Filters and downloads only images with certain file extensions, ensuring no irrelevant content is fetched.

## Installation

### Flask Version

To set up and run the Flask application, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/verifizieren/alibaba_image_scraper.git
   cd alibaba_image_scraper
   ```

2. **Set up a virtual environment (optional but recommended):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**
   ```bash
   pip install flask requests beautifulsoup4
   ```

4. **Run the application:**
   ```bash
   python app.py
   ```

### Node.js Version

To set up and run the Node.js application, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/verifizieren/alibaba_image_scraper.git
   cd alibaba_image_scraper
   ```

2. **Navigate to the Node.js project directory:**
   ```bash
   cd nodejs_version
   ```

3. **Install the required packages:**
   ```bash
   npm install
   ```

4. **Run the application:**
   ```bash
   node src/app.js
   ```

## Usage

### Flask Version

1. **Access the Web Interface:**
   - Open your browser and navigate to `http://127.0.0.1:5000/`.
   - You should see a form asking for a URL.

2. **Enter a URL and Download Images:**
   - Enter the URL of a webpage you want to extract images from in the provided text box.
   - Click the "Download Images as ZIP" button.
   - The images will be downloaded, zipped, and the ZIP file will be automatically downloaded to your computer.

### Node.js Version

1. **Access the Web Interface:**
   - Open your browser and navigate to `http://localhost:3000/`.
   - You should see a form asking for a URL.

2. **Enter a URL and Download Images:**
   - Enter the URL of a webpage you want to extract images from in the provided text box.
   - Click the "Download Images as ZIP" button.
   - The images will be downloaded, zipped, and the ZIP file will be automatically downloaded to your computer.

## Code Overview

### Flask Version

- **`index()`**: Handles the main route ('/'). Displays the HTML form on GET requests and processes the form data on POST requests.
- **`handle_post_request()`**: Processes the form data from the POST request, extracts image links from the provided URL, and initiates the ZIP download.
- **`create_zip_file(links)`**: Takes image links, downloads the images, and packages them into a ZIP file.
- **`send_zip_file(zip_file)`**: Sends the ZIP file to the client.
- **`extract_image_links_from_url(url)`**: Fetches the content of the given URL, parses it for image links, and filters them based on allowed extensions.
- **`filter_images(img_tags)`**: Filters out image links based on certain criteria to ensure only valid image files are downloaded.
- **`download_image(link)`**: Downloads an image from a given link.

### Node.js Version

- **`app.get('/')`**: Handles the main route ('/'). Displays the HTML form on GET requests.
- **`app.post('/')`**: Processes the form data from the POST request, extracts image links from the provided URL, and initiates the ZIP download.
- **`extractImageLinksFromUrl(url)`**: Fetches the content of the given URL, parses it for image links, and filters them based on allowed extensions.
- **`createZipStream(links)`**: Takes image links, downloads the images, and packages them into a ZIP file stream.
- **`download_image(link)`**: Downloads an image from a given link.

## Contact

For questions or issues, please open an issue on the GitHub repository page.

## GitHub Repository

For more details and to access the code, visit the [GitHub repository](https://github.com/verifizieren/alibaba_image_scraper).
