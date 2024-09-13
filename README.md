# Web Scraping Project (ONGOING)

## Overview

This project aims to build a web scraping pipeline for extracting data from static websites that use letters for pagination (e.g., A, B, C, D). The pipeline ensures that the scraped data is clean and ready for use at the end of the process. The scripts are written in Python to be easily modifiable, reusable, and maintainable, with any potentially sensitive data managed securely.

## Technologies Used

The following technologies and libraries are used in this project:

- **Python**: The core programming language for the project.
- **Pandas**: For data manipulation and cleaning.
- **Requests**: To handle HTTP requests.
- **BeautifulSoup**: To parse HTML content and extract data.
- **python-dotenv**: To manage environment variables securely.

## Project Components

This project consists of the following components:

1. **Web Scraper Script (`scraper.py`)**: A Python script designed to scrape data from static websites using letters for pagination.

2. **Data Cleaning Script (`data_cleaner.py`)**: A Python script to transform raw scraped data into a clean, structured format.

3. **Main Script (`main.py`)**: The main orchestrator script that runs both the web scraping and data cleaning scripts in sequence.

## Project Structure

```txt
web_scraping_project/
│
├── data/
│   ├── raw/                  # Folder for raw data (Files are encrypted for privacy and security)
│   └── processed/            # Folder for cleaned data (Files are encrypted for privacy and security)
│
├── docs/                     # Documentation
│
├── references/
│   └── folder_structure.txt  # Folder structure
│
├── scripts/
│   ├── utility/              # Config modules
│   ├── scraper.py            # Script for web scraping
│   ├── data_cleaner.py       # Script for data cleaning
│   └── main.py               # Main script that orchestrates the scraping and cleaning
│
├── .env                      # Environment file for sensitive data like API keys, etc.
├── .gitignore                # Git ignore file
├── requirements.txt          # Project requirements
├── LICENSE.txt               # Open-source license
└── README.md                 # Project documentation
```

## Usage

1. **Setup**: Ensure all required Python libraries are installed:

   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Main Script**: Execute the main script to perform web scraping and data cleaning:

   ```bash
   python scripts/main.py
   ```

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.
