from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=New+Delhi&cboWorkExp1=1').text

soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

for job in jobs:
    company_element = job.find('h3', class_='joblist-comp-name')
    skills_element = job.find('span', class_='srp-skills')
    date_element = job.find('span', class_='sim-posted')
    
    if company_element:
        company = company_element.text.strip()
    else:
        company = "Company name not found"

    if skills_element:
        skills = skills_element.text.strip()
    else:
        skills = "Skills not found"

    if date_element:
        date = date_element.text.strip()
    else:
        date = "Date not found"

    print(f'''
    Company Name: {company}
    Skills: {skills}
    Date Posted: {date}
    ''')
