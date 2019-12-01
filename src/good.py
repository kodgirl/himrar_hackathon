import numpy as np
import cv2
from selenium import webdriver
import time
import os, platform
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import re
import requests
from tkinter import Tk
from selenium.webdriver.common.keys import Keys

def ret_smiles():
	with open("pars.html", 'r') as fd:
		page = fd.read()
	soup = BeautifulSoup(page, features="html.parser")
	cities = soup.find('chemical:x-mdl-molfile').text
	cit = ""
	for ch in cities:
		if ch == '\\':
			break
		cit += ch
	return(cit)

def my_func(im):
	WINDOW_SIZE = "834, 596"
	kernel = np.ones((2, 2), np.uint8)
	osplat = platform.system()
	chrome_options = Options()
	print(im)
	# chrome_options.add_argument('--disable-gpu')
	# chrome_options.add_argument("--log-level=3")                     
	# chrome_options.add_argument("--headless")
	chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
	# chrome_options.add_argument("--window-size=%s" % (853, 821)) 
	driver = webdriver.Chrome(chrome_options=chrome_options) if osplat == "Windows" else webdriver(os.path.join(os.path.abspath(os.path.dirname(__file__), "chromedriver"), chrome_options=chrome_options))
	img = cv2.imread(im)
	final_wide = 800
	r = float(final_wide) / img.shape[1]
	dim = (final_wide, int(img.shape[0] * r))
	img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	gray = cv2.medianBlur(gray, 3)
	ret, gray = cv2.threshold(gray, 130, 255, 0)
	cv2.imwrite('mol.jpg', gray)
	driver.get('https://cactus.nci.nih.gov/cgi-bin/osra/index.cgi')
	driver.find_element_by_css_selector('[type="file"]').send_keys(os.path.join(os.path.abspath(os.path.dirname(__file__)), "mol.jpg"))
	driver.find_element_by_css_selector('[id="b_upload"]').click()
	time_old = time.time()
	tes_zag = ""
	while tes_zag == "":
		try:
			if (time.time() - time_old > 15):
				print('some error, please try again')
				driver.quit()
				return(0)
			while driver.find_element_by_css_selector('[alt="Chemical Structure"]') is None:
				pass
			if driver.find_element_by_css_selector('[alt="Chemical Structure"]'):
				tes_zag = "yes"
		except:
			pass
	try:
		time.sleep(0.2)
		driver.find_element_by_css_selector('[x="9390"][y = "750"]').click()
		time.sleep(2)
		driver.find_element_by_css_selector('[class="gwt-MenuItem"][id="gwt-uid-9"]').click()
		time.sleep(2.5)
		driver.find_element_by_css_selector('.gwt-TextArea.gwt-TextArea-readonly').send_keys(Keys.CONTROL, "c")
		tk = Tk()
		tk.withdraw()
		with open("pars.html", "w") as fd:
			fd.write(tk.clipboard_get())
		driver.quit()
		return (1)
	except:
		return (0)
my_func("11.jpg")
print(ret_smiles())
