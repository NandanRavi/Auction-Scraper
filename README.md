# Auction-Scrapper
This Python script is designed to scrape auction data from a specific website, parse the information, and store it in a CSV file. It utilizes the requests library for web scraping and BeautifulSoup for parsing HTML.

# Table of Contents

## [Getting Started](#section-1)
<a id="section-1"></a>
###  [Prerequisites 1.1](#subsection-1-1)
<a id="subsection-1-1"></a>
### [Installation 1.2](#subsection-1-2)
<a id="subsection-1-2"></a>
## [Usage](#section-2)
<a id="section-2"></a>
## [Script Explanation](#section-2)
<a id="section-2"></a>
## [Contributing](#section-2)
<a id="section-2"></a>


# Getting Started
## Prerequisites
To run this script, you need the following dependencies installed:

	'requests'

	'BeautifulSoup'

You can install these dependencies using pip:

	'pip install requests'

 	'pip install beautifulsoup4'


# Installation
Clone the repository to your local machine:

	git clone https://github.com/yourusername/auction-scraper.git

	cd auction-scraper

# Usage

The script is designed to scrape auction data from a specific URL. To use it, follow these steps:

1. Modify the URL in the 'scrape_web' method to point to the auction page you want to scrape:

        URL = requests.get("https://www.phillips.com/auctions/auction/UK010122")

  1. Run the script using the instructions provided in the "Installation" section.

  2. The scraped data will be stored in a CSV file named main.csv.


# Script Explanation


The script works as follows:
  1. It fetches the HTML content of the auction page using the requests library.

  2. It parses the HTML content with BeautifulSoup to extract relevant information.

  3. It collects data for each auction item, including item ID, name, and link to the item details page.

  4. For each item, it scrapes additional information by following the item's link and stores this data in a dictionary.

  5. Finally, it appends the scraped data to a CSV file named main.csv.


# Contributing

If you'd like to contribute to this project, please open an issue or submit a pull request. We welcome improvements and bug fixes.

