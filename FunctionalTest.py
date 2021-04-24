from selenium import webdriver
import unittest

from selenium.webdriver.common.keys import Keys
import time

'''browser = webdriver.Firefox()
browser.get('http://127.0.0.1:8000')'''

class PageTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	'''def tearDown(self):
		self.browser.quit()

	def test_browser_test(self):
		self.browser.get('http://localhost:8000')
		self.assertIn('The Resorts Hub', self.browser.title)
		self.fail('Finish the test!')

	def check_rows_in_listTable(self, row_text):
		table = self.browser.find_element_by_id('listTable')
		rows = table.find_element_by_tag_name('tr')
		self.assertIn(row_text, [row.text for row in rows])'''

	def test_start_list_and_retrieve_it(self):
		self.browser.get('http://localhost:8000')
		self.assertIn('The Resorts Hub', self.browser.title)

		headerText = self.browser.find_element_by_tag_name('h1').text 
		self.assertIn('Digital Reservation Receipt', headerText)

		input1 = self.browser.find_element_by_tag_name('label').text
		self.assertIn('Full Name', input1)
		fname = self.browser.find_element_by_name('Fullname').send_keys("Kim Magbanua")
		time.sleep(2)

		select = self.browser.find_element_by_id('reserve').click()
		time.sleep(1)

		select = self.browser.find_element_by_id('reserve').send_keys("2021-04-30")
		time.sleep(2)

		select = self.browser.find_element_by_id('contact').send_keys("09123456789")
		time.sleep(2)

		select = self.browser.find_element_by_id('resortb').click()
		time.sleep(1)

		select = self.browser.find_element_by_id('entrancec').click()

		select = self.browser.find_element_by_id('admitquant').send_keys("2")
		time.sleep(2)

		select = self.browser.find_element_by_name('submitbutton').click()	
		time.sleep(2)

		table = self.browser.find_element_by_id('listTable')
		rows = table.find_element_by_tag_name('tr')
		'''self.assertIn('Kim Magbanua',[row.text for row in rows])
		self.assertIn('2021-04-08',[row.text for row in rows])'''

if __name__== '__main__':
	unittest.main()																																																	