# instaPhotoDownloader
This is python script which will download all photos of your account or any public account.  
Please download the following packages first
1.selenium chrome webdriver
[download instruction]

1) You need to specify the path where your chromedriver is located.
2) Download chromedriver for your desired platform from here. https://sites.google.com/a/chromium.org/chromedriver/downloads
3) Place chromedriver on your system path, or where your code is.
4) If not using a system path, link your chromedriver.exe (For non-Windows users, it's just called chromedriver):
   browser = webdriver.Chrome(executable_path=r"C:\path\to\chromedriver.exe")
   (Set executable_path to the location where your chromedriver is located.)
   If you've placed chromedriver on your System Path, you can shortcut by just doing the following:
   browser = webdriver.Chrome()
5) If you're running on a Unix-based operating system, you may need to update the permissions of chromedriver after downloading it in order to make it executable:
  chmod +x chromedriver

2.install following 

1) beautifulsoup ---> pip install beautifulsoup4
2) urllib ---> pip install urllib3

