from django.urls import resolve
from django.test import TestCase
from TRH.views import homepage

class HomePageTest(TestCase):

	def test_mainpage_returns_correct_view(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response,'homepage.html')

	def test_save_POST_request(self):
		response = self.client.post('/',data={'Fullname':'New entry'})
		self.assertIn('New entry', response.content.decode())
		response = self.client.post('/',data={'reserve':'New entry'})
		self.assertIn('New entry', response.content.decode())
		response = self.client.post('/',data={'contact':'New entry'})
		self.assertIn('New entry', response.content.decode())
		response = self.client.post('/',data={'resort':'New entry'})
		self.assertIn('New entry', response.content.decode())
		response = self.client.post('/',data={'admit':'New entry'})
		self.assertIn('New entry', response.content.decode())
		response = self.client.post('/',data={'admitquant':'New entry'})
		self.assertIn('New entry', response.content.decode())

		self.assertTemplateUsed(response,'homepage.html')

	'''def test_mainpage_returns_correct_view(self):
			response = self.client.get('/')
			html = response.content.decode('utf8')
			string_html = render_to_string('homepage.html')
			self.assertEqual(html,string_html)
			self.assertTemplateUsed(response,'homepage.html')

		def test_root_url_resolve_to_mainpage_view(self)
			found = resolve('/')
			self.assertEqual(found.func, Mainpage)

		def test_mainpage_returns_correct_view(self):
			request = HttpRequest()
			response = Mainpage(request)
			html = response.content.decode('utf8')
			string_html = render_to_string('homepage.html')
			self.assertEqual(html, string_html)

		def test.mainpage_returns_correct_view(self):
			request = HttpRequest()
			response = MainPage(request)
			html = response.content.decode('utf8')
			self.assertTrue(html.strip().startswith('<html>'))
			self.assertIn('(<title>Digital Reservation Receipt</title>',html)
			self.assertTrue(html.strip().endswith('</html>'))'''
