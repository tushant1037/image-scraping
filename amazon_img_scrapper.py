import urllib
import requests
from urllib.request import urlopen

import numpy as np
from bs4 import BeautifulSoup
import re

for i in range(1,100):
	html = urlopen('https://www.amazon.com/s?k=pantry&ref=nb_sb_noss_' + str(i))
	bs = BeautifulSoup(html, 'html.parser')
	images = bs.find_all('img', {'src':re.compile('.jpg')})
	j = 0
	for image in images:
		print(image['src']+'\n')
		l = image['src']
		j = str(j)
		urllib.request.urlretrieve(l, "C:/Users/tushant/Desktop/local_file/"+str(i)+j+"img.jpg")
		j = int(j)
		j = j + 1
