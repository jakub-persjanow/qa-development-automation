import os
import csv
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Define CSV file path
csv_directory = "qa-development-automation/resources/data"
csv_filename = os.path.join(csv_directory, "superheroes.csv")

# Ensure the directory exists
os.makedirs(csv_directory, exist_ok=True)

# Initialize Selenium WebDriver
driver = webdriver.Chrome()

try:
    # Open the webpage
    driver.get("https://qaplayground.dev/apps/dynamic-table/")

    # Wait until the table loads
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "tbody")))

    # Get page source after JavaScript execution
    html = driver.page_source

    # Parse HTML with BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")
    tbody = soup.find("tbody")

    data = []  # List to store extracted data

    if tbody:
        rows = tbody.find_all("tr")
        for row in rows:
            cells = row.find_all("td")
            if len(cells) >= 3:
                superhero_name = cells[0].text.strip()
                email = cells[1].text.strip()
                real_name = cells[2].text.strip()
                data.append([superhero_name, email, real_name])

    # Write data to CSV
    with open(csv_filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["superhero_name", "email", "real_name"])  # Column headers
        writer.writerows(data)

    print(f"Data successfully saved to {csv_filename}")

finally:
    driver.quit()  # Close the browser
