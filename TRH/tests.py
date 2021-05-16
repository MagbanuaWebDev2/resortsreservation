from django.test import TestCase
from django.template.loader import render_to_string
from TRH.views import homepage
from TRH.models import Info,User
from django.urls import resolve


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
		self.assertIn('<h1 style="font-family: Ubuntu, sans-serif; text-align:center; margin-top: 30px;">Digital Resort Reservation</h1>', html)
		self.assertIn('<form style="font-family: Ubuntu, sans-serif; text-align: center; padding-top: 10px; margin-left: 480px; width:400px; border-radius: 10px; box-shadow: 0 2px 8px 0 gray; height:500px;" class="form" action="" method="POST">', html)
		self.assertIn('<p id="Fullnamea" style="font-weight:bold;">Full Name</p>', html)
		self.assertIn('<input type="text" id="Fullname" name="Fullname" placeholder="Full Name" required/>', html)
		self.assertIn('<p id="reservea" style="font-weight:bold;">Date of Reservation</p>', html)
		self.assertIn('<input type="date" id="reserve" name="reserve" required/>', html)
		self.assertIn('<p id="contacta" style="font-weight:bold;">Contact Number</p>', html)
		self.assertIn('<input type="tel" id="contact" name="contact" placeholder="Enter your Contact Number" pattern="[0-9]{11}" required/>', html)
		self.assertIn('<p id="resorte" style="font-weight:bold;">Select a Resort</p>', html)
		self.assertIn('<select id="resort" name="resort" required>', html)
		self.assertIn('<option id="resorta" value="Tubigan Garden Resort">Tubigan Garden Resort </option>', html)
		self.assertIn('<option id="resortb" value="Saniya Resort & Hotel">Saniya Resort & Hotel</option>', html)
		self.assertIn('<option id="resortc" value="Coco Valley Richnez Waterpark">Coco Valley Richnez Waterpark</option>', html)
		self.assertIn('<option id="resortd" value="Volets Hotel & Resort">Volets Hotel & Resort</option>', html)
		self.assertIn('</select>', html)
		self.assertIn('<p id="entranced" style="font-weight:bold;">Admission (Adult)</p>', html)
		self.assertIn('<select id="entrance" name="entrance" required>', html)
		self.assertIn('<option id="entrancea" value="Day [Adult]">Day </option>', html)
		self.assertIn('<option id="entranceb" value="Night [Adult]">Night </option>', html)
		self.assertIn('<option id="entrancec" value="Overnight [Adult]">Overnight</option>', html)
		self.assertIn('<input type="number" id="admit" name="admit" placeholder="Quantity (Max of 30)" min="1" max="30" required/>', html)
		self.assertIn('<input type="submit" name="submitbutton" value="Create a Reservation">', html)
		self.assertIn('<br/>', html)
		self.assertIn('</form>',html)
		self.assertTrue(html.strip().endswith('</html>'))

class ListViewTest(TestCase):

	def test_uses_main_template(self):
		visitor = User.objects.create()
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'homepage.html')
	def test_uses_next_template(self):
		response = self.client.get('/success')
		self.assertTemplateUsed(response, 'receipt.html')
	def test_displays_all_info(self):
		visitor = User.objects.create()
		Fullname = Info.objects.create(Fullname='Fullname')
		reserve = Info.objects.create(reserve='2021-04-30')
		contact = Info.objects.create(contact='contact')
		resort = Info.objects.create(resort='resort')
		entrance = Info.objects.create(entrance='entrance')
		admit = Info.objects.create(admit='3')
		response = self.client.get('/')
		self.assertIn('Fullname', response.content.decode())
		self.assertIn('reserve', response.content.decode())
		self.assertIn('contact', response.content.decode())
		self.assertIn('resort', response.content.decode())
		self.assertIn('entrance', response.content.decode())
		self.assertIn('admit', response.content.decode())
		Fullname = Info.objects.get(Fullname='Fullname')
		reserve = Info.objects.get(reserve='2021-04-30')
		contact = Info.objects.get(contact='contact')
		resort = Info.objects.get(resort='resort')
		entrance = Info.objects.get(entrance='entrance')
		admit = Info.objects.get(admit='3')
		self.assertEqual(Info.objects.count(), 6)


