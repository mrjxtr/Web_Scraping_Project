# Web Scraping Project

## Overview

This project aims to build a web scraping pipeline for extracting data from static websites with pagination based on alphabetical letters (e.g., A, B, C, D). The pipeline is designed to extract data, organize it into a DataFrame, and ensure that it is clean and ready for use at the end of the process. The scripts are written in Python to be easily modifiable, reusable, and maintainable. Additionally, any potentially sensitive data is handled securely to protect privacy and data integrity.

## Technologies Used

The following technologies and libraries are utilized in this project:

- **Python**: The primary programming language used to build the web scraping pipeline.
- **Pandas**: A powerful library for data manipulation, cleaning, and organization, ensuring the scraped data is structured and ready for analysis.
- **Requests**: A user-friendly library to make HTTP requests, allowing us to retrieve web pages for scraping.
- **BeautifulSoup**: A parsing library that helps in navigating and extracting data from HTML and XML files.
- **python-dotenv**: A library to manage environment variables securely, ensuring sensitive data (like API keys or credentials) is kept out of the source code.
- **Cryptography**: A library for secure encryption and decryption of data.

## Project Components

This project consists of the following components:

1. **Web Scraper Script (`scraper.py`)**: A Python script that scrapes data from static websites with alphabetical pagination (e.g., pages A, B, C). It uses libraries like `Requests` to fetch web pages and `BeautifulSoup` to parse and extract data.

2. **Data Cleaning Script (`data_cleaner.py`)**: A Python script that takes the raw scraped data and transforms it into a clean and structured format, utilizing `Pandas` for data manipulation and handling.

3. **Main Script (`main.py`)**: The primary orchestration script that sequentially runs both the web scraper and data cleaning scripts, managing the entire data extraction and preparation pipeline.

4. **Encryption Script (`config.py`)**: A configuration module where the code for encryption and decryption of sensitive data is stored.

5. **Environment File (`.env`)**: A file containing sensitive data like encryption/decryption keys, links to websites used as data source for the scraper. *(Excluded from version control)*

## Project Structure

```txt
Web_Scraping_Project/
│
├── data/
│   ├── raw/                  <- Folder for raw data (Files are encrypted for privacy and security)
│   └── processed/            <- Folder for cleaned data (Files are encrypted for privacy and security)
│
├── docs/                     <- Documentation
│
├── references/
│   └── folder_structure.txt  <- Folder structure
│
├── scripts/
│   ├── utility/              <- Config modules
│   ├── data_cleaner.py       <- Script for data cleaning
│   ├── main.py               <- Main script that orchestrates the scraping and cleaning
│   └── scraper.py            <- Script for web scraping
│
├── .env                      <- Environment file for sensitive data. (Excluded from version control)
├── .gitignore                <- Git ignore file
├── requirements.txt          <- Project requirements
├── LICENCE.txt               <- Open-source license
└── README.md                 <- Project documentation
```

## Usage

1. **Setup**: Ensure all required Python libraries are installed:

   ```bash
   pip install -r requirements.txt
   ```

2. **Create a `.env` file**: Create a `.env` file in the root directory of the project to store encryption/decryption keys, links to websites used as data source for the scraper.

   ```.env
   # Web Scraping Configuration
   BASE_URL=https://www.website/you/want/to/scrape/
   REFERER_URL=https://www.home/page/of/website/ 

   # Encryption/Decryption Key (Use the key generator in `config.py` script)
   ENC_KEY=*******************************************=
   ```

3. **Run the Main Script**: Execute the main script to perform web scraping and data cleaning:

   ```bash
   python scripts/main.py
   ```

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

📝 **Let's Connect!:**
[![LinkedIn](https://img.shields.io/badge/-LinkedIn-0077B5?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mrjxtr)
[![Upwork](https://img.shields.io/badge/-Upwork-6fda44?style=flat-square&logo=upwork&logoColor=white)](https://www.upwork.com/freelancers/~01f2fd0e74a0c5055a?mp_source=share)
[![Facebook](https://img.shields.io/badge/-Facebook-1877F2?style=flat-square&logo=facebook&logoColor=white)](https://www.facebook.com/mrjxtr)
[![Instagram](https://img.shields.io/badge/-Instagram-E4405F?style=flat-square&logo=instagram&logoColor=white)](https://www.instagram.com/mrjxtr)
[![Threads](https://img.shields.io/badge/-Threads-000000?style=flat-square&logo=threads&logoColor=white)](https://www.threads.net/@mrjxtr)
[![Twitter](https://img.shields.io/badge/-Twitter-1DA1F2?style=flat-square&logo=twitter&logoColor=white)](https://twitter.com/mrjxtr)
[![Gmail](https://img.shields.io/badge/-Gmail-D14836?style=flat-square&logo=gmail&logoColor=white)](mailto:youremail@gmail.com)
