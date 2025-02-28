# Backlink Checker Tool


## Introduction
The **Backlink Checker Tool** is a web application built using Flask that allows you to check the details of Backlink on a given page. It verifies anchor text, `rel` attributes, and checks whether the Backlink URL exists on the page. You can also upload and download data in Excel format for easy sharing and analysis.

## Features
- Check multiple URLs on a single page.
- Verify if anchor text matches.
- Check for the presence of specific `rel` attributes (e.g., `nofollow`).
- View results in a user-friendly interface.
- Download and upload Backlinks in Excel format.
- Built with Python (Flask) and JavaScript.

## How to Use

### Prerequisites
Before you begin, ensure you have the following installed on your system:
- **Python 3.6+**
- **Pip** (Python's package installer)
- **Node.js** (for running JavaScript features if needed)


### Installation:

1. Install Python dependencies:
   
    ```bash
   pip install Flask==2.2.2 requests==2.28.1 beautifulsoup4==4.11.1 pandas==1.5.2 openpyxl==3.0.10 XlsxWriter==3.0.2 
2. (Optional) Install any required frontend dependencies if needed for additional functionality.

### Running the Application:

1. Start the Flask application:

    ```bash
      python app.py

The application will run locally at http://127.0.0.1:5000/.

## Accessing the Tool:
Once the app is running, you can access the tool through your web browser by navigating to:

    http://127.0.0.1:5000/

This will take you to the main interface where you can add URLs, check their details, and download the results.

## Using the Tool:

1. Enter the Page URL where you want to check the links.
2. Provide the Target URL that should be checked.
3. Enter the Anchor Text you want to verify.
4. (Optional) Specify the expected rel attribute (e.g., nofollow).
5. Click Check URLs to see the results.
6. You can also download the results as an Excel file or upload an Excel file with URLs to check.


## File Structure


- **app.py**: This is the main Python file that runs the Flask server and handles all routes and business logic.
- **index.html**: The HTML template that provides the frontend interface for the user.
- **requirements.txt**: Lists the Python dependencies for the project.
- **templates/**: Contains HTML templates used by Flask for rendering.
- **README.md**: This file that contains all the information about the project.

## Note:
*	 This tool is intended for checking the validity of backlinks on a given page and can be used for SEO purposes, site auditing, or general link verification.
*	The application currently works with URLs provided manually or through Excel uploads.
*	For any issues or feature requests, please open an issue in the Issues section.


## Extended Description

The **Backlink Checker Tool** is designed to make the process of validating and auditing Backlinks on a webpage faster and more efficient. This tool can be especially useful for SEO professionals, website developers, or anyone managing a website who wants to ensure that internal and external links are working correctly and have the appropriate attributes.

### Key Features:
- **Backlink Validation:** The tool checks if the given target URL exists on the page, making it easy to identify broken or outdated links.
- **Anchor Text Verification:** Ensures that the correct anchor text is used for the target URLs, which is crucial for SEO optimization.
- **Rel Attribute Check:** Verifies that the target URL has the correct `rel` attribute (e.g., `nofollow`, `noopener`, etc.) to prevent undesirable link behaviors.
- **Excel Integration:** The tool allows users to import a list of URLs via an Excel file and also export the results into an Excel sheet for easy sharing and reporting.

### Use Cases:
1. **SEO Audits:** Use this tool to verify that your website links are SEO-friendly and correctly implemented.
2. **Content Management:** Ensure that internal links are correctly pointing to valid pages and external links are up-to-date.
3. **Website Migration:** When migrating a website, you can use this tool to ensure that all URLs are redirected correctly and that no broken links remain.
4. **Backlinks Building:** Check if the backlinks are implemented properly and have the correct attributes.

This project is a work-in-progress, and contributions are welcome to make it more feature-rich and robust. If you have any suggestions or

Thank you for using URL Backlink Checker Tool! Happy checking!
