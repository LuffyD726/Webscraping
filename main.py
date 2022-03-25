from bs4 import BeautifulSoup
import requests
import webbrowser



print('name, collateral object')
URL = 'https://en.wikipedia.org/wiki/List_of_animal_names'
response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

# find all the tables on the page
All_tables = soup.findChildren('table')

# find the specific table on the page
my_table = All_tables[2]

# find the body of the table
my_tbody = my_table.find('tbody')

# finds all the rows in the body
rows = my_tbody.find_all('tr')



# loop through all the rows on the body
for row in rows:

    # find every cell
    value = row.find_all('td')

    # strip the data from the cell
    clear_value = [dp.text.strip() for dp in value]
    # check if there is an empty cell (like the first one)
    if len(clear_value) == 0:
        continue
    if clear_value[5] == '?':
        print(clear_value[0])
    else:
        print(clear_value[0] + ', ' + clear_value[5] )

