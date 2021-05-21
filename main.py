from bs4 import BeautifulSoup
import requests
import re

# TODO: Get the webpage
response = requests.get(url="https://www.empireonline.com/movies/features/best-movies-2/")
webpage = response.text

# TODO: Parse the webpage
soup = BeautifulSoup(webpage, "html.parser")
site_data = str(soup.find(id="__NEXT_DATA__").contents[0])
start_indexes = [occurrence.start() + 13 for occurrence in re.finditer('"titleText":"', site_data)]

# TODO: Reverse the order of the indexes
for start_index in start_indexes[::-1]:
    end_index = site_data.find('"', start_index)
    title = site_data[start_index:end_index]

    # TODO: Open and write the data into a text file
    try:
        file = open('movies.txt', 'a')
    except FileNotFoundError:
        file = open('movies.txt', 'w')
    finally:
        file.write(f"{title}\n")
        file.close()
