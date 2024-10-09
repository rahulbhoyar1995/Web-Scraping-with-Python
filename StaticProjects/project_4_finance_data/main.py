import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.moneycontrol.com/financials/relianceindustries/consolidated-balance-sheetVI/RI'
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the table in the HTML content
    table = soup.find('table', class_='mctable1')

    # Check if the table exists
    if table:
        rows = table.find_all('tr')
        
        # Open a CSV file to write the table data
        with open('financial_data.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            
            for row in rows:
                cells = row.find_all(['td', 'th'])  # Including 'th' to capture header cells
                cell_text = [cell.get_text(strip=True) for cell in cells]
                
                # Write the row to the CSV file
                writer.writerow(cell_text)
    else:
        print("No table found on the page.")
else:
    print(f"Failed to retrieve the URL. Status code: {response.status_code}")
