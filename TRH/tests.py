# from django.urls import resolve
from django.test import TestCase
from django.template.loader import render_to_string

from TRH.views import homepage
from TRH.models import Info

class HomePageTest(TestCase):

	def test_mainpage_returns_correct_view(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response,'homepage.html')

	def html_homepage(self):
		found = resolve('/')
		self.assertEqual(found.func,homepage)
		self.assertTrue(html.strip().startswith('<html>'))
		self.assertTemplateUsed(response,'homepage.html')
		self.assertIn('<title>The Resorts Hub</title>', html)
		self.assertIn('<h1>Digital Resort Reservation</h1>', html)
		self.assertIn('<form class="form" action="" method="POST">', html)
		self.assertIn('<p id="Fullnamea"></p>', html)
		self.assertIn('<input type="text" id="Fullname" name="Fullname" placeholder="Full Name" required/>', html)
		self.assertIn('<p id="reservea">Date of Reservation</p>', html)
		self.assertIn('<input type="date" id="reserve" name="reserve" required/>', html)
		self.assertIn('<p id="contacta">Contact Number</p>', html)
		self.assertIn('<input type="tel" id="contact" name="contact" placeholder="Enter your Contact Number" pattern="[0-9]{11}" required/>', html)
		self.assertIn('<p id="resorte">Select a Resort</p>', html)
		self.assertIn('<select id="resort" name="resort" required>', html)
		self.assertIn('<option id="resorta" value="Tubigan Garden Resort">Tubigan Garden Resort </option>', html)
		self.assertIn('<option id="resortb" value="Saniya Resort & Hotel">Saniya Resort & Hotel</option>', html)
		self.assertIn('<option id="resortc" value="Coco Valley Richnez Waterpark">Coco Valley Richnez Waterpark</option>', html)
		self.assertIn('<option id="resortd" value="Volets Hotel & Resort">Volets Hotel & Resort</option>', html)
		self.assertIn('</select>', html)
		self.assertIn('<br/>', html)
		self.assertIn('<p id="entranced">Admission (Adult)</p>', html)
		self.assertIn('<select id="entrance" name="entrance" required>', html)
		self.assertIn('<option id="entrancea" value="Day [Adult]">Day </option>', html)
		self.assertIn('<option id="entranceb" value="Night [Adult]">Night </option>', html)
		self.assertIn('<option id="entrancec" value="Overnight [Adult]">Overnight</option>', html)
		self.assertIn('<input type="number" id="admit" name="admit" placeholder="Quantity (Max of 30)" min="1" max="30" required/>', html)
		self.assertIn('<input type="submit" name="submitbutton" value="Create a Reservation">', html)
		self.assertIn('</form>',html)
		self.assertTrue(html.strip().endswith('</html>'))


