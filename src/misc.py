# price = driver.find_element_by_id("priceblock_ourprice")
# print(price.text)

# search_bar = driver.find_element_by_name("q")
# print(search_bar.get_attribute("placeholder"))

# logo = driver.find_element_by_class_name("python-logo")
# print(logo.size)

# documentation_link = driver.find_elements_by_css_selector(".documentation-widget a")
# print(documentation_link)

# bug_link = driver.find_element_by_xpath('//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link)

# event_times = driver.find_elements_by_css_selector(".event-widget time")
# event_names = driver.find_elements_by_css_selector(".event-widget li a")
# events = {}

# for n in range(len(event_times)):
#     events[n] = {
#         "time": event_times[n].text,
#         "name": event_names[n].text,
#     }


# print(events)

# special_stats = driver.find_element_by_xpath('//*[@id="articlecount"]/a[1]')
# print(special_stats.text)

#article_count = driver.find_element_by_css_selector("#articlecount a")
#article_count.click()


#all_portals = driver.find_element_by_partial_link_text("All portals")
# search = driver.find_element_by_name("search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

# first_name = driver.find_element_by_name("fName")
# first_name.send_keys("testing")
# last_name = driver.find_element_by_name("lName")
# last_name.send_keys("testing")
# email = driver.find_element_by_name("email")
# email.send_keys("testing@test.com")
# sign_up = driver.find_element_by_xpath("/html/body/form/button")
# sign_up.send_keys(Keys.ENTER)
#driver.quit()