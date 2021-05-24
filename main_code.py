from selenium import webdriver


driver=webdriver.Chrome(executable_path="D:\Web driver\chromedriver_win32\chromedriver.exe")
driver.maximize_window()
driver.get("https://sponsorship-page-atharva.netlify.app/")

print("Enter the serial number of the operation you want to perform\n")
print('1-> form filling')
print('2-> getting the contact details')
print('3->Navigate to the official website')

tex= input()

if(tex=='1'):
   print("Enter name, contact number, maild_id to be submitted in the form")
   name=input()
   contact_number=input()
   mail_id=input()
   driver.find_element_by_xpath("//*[@id='03']/button[2]").click()
   mail=driver.find_element_by_xpath("//*[@id='mname']")
   driver.execute_script("arguments[0].scrollIntoView();",mail)
   driver.find_element_by_xpath("//*[@id='fname']").send_keys(name)
   driver.find_element_by_xpath("//*[@id='cno']").send_keys(contact_number)
   mail.send_keys(mail_id)

if(tex=='2'):
   info=driver.find_element_by_css_selector("body > div:nth-child(8) > div")
   driver.execute_script("arguments[0].scrollIntoView();", info)
   print(info.text)

if(tex=='3'):
   faq=driver.find_element_by_xpath('//*[@id="03"]/button[1]').click()
   web=driver.find_element_by_xpath('//*[@id="03"]/div[1]/p/a')
   driver.execute_script("arguments[0].scrollIntoView();", web)
   web.click()

