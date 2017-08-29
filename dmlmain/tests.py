from django.test import TestCase
#unittest / unittest2
#doctest

class MainViewsTestCase(TestCase):
	def test_homepage(self):
		resp = self.client.get('/')
		self.assertEqual(resp.status_code, 200)

from django.urls import reverse
from .urls import urlpatterns

class UrlsTest(TestCase):

	def test_responses(self):
		for pattern in urlpatterns:
			if hasattr(pattern, "name") and pattern.name:
				response = self.client.get(reverse(pattern.name))
				print(str(pattern) + str(response.status_code))
			else:
				print(str(pattern) + "skipped")
			allowed_codes = [200, 302,]
			""" 200: httpresponse, 302:httpredirect """
			self.assertTrue(response.status_code in allowed_codes)
