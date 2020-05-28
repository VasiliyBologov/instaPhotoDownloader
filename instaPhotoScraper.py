# from BeautifulSoup import bs4
from urllib.request import Request,urlopen,urlretrieve
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import os

WINDOW_SIZE = "1920,1080"
options = Options()  
options.add_argument("--headless")  
options.add_argument("--window-size=%s" % WINDOW_SIZE)

class InstaphotoScrapper:
	def __init__(self,username,password):
		self.username = username
		self.password = password
		self.driver = webdriver.Chrome(chrome_options=options)
		self.fileList = []
		self.l = []

	def login(self):
		if(self.password == ""):
			return 1
		login_url = "https://www.instagram.com/accounts/login/?source=auth_switcher"
		driver = self.driver
		driver.get(login_url)
		time.sleep(2)
		usr_ele = driver.find_element_by_xpath("//input[@name='username']")
		usr_ele.clear()
		usr_ele.send_keys(self.username)
		pass_ele = driver.find_element_by_xpath("//input[@name='password']")
		pass_ele.clear()
		pass_ele.send_keys(self.password)
		pass_ele.send_keys(Keys.RETURN)
		time.sleep(2)
		try:
			error = driver.find_element_by_xpath("//*[@id='slfErrorAlert']")
			return error.text
		except:
			return 1

	def scroll_down(self):
	# Get scroll height.
		time.sleep(2)
		try:
			errorPage = self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/h2")
			return 1
		except:
			last_height = self.driver.execute_script("return document.body.scrollHeight")
			while True:
			# Scroll down to the bottom.
				self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
				html = self.driver.page_source
				soup = BeautifulSoup(html,"html.parser")
				try:
					imgLink = soup.find("article",{"class":"ySN3v"})
					imgLink = imgLink.findAll("div",{"class":"Nnq7C weEfm"})
					# print(imgLink)
					for i in imgLink:
						for j in i.findAll('a'):
							x=j['href']
							if x not in self.l:
								self.l.insert(0,x)
								# print(x+" sucessfully inserted.")
				except Exception as e:
					print(e)
				else:
					pass
				finally:
					pass
					# Wait to load the page.
				time.sleep(2)

				# Calculate new scroll height and compare with last scroll height.
				new_height = self.driver.execute_script("return document.body.scrollHeight")
				if new_height == last_height:
					break
				last_height = new_height
				

	def scrapPhotos(self):
		url_f = "https://www.instagram.com/"+self.username+"/?hl=en"
		self.driver.get(url_f)
		if self.scroll_down() == 1:
			print("username is wrong")

	def createDir(self):
		parent_path = os.getcwd()
		folder = os.path.join(parent_path,self.username)
		if not os.path.exists(folder):
			os.mkdir(folder)
		return folder

	def checkAlredyExistPhotos(self,folder):
		for i in os.listdir(folder):
			self.fileList.append(i.split(".")[0][10:])
		time.sleep(2)

	def downloadPhotos(self,folder):
		os.chdir(folder)
		for x in self.l:
			url = "https://www.instagram.com"+x
			print(url)
			if x[3:-1] not in self.fileList:
				self.driver.get(url)
				r = self.driver.page_source
				soup = BeautifulSoup(r,'html.parser')
				td = soup.find("a",{"class":"c-Yi7"})
				title = td.find("time")['datetime'][:10]+x[3:-1]
				imgg = soup.find("div",{"class":"KL4Bh"})
				fileName = title+".jpg"
				try:
					urllib.request.urlretrieve(imgg.find('img')['src'],fileName)
					print(fileName+" succesfully Download.")
				except Exception as e:
					print(e)
				else:
					pass
				finally:
					print("----------------------------")
		self.driver.quit()

if __name__ == '__main__':
	
	print("If your account is public than password is optional")
	username = input("Enter your username"+'\n')
	k = input("If account is private = [yes/no]")
	if k=="yes":
		password = input("Enter your password"+'\n')
	else:
		password = ""
	if(username):
		insta = InstaphotoScrapper(username,password)
		if(insta.login() == 1):
			folder = insta.createDir()
			insta.checkAlredyExistPhotos(folder)
			insta.scrapPhotos()
			insta.downloadPhotos(folder)

		else:
			print("something went wrong")
	else:
		print("run script again")

