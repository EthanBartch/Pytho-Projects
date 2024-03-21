import requests
from bs4 import BeautifulSoup

url = "https://apclassroom.collegeboard.org/92/assessments/assignments/57113936"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")



tag = doc.find_all("div",{"class": "lrn-assess-content content lrn "})

tag2 = tag.find_all("")
print(tag)