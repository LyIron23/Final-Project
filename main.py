from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

import csv


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# Replace 'your_linkedin_url' with the LinkedIn URL you provided
linkedin_url = 'https://www.linkedin.com/jobs/search?keywords=Data%20Analysis&location=Germany&geoId=101282230&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0'

# Open the LinkedIn URL
driver.get(linkedin_url)
time.sleep(20)  # Give the page some time to load (you may need to adjust this based on your internet speed)

# Scroll down to load more jobs (repeat as needed)
driver.find_element(By.XPATH, "//body").send_keys(Keys.END)
time.sleep(20)  # Give the page some time to load more jobs

# Find job names using the specified XPath
job_names = driver.find_elements(By.XPATH, "//ul[@class='col-lg-12 px-0']//span[@class='sr-only']")

# Create a CSV file and write job names to it
csv_file_path = 'job_names.csv'
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['Job Name'])  # Write header row

    for job_name in job_names:
        csv_writer.writerow([job_name.text])

# Close the WebDriver
driver.quit()

print(f'Job names have been written to {csv_file_path}')