class ORMTest(TestCase):

	def test_saving_info(self):
		Info1 = Info()
		Info1.Fullname = 'Kim Magbanua'
		# Info1.UserId = newUser
		Info1.save()
		Info2 = Info()
		Info2.reserve = '2021-04-30'
		Info2.save()
		Info3 = Info()
		Info3.contact = '09123456789'
		Info3.save()
		Info4 = Info()
		Info4.resort = 'Volets Hotel & Resort'
		Info4.save()
		Info5 = Info()
		Info5.entrance = 'Overnight [Adult]'
		Info5.save()
		Info6 = Info()
		Info6.admit = '3'
		Info6.save()

		saveall = Info.objects.all()
		self.assertEqual(saveall.count(), 6)
		save1 = saveall[0]
		save2 = saveall[1]
		save3 = saveall[2]
		save4 = saveall[3]
		save5 = saveall[4]
		save6 = saveall[5]
		self.assertEqual(Info1.Fullname, 'Kim Magbanua')
		self.assertEqual(Info2.reserve, '2021-04-30')
		self.assertEqual(Info3.contact, '09123456789')
		self.assertEqual(Info4.resort, 'Volets Hotel & Resort')
		self.assertEqual(Info5.entrance, 'Overnight [Adult]')
		self.assertIn(Info6.entrance, '3')


	def test_saving_info2(self):
		Info1 = Info()
		Info1.Fullname = 'Kim Magbanua'
		# Info1.UserId = newUser
		Info1.save()
		Info2 = Info()
		Info2.reserve = '2021-04-30'
		Info2.save()
		Info3 = Info()
		Info3.contact = '09123456789'
		Info3.save()
		Info4 = Info()
		Info4.resort = 'Volets Hotel & Resort'
		Info4.save()
		Info5 = Info()
		Info5.entrance = 'Overnight [Adult]'
		Info5.save()
		Info6 = Info()
		Info6.admit = '3'
		Info6.save()

		saveall = Info.objects.all()
		self.assertEqual(saveall.count(), 6)
		save1 = saveall[0]
		save2 = saveall[1]
		save3 = saveall[2]
		save4 = saveall[3]
		save5 = saveall[4]
		save6 = saveall[5]
		self.assertEqual(Info1.Fullname, 'Kim Magbanua')
		self.assertEqual(Info2.reserve, '2021-04-30')
		self.assertEqual(Info3.contact, '09123456789')
		self.assertEqual(Info4.resort, 'Volets Hotel & Resort')
		self.assertEqual(Info5.entrance, 'Overnight [Adult]')
		self.assertIn(Info6.entrance, '3')



class Views(TestCase):
	def test_displays_info(self):
		Info.objects.create(Fullname='fullname', 
			reserve='2021-04-30', contact='contact',
			entrance='entrance', admit='3')
		response = self.client.get('/app/views.TRH/')



	

# 	# class ORMTest(TestCase)
# 	# 	def test_saving_retrieving_list(self):
# 	# 		admit1 = item()
# 	# 		admit1.text


# # def test_save_POST_request(self):
# 	# 	response = self.client.post('/',data={'Fullname':'Name of user'})
# 	# 	self.assertIn('Name of user', response.content.decode())
# 	# 	response self.client.post('/',data={'reserve':'date of Reservation'})
# 	# 	self.assertIn ('date of Reservation', response.content.decode())
# 	# 	response = self.client.post('/',data={'contact':'contact info'})
# 	# 	self.assertIn('contact info', response.content.decode())
# 	# 	response = self.client.post('/',data={'resort':'chosen resort'})
# 	# 	self.assertIn('chosen resort', response.content.decode())
# 	# 	response = self.client.post('/',data={'entrance':'New entry'})
# 	# 	self.assertIn('New entry', response.content.decode())
# 	# 	response = self.client.post('/',data={'admitquant':'New entry'})
# 	# 	self.assertIn('New entry', response.content.decode())
# 	# 	self.assertTemplateUsed(response,'homepage.html')

# 	'''def test_mainpage_returns_correct_view(self):
# 			response = self.client.get('/')
# 			html = response.content.decode('utf8')
# 			string_html = render_to_string('homepage.html')
# 			self.assertEqual(html,string_html)
# 			self.assertTemplateUsed(response,'homepage.html')

# 		def test_root_url_resolve_to_mainpage_view(self)
# 			found = resolve('/')
# 			self.assertEqual(found.func, Mainpage)

# 		def test_mainpage_returns_correct_view(self):
# 			request = HttpRequest()
# 			response = Mainpage(request)
# 			html = response.content.decode('utf8')
# 			string_html = render_to_string('homepage.html')
# 			self.assertEqual(html, string_html)

# 		def test.mainpage_returns_correct_view(self):
# 			request = HttpRequest()
# 			response = MainPage(request)
# 			html = response.content.decode('utf8')
# 			self.assertTrue(html.strip().startswith('<html>'))
# 			self.assertIn('(<title>Digital Reservation Receipt</title>',html)
# 			self.assertTrue(html.strip().endswith('</html>'))'''
