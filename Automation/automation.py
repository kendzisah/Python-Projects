from selenium import webdriver

chrome_browser = webdriver.Chrome('./chromedriver')
chrome_browser.maximize_window()
chrome_browser.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')


show_message_button = chrome_browser.find_element_by_class_name('btn-default')
user_buttons = chrome_browser.find_element_by_css_selector(
    '#get-input > .btn-default')
text_input = chrome_browser.find_element('id', 'user-message')
text_input.clear()
text_input.send_keys('I am very exquisite')

show_message_button.click()

output_message = chrome_browser.find_element('id', 'display')

assert 'I am very exquisite' in output_message.text


chrome_browser.close()
