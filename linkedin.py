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
job_names = driver.find_elements(By.XPATH, "//ul[@class='jobs-search__results-list']//span[@class='sr-only']")
job_companies = driver.find_elements(By.XPATH, "//ul[@class='jobs-search__results-list']//a[@class='hidden-nested-link']")

job_locations = driver.find_elements(By.XPATH, "//ul[@class='jobs-search__results-list']//span[@class='job-search-card__location']")

# Create a CSV file and write job names to it
csv_file_path = 'job_names2.csv'
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['Job Name','Company','Location'])  # Write header row

  #  for job_name in job_names:
   #     csv_writer.writerow([job_name.text])

    #for job_location in job_locations:
     #   csv_writer.writerow([job_location.text])

    for job_name, job_company, job_location in zip(job_names, job_companies, job_locations):
        csv_writer.writerow([job_name.text, job_company.text, job_location.text])

# Close the WebDriver
driver.quit()

print(f'Job names have been written to {csv_file_path}')

