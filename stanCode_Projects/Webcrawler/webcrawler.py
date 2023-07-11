"""
File: webcrawler.py
Name: 
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male number: 10895302
Female number: 7942376
---------------------------
2000s
Male number: 12976700
Female number: 9208284
---------------------------
1990s
Male number: 14145953
Female number: 10644323
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        # soup = BeautifulSoup(html)   # 會有 warning
        soup = BeautifulSoup(html, features="lxml")  # Explicitly specify the parser

        # ----- Write your code below this line ----- #
        # Find all the tables with the name data
        tables = soup.find_all('table', class_='t-stripe')

        # Initialize variables to keep track of total counts
        male_total = 0
        female_total = 0

        # Iterate over each table
        for table in tables:
            tbody = table.find('tbody')  # Find the <tbody> element

            # Find all the rows within the <tbody> element
            rows = tbody.find_all('tr')

            # Find each element (rank, male_count, female_count)
            for row in rows:

                #  Skip unwanted rows (at the end)
                if row.find('td', colspan="4"):
                    continue

                # Find rank, male_count, female_count for each row
                rank = row.find_all('td')[0].get_text()
                male_count = row.find_all('td')[2].get_text().replace(',', '')
                female_count = row.find_all('td')[4].get_text().replace(',', '')

                # Find rank within 200 and calculate the sum
                if int(rank) <= 200:
                    male_total += int(male_count)
                    female_total += int(female_count)

        print(f"Male number: {male_total}")
        print(f"Female number: {female_total}")


if __name__ == '__main__':
    main()
