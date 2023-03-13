import csv
import requests
from bs4 import BeautifulSoup

# Open the CSV file and create a new CSV file
with open('input.csv', 'r', encoding='utf-8') as input_file, \
     open('output.csv', 'w', encoding='utf-8', newline='') as output_file:

    # Creating objects for reading and writing CSV
    reader = csv.reader(input_file)
    writer = csv.writer(output_file)

    # we go through each line in the CSV file
    for row in reader:
        articul = row[0]

        # Forming a query to the search engine
        query = f"{articul} image"
        url = f"https://www.google.com/search?q={query}&tbm=isch"

        # We execute the query and get an HTML page with search results
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # We find a link to the first image in the search results
        image_url = None
        for img in soup.find_all('img'):
            if 'src' in img.attrs:
                image_url = img.attrs['src']
                break

        # Adding the article and the link to the image to the new CSV file
        writer.writerow([articul, image_url])

