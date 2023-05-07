# nina scraper - BETA
# 070523 1855

import requests
from bs4 import BeautifulSoup

escargot_url = "https://escargot.chat/download/msn/"

# Make a request to the webpage
response = requests.get(escargot_url)

# Parse the HTML content of the webpage using Beautiful Soup
soup = BeautifulSoup(response.content, 'html.parser')

# Extract the title of the webpage
title = soup.title.string

# Find the <body> tag and extract its text content
body = soup.find('body').text

# Create an empty list to store the href attributes
href_list = []

# Find all the <div> tags with the specified class
div_tags = soup.find_all('div', class_='col-md-3 my-0 py-0 justify-content-md-center')

print(title)

# Loop through each <div> tag
for div in div_tags:
    # Find all the <p> tags inside the current <div> tag
    p_tags = div.find_all('p')
    # Loop through each <p> tag
    for p in p_tags:
        # Find all the <a> tags inside the current <p> tag
        a_tags = p.find_all('a')
        # Loop through each <a> tag and print its href attribute
        for a in a_tags:
            href_list.append(a['href'])


# Create a new list that contains the concatenation of "escargot_url" and every element from href_list with "/"
new_list = [escargot_url + href for href in href_list]

# Print the new list
print(new_list)

# Create a new list that contains the responses from making a GET request to each URL in new_list
response_list = []
for url in new_list:
    # Make a GET request to the current URL using the requests.get() function with stream=True
    responseb = requests.get(url, stream=True)
    # Append the response to the response_list
    response_list.append(responseb)
    # Parse the HTML content of the webpage using Beautiful Soup
    subsoup = BeautifulSoup(responseb.content, 'html.parser')
    ''' Patched installers '''
    print("Patched installers")
    # Find all the <h6> tags with the specified class
    h6_tags = subsoup.find_all('h6', class_='card-subtitle')
    #print(h6_tags)
    # Create an empty list to store the href attributes
    #hrefa_list = []
    # Loop through each <h6> tag with class="card-subtitle"
    for h6 in h6_tags:
    # Find all <strong> tags inside the current <h6> tag
        strong_tags = h6.find_all('strong')
        # Loop through each <strong> tag
        for strong in strong_tags:
            # Find all <a> tags inside the current <strong> tag and print its href attribute
            a_tags = strong.find_all('a')
            for a in a_tags:
                l = a.get('href')
                print("https:" + l)
    ''' Unpatched installers '''
    print("Unpatched installers")
    for link in subsoup.find_all('a'):
        hrefb = link.get('href')
        if hrefb and 'msnp/installer/' in hrefb:
            print("https:" +hrefb)
