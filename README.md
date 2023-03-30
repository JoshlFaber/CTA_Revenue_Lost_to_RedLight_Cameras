# CTA_Revenue_Lost_to_RedLight_Cameras
Python script that leverages BS4 to scrape each years CTA expenditure reports, leverages Pandas to locate revenue lost to red-light cameras in each report, sum the values, organize these values by year and place the results into a DataFrame.

This script leverages BeatifulSoup, requests and pandas. 

The CTA expenditure reports are linked to by year and whose links can be found on a single url 'https://rtams.org/dataset/cta-expenditures'.

We leverage BeautifulSoup to locate the links that link to the CSV files that contain the expenditure reports.

We leverage pandas to locate the revenue paid to red-light cameras and sum these values together.

We organize the values of revenue lost to red-light cameras per year (2022 - 2015) in a DataFrame and export the DataFrame as a CSV file.
