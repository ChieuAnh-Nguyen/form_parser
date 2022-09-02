from cgitb import html
import os
from bs4 import BeautifulSoup


text_file = open('parsethis.html','r')
text = text_file.read()
soup = BeautifulSoup(text).get_text()
print(soup)