import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url1 = 'https://www.coursera.org/specializations/deep-learning'
my_url2 = 'https://www.coursera.org/specializations/aml'

uClient = uReq(my_url1)
page_html = uClient.read()
uClient.close()


page_soup = soup(page_html,"html.parser")

containers = page_soup.findAll("section",{"class":"rc-Course bgcolor-white"})
import os
directory = "Coursera - Deep Learning/"
if not os.path.exists(directory):
    os.makedirs(directory)
filename = "Coursera - Deep Learning/dlcourses.csv"
f = open(filename, "w")

headers = "Course Number, Course Name, Upcomming Sessions, Commitment, Subtitles, About the Course\n"
f.write(headers)

for container in containers:
	course_number = container.h3.text
	course_name_class = container.findAll("h2",{"class":"course-name headline-5-text"})
	course_name = course_name_class[0].text.replace(",","|")
	upcoming_session_class = container.findAll("div",{"class":"course-start-date"})
	upcoming_session = upcoming_session_class[0].text[17:]
	commitment_class = container.findAll("dl",{"class":"basic-info-row horizontal-box"})
	commitment = commitment_class[0].text[10:].replace(","," |")
	subtitles_class = container.findAll("dl",{"class":"basic-info-row horizontal-box"})
	try:
		subtitles = subtitles_class[1].text[9:].replace(",","/")
	except:
		commitment = "None"
		subtitles = subtitles_class[0].text[9:].replace(",","/")
	aboutcourse_class = container.findAll("div",{"class":"description-cont"})
	aboutcourse = aboutcourse_class[0].text.replace(",","|").replace("\n"," ")

	print("course number : " + course_number)
	print("course_name : " + course_name)
	print("upcoming_session : " + upcoming_session)
	print("commitment : " + commitment)
	print("subtitles : " + subtitles)
	print("aboutcourse : " + aboutcourse)

	f.write(course_number + "," + course_name + "," + upcoming_session + "," + commitment + "," + subtitles + "," + aboutcourse + "\n")

f.close()




uClient = uReq(my_url2)
page_html = uClient.read()
uClient.close()


page_soup = soup(page_html,"html.parser")

containers = page_soup.findAll("section",{"class":"rc-Course bgcolor-white"})
import os
directory = "Coursera - Advance Machine Learning/"
if not os.path.exists(directory):
    os.makedirs(directory)
filename = "Coursera - Advance Machine Learning/amlcourses.csv"
f = open(filename, "w")

headers = "Course Number, Course Name, Upcomming Sessions, Commitment, Subtitles, About the Course\n"
f.write(headers)

for container in containers:
	course_number = container.h3.text
	course_name_class = container.findAll("h2",{"class":"course-name headline-5-text"})
	course_name = course_name_class[0].text.replace(",","|")
	upcoming_session_class = container.findAll("div",{"class":"course-start-date"})
	upcoming_session = upcoming_session_class[0].text[17:]
	commitment_class = container.findAll("dl",{"class":"basic-info-row horizontal-box"})
	commitment = commitment_class[0].text[10:].replace(","," |")
	subtitles_class = container.findAll("dl",{"class":"basic-info-row horizontal-box"})
	try:
		subtitles = subtitles_class[1].text[9:].replace(",","/")
	except:
		commitment = "None"
		subtitles = subtitles_class[0].text[9:].replace(",","/")
	aboutcourse_class = container.findAll("div",{"class":"description-cont"})
	aboutcourse = aboutcourse_class[0].text.replace(",","|").replace("\n"," ")

	print("course number : " + course_number)
	print("course_name : " + course_name)
	print("upcoming_session : " + upcoming_session)
	print("commitment : " + commitment)
	print("subtitles : " + subtitles)
	print("aboutcourse : " + aboutcourse)

	f.write(course_number + "," + course_name + "," + upcoming_session + "," + commitment + "," + subtitles + "," + aboutcourse + "\n")

f.close()