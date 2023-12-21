from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.by import By
 
usr=input('Enter Email Id:') 
pwd=input('Enter Password:') 
 
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.facebook.com/')
print ("Opened facebook")
sleep(1)
 
username_box = driver.find_element(By.ID, 'email')
username_box.send_keys(usr)
print ("Email Id entered")
sleep(1)
 
password_box = driver.find_element(By.ID, 'pass')
password_box.send_keys(pwd)
print ("Password entered")
 
login_box = driver.find_element(By.ID, 'loginbutton')
login_box.click()
 
print ("Done")
input('Press anything to quit')
driver.quit()
print("Finished")

String1 = 'Welcome to the Geeks World'
print("String with the use of Single Quotes: ")
print(String1)
String1 = "I'm a Geek"
print("\nString with the use of Double Quotes: ")
print(String1)
print(type(String1))
String1 = '''I'm a Geek and I live in a world of "Geeks"'''
print("\nString with the use of Triple Quotes: ")
print(String1)
print(type(String1))
 
String1 = '''Geeks 
            For 
            Life'''
print("\nCreating a multiline String: ")
print(String1)


List = []
print("Initial blank List: ")
print(List)
List = ['GeeksForGeeks']
print("\nList with the use of String: ")
print(List)
List = ["Geeks", "For", "Geeks"]
print("\nList containing multiple values: ")
print(List[0])
print(List[2])
List = [['Geeks', 'For'], ['Geeks']]
print("\nMulti-Dimensional List: ")
print(List)
