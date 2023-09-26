from bs4 import BeautifulSoup
import requests
import time

def find_job():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=New+Delhi&cboWorkExp1=1').text
    print("Enter unfamiliar skills")
    skill_issue=input(">")
    print(f"Removing {skill_issue}")
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for index,job in enumerate(jobs):
        date = job.find('span', class_='sim-posted').text.strip()
        if "few" in date:
            company = job.find('h3', class_='joblist-comp-name').text.strip().replace("('More Jobs')","")
            skills = job.find('span', class_='srp-skills').text.strip().replace(" ", "")
            more_info=job.header.h2.a['href']
            if (skill_issue.upper() or skill_issue.lower()) not in skills:
                with open(f'posts/{index}.txt') as f:
                    f.write(f"Company: {company}")
                    f.write(f"Skills: {skills}")
                    f.write(f"More info: {more_info}")
                    f.write(" ") 
if __name__ =='__main__':
    while True:
        find_job()
        time_wait=10
        print(f'Waiting {time_wait} minutes......')
        time.sleep(time_wait*60)