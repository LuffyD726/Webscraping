from bs4 import BeautifulSoup
import requests
import webbrowser
import shutil
import urllib.request

print('name, collateral object')

#Request the wikipedia page
URL = 'https://en.wikipedia.org/wiki/List_of_animal_names'
image_url = 'https://www.google.com/search?q='
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
    elif '/' in clear_value[0]:
        clear_value[0] = clear_value[0].replace("/","or")
    elif '(list)' in clear_value[0]:
        clear_value[0] = clear_value[0].replace("(list)","")
    if clear_value[5] == '?':
        print(clear_value[0])
    else:
        #image_url = 'https://en.wikipedia.org/wiki/'
        #full_path = '.tmp/' + clear_value[0] + '.jpg'
        #urllib.request.urlretrieve(image_url + clear_value[0], full_path)
        print(clear_value[0] + ', ' + clear_value[5] )