class Models(TestCase):
	def confirm(self,
		Fullname="test1",
		reserve="test2",
		contact="test3",
		resort="test4",
		entrance="test5",
		admit="test6"):

		return User.objects.create()
		return Info.objects.create(
			Fullname="Fullname",
			reserve="reserve",
			contact="contact",
			resort="resort",
			entrance="entrance",
			admit="admit", )

	def test_generated(self):
		new = self.confirm()
		self.assertTrue(isinstance(new, User))
		self.assertFalse(isinstance(new, Info))

class ORMTest(TestCase):

	def test_saving_info(self):

		info_= Info()
		info_.save()

		Info1 = Info()
		Info1.Fullname = 'Kim Magbanua'
		Info1.info_ = info_
		Info1.save()
		Info2 = Info()
		Info2.reserve = '2021-04-30'
		Info2.info_ = info_
		Info2.save()
		Info3 = Info()
		Info3.contact = '09123456789'
		Info3.info_ = info_
		Info3.save()
		Info4 = Info()
		Info4.resort = 'Volets Hotel & Resort'
		Info4.info_ = info_
		Info4.save()
		Info5 = Info()
		Info5.entrance = 'Overnight [Adult]'
		Info5.info_ = info_
		Info5.save()
		Info6 = Info()
		Info6.admit = '3'
		Info6.info_ = info_
		Info6.save()

		saveall = Info.objects.all()
		self.assertEqual(saveall.count(), 7)
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

		info_= Info()
		info_.save()

		Info1 = Info()
		Info1.Fullname = 'Kim Magbanua'
		Info1.info_ = info_
		Info1.save()
		Info2 = Info()
		Info2.reserve = '2021-04-30'
		Info2.info_ = info_
		Info2.save()
		Info3 = Info()
		Info3.contact = '09123456789'
		Info3.info_ = info_
		Info3.save()
		Info4 = Info()
		Info4.resort = 'Volets Hotel & Resort'
		Info4.info_ = info_
		Info4.save()
		Info5 = Info()
		Info5.entrance = 'Overnight [Adult]'
		Info5.info_ = info_
		Info5.save()
		Info6 = Info()
		Info6.admit = '3'
		Info6.info_ = info_
		Info6.save()

		saveall = Info.objects.all()
		self.assertEqual(saveall.count(), 7)
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
		self.assertIn(Info6.admit, '3')


class Views(TestCase):
	def setUp(self):
		Fullname = Info.objects.create()
		reserve = Info.objects.create()
		contact = Info.objects.create()
		resort = Info.objects.create()
		entrance = Info.objects.create()
		admit = Info.objects.create()

		Info.objects.create(
			Fullname = 'Kim Magbanua',
			reserve = '2021-04-30',
			contact = '09123456789',
			resort = 'Volets Hotel & Resort',
			entrance = 'Overnight [Adult]',
			admit = '3',
			)
		self.client.post('/success')

		self.assertEqual(Info.objects.count(), 7)
























	# def test_redirect_view(self):
	# 	Fullname = Info.objects.get(Fullname="Kim Magbanua")
	# 	reserve = Info.objects.get(reserve="2021-04-30")
	# 	contact = Info.objects.get(contact="Kim Magbanua")
	# 	resort = Info.objects.get(resort="2021-04-30")
	# 	entrance = Info.objects.get(entrance="Kim Magbanua")
	# 	admit = Info.objects.get(admit="2021-04-30")

	# 	response = self.client.post('/success')
	# 	self.assertRedirects(response,'/success')
