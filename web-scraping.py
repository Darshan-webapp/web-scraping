import requests
from bs4 import BeautifulSoup
import pandas as pd

# Make an HTTP request to the website
url = 'https://customizewatch.en.alibaba.com/productgrouplist-909447158/Men_Watches.html?spm=a2700.galleryofferlist.topad_classic.7.4ef53ee9pZF4hk'
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Extract data from the HTML
data = []

module_product_list = soup.find_all('div', class_='icbu-product-card vertical large product-item')
for item in module_product_list:
    
    product_name = item.find('a', class_='title-link icbu-link-normal').text.strip()
    product_price = item.find('div', class_='price').text.strip()
    data.append([product_name, product_price])

# Create a Pandas DataFrame from the extracted data
df = pd.DataFrame(data, columns=['Product Name', 'Product Price'])

# Save the DataFrame to an Excel file
df.to_excel('scraped_data.xlsx', index=False)
