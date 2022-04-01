from bs4 import BeautifulSoup
import requests
import webbrowser


#open the html file
f=open("Output.html", "w", encoding='utf-8')


start ='''
<html>
<body><h2> Name, Collateral adjective <h2>'''


#write the start of the html file
f.write(start)

print('Name, Collateral adjective')

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

# loop through all the rows in the body
for row in rows:

    # find every cell
    value = row.find_all('td')
    
    # strip the data from the cell
    clear_value = [dp.get_text(strip=True, separator=' ')  for dp in value]

    # check if there is an empty cell (like the first one)
    if len(clear_value) == 0 :
        continue
    elif '/' in clear_value[0]:
        clear_value[0] = clear_value[0].replace("/"," or ")
    elif '(list)' in clear_value[0]:
        clear_value[0] = clear_value[0].replace("(list)","")
        
    #remove the empty colleteral adjactive cells
    if clear_value[5] == '?':
        print(clear_value[0])   
    else:
        Output = clear_value[0] + ', ' + clear_value[5] 
        add_names = '''
        <h3>'''+str(Output) + ''' <h3>'''

        #add every name and collateral adjactive to the html file
        f.write(add_names)
        print(Output)

end = '''<body>
</html>
'''

f.write(end)
f.close

webbrowser.open_new_tab("Output.html")


