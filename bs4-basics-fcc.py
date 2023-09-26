from bs4 import BeautifulSoup

with open('home.html','r') as html_file:
   data= html_file.read()
   soup=BeautifulSoup(data,'lxml')
   tags=soup.find_all('div')
   course_cards=soup.find_all('div',class_='card')
   for course in course_cards:
      course_names = course.h5.text
      # course_desc=course.p.text
      course_cost=course.a.text.split()[-1]
      print(f'{course_names} is for {course_cost}')

      