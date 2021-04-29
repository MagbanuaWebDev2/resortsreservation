from django.test import TestCase
from django.template.loader import render_to_string
from TRH.views import homepage
from TRH.models import Info,User

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


class ORMTest(TestCase):

	def test_saving_info(self):
		Info1 = Info()
		Info1.Fullname = 'Kim Magbanua'
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

	def test_redirects(self):
		Fullname = Info.objects.get(Fullname="Kim Magbanua")
		reserve = Info.objects.get(reserve="2021-04-30")
		contact = Info.objects.get(contact="09123456789")
		resort = Info.objects.get(resort="Volets Hotel & Resort")
		entrance = Info.objects.get(entrance="Overnight [Adult]")
		admit = Info.objects.get(admit="3")

		response = self.client.post('/success')
		self.assertRedirects(response, '/success')

