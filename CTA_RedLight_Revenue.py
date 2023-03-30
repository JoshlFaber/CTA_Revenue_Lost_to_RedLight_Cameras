#%%
from bs4 import BeautifulSoup
import requests
import pandas as pd

## The URL is the CTA site that has links to all the 
## CTA expenditures since 2015
url = 'https://rtams.org/dataset/cta-expenditures'
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")

## We make an empty list and fill it will links that end with .csv
## The .csv files are the sperate expenditure reports

links = []
for link in soup.find_all('a'):
    if '.csv' in link.get('href'):
        links.append(link.get('href'))

## We make an empty dictonary, the key is the year and the value is
## the sum of the expenditures from red light camera tickets.
## These values were found in the column vendor name equal to CITY OF CHICAGO DEPT.OF REVENUE-RED LIGHT
## and summing up the values in the column PAYMENT AMOUNT.
## The older expenditure reports were strings so line 34 cleans the info, 
## transforms the strings into integers and outputs the sum

redLight_dict = {}

for i in range(len(links)):
    data_pd = pd.read_csv(links[i])
    redlight = data_pd[data_pd['VENDOR NAME'] == 'CITY OF CHICAGO DEPT.OF REVENUE-RED LIGHT']
    sum_payed = redlight['PAYMENT AMOUNT'].sum()

    if type(sum_payed) == str: ## If values are string values instead of integers
        sum_payed = sum_payed.replace("$","")
        sum_payed = sum_payed.replace(",","")
        sum_payed = sum_payed.strip()
        pay_list = sum_payed.split(" ")
        pay_sum = 0
        for num in pay_list:
            pay_sum = pay_sum + int(num)
        redLight_dict[2022-i] = '$' + str(float(pay_sum))
    else:    
        redLight_dict[2022-i] = '$'+str(sum_payed)

## We make a dataframe from the dictonary          
df = pd.DataFrame(list(redLight_dict.items()), columns = ['Year', 'Revenue Paid to Red Light Cameras'])

## We save the dataFrame as a CSV file 
## (of course we need to save the python file to specify a path)
df.to_csv('CTA Revenue Lost To Redlight Cameras.csv', index=False)

## We print the dataframe to the console
print(df)
# %%
