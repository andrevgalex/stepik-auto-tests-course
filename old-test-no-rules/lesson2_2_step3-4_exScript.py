# https://stepik.org/lesson/228249/step/4?unit=200781
# from selenium import webdriver
# browser = webdriver.Chrome()

# browser.execute_script("alert('Robots at work');")
# browser.execute_script("document.title='Script executing';")
# browser.execute_script("document.title='Script executing';alert('Robots at work');")

# https://stepik.org/lesson/228249/step/5?unit=200781
from selenium import webdriver

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
# browser.execute_script("window.scrollBy(0, 10000);")
# button.click()