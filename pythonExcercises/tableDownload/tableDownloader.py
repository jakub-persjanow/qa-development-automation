import os
import csv
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

# Define CSV file path
csv_directory = "pythonExcercises/tableDownload/"
csv_filename = os.path.join(csv_directory, "dataTables.csv")

# Ensure the directory exists
os.makedirs(csv_directory, exist_ok=True)

# Initialize Selenium WebDriver
driver = webdriver.Chrome()

try:
    # Open the webpage
    driver.get("https://datatables.net")

    # Wait until the table loads
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//table[@id="example"]/tbody')))

    # Find entities dropdown by ID
    select_element = driver.find_element(By.ID, "dt-length-0")

    # create Select object and set it's value to "100"
    select = Select(select_element)
    select.select_by_value("100")

    # Wait until the table reloads
    WebDriverWait(driver, 10).until(lambda d: len(d.find_elements(By.CSS_SELECTOR, "#example tbody tr")) > 10)

    # Get page source after JavaScript execution
    html = driver.page_source

    # Parse HTML with BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")
    table = soup.find("table", {"id": "example"})
    tbody = table.find("tbody") if table else None

    data = []  # List to store extracted data

    if tbody:
        rows = tbody.find_all("tr")
        for row in rows:
            cells = row.find_all("td")
            if len(cells) >= 3:
                Name = cells[0].text.strip()
                Position = cells[1].text.strip()
                Office = cells[2].text.strip()
                Age = cells[3].text.strip()
                Date = cells[4].text.strip()
                Money = cells[5].text.strip()
                data.append([Name, Position, Office, Age, Date, Money])

    # Write data to CSV
    with open(csv_filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Position", "Office", "Age", "Date", "Money"])  # Column headers
        writer.writerows(data)

    print(f"Data successfully saved to {csv_filename}")

finally:
    driver.quit()  # Close the browser