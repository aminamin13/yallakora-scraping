<h1>Yalla Kora Website Scraping using Python</h1>

<h1 align="center">
  <img src="https://github.com/aminamin13/yallakora-scraping/blob/main/Screenshot%202024-09-22%20001638.png">
</h1>

This Python project focuses on web scraping the sports website YallaKora.com to extract match results for a specific day. The primary goal is to gather comprehensive data about games played on the selected date, including the teams involved, match dates, and final results. This information can be utilized for sports analytics, reporting, or personal tracking of game outcomes.

**Objectives**
* **Data Extraction:** Develop a script that efficiently scrapes match results from YallaKora.com for a specified date.
* **Data Organization:** Format the extracted data into a structured format, making it easy to analyze and report.
* **Output Generation:** Save the scraped data into a CSV or Excel file for further analysis.

**Key Features**
* **Date Selection:** Allow users to specify a date for which they want to retrieve match results.
* **Automated Scraping:** Use Python libraries such as BeautifulSoup and Requests to automate the scraping process, ensuring that the script can run with minimal manual intervention.
* **Data Integrity:** Implement error handling to manage unexpected changes in the website structure or connectivity issues.
* **Flexible Output:** Provide options to save the results in different formats (CSV, Excel) for user convenience.
  
**Technical Details**
**Libraries Used:**
* requests for sending HTTP requests to YallaKora.com.
* BeautifulSoup for parsing HTML content and extracting relevant data.
* pandas for organizing and saving the data into structured formats.
  
**Data Fields Extracted:**
* Team names
* Match date and time
* Final results (scores)

**Usage**
To use the script, simply input the desired date in the specified format. The script will fetch and compile all relevant match results from YallaKora.com, saving the data to the chosen output format.

This project not only showcases web scraping techniques but also emphasizes the importance of data collection in sports analytics, making it a valuable tool for fans and analysts alike.
