from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time
from django.test import LiveServerTestCase


class PageTest(LiveServerTestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		

	def test_browser_firstvisit(self):
		self.browser.get(self.live_server_url)
		self.assertIn('The Resorts Hub', self.browser.title)

		#Header

		headerText = self.browser.find_element_by_tag_name('h1').text 
		self.assertIn('Digital Resort Reservation', headerText)

		#Fullname

		name = self.browser.find_element_by_id('Fullnamea').text
		self.assertIn('Full Name', name)

		name = self.browser.find_element_by_name('Fullname')
		self.assertEqual(name.get_attribute('placeholder'),'Full Name')

		name = self.browser.find_element_by_name('Fullname').send_keys("Kim Magbanua")
		time.sleep(1)

		#Date of Reservation

		date = self.browser.find_element_by_id('reservea').text
		self.assertIn('Date of Reservation', date)

		date = self.browser.find_element_by_id('reserve').click()

		date = self.browser.find_element_by_id('reserve').send_keys("2021-04-30")
		time.sleep(1)

		#Contact No.

		cont = self.browser.find_element_by_id('contacta').text
		self.assertIn('Contact Number', cont)

		cont = self.browser.find_element_by_id('contact')
		self.assertEqual(cont.get_attribute('placeholder'),'Enter your Contact Number')

		cont = self.browser.find_element_by_id('contact').send_keys("09123456789")
		time.sleep(1)

		#Chosen Resort

		rsrt = self.browser.find_element_by_id('resorte').text
		self.assertIn('Select a Resort', rsrt)

		rsrt = self.browser.find_element_by_id('resort').click()

		rsrt = self.browser.find_element_by_id('resortd').send_keys("Volets Hotel & Resort")
		time.sleep(1)

		
		#Admission

		admis = self.browser.find_element_by_id('entranced').text
		self.assertIn('Admission (Adult)', admis)

		admis = self.browser.find_element_by_id('entrance').click()

		admis = self.browser.find_element_by_id('entranceb').send_keys("Overnight [Adult]")
		time.sleep(1)


		#Quantity1

		quant1 = self.browser.find_element_by_id('admit')
		self.assertEqual(quant1.get_attribute('placeholder'),'Quantity (Max of 30)')

		quant1 = self.browser.find_element_by_id('admit').send_keys("3")
		time.sleep(1)

		submit = self.browser.find_element_by_name('submitbutton').click()	

		Nextpage = self.browser.current_url
		self.assertRegex(Nextpage, '/success')
		self.browser.quit()

	def test_browser_second_visit(self):
		self.browser.get(self.live_server_url)


		name = self.browser.find_element_by_name('Fullname').send_keys("Kim Magbanua")
		time.sleep(1)

		date = self.browser.find_element_by_id('reserve').send_keys("2021-04-30")
		time.sleep(1)

		cont = self.browser.find_element_by_id('contact').send_keys("09123456789")
		time.sleep(1)

		rsrt = self.browser.find_element_by_id('resortd').send_keys("Volets Hotel & Resort")
		time.sleep(1)

		admis = self.browser.find_element_by_id('entrancec').send_keys("Overnight [Adult]")
		time.sleep(1)

		quant1 = self.browser.find_element_by_id('admit').send_keys("3")
		time.sleep(1)

		submit = self.browser.find_element_by_name('submitbutton').click()

# if __name__== '__main__':
# 	unittest.main()																																															