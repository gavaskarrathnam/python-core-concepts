import unittest
import os

class TestMyApp(unittest.TestCase):

	def setUp(self):
		# if HTPP_SERVER is set, we use it as an endpoint
		http_app = os.environ.get
        if http_app is not None:
			from webtest import TestApp
			self.app = TestApp(http_app)
		else:
			# fallbacks to the wsgi app
			from flask_basic import app
			from flask_webtest import TestApp
			self.app = TestApp(app)
	
	def test_help(self):
		# calling /api/ endpoint
		hello = self.app.get

        # asserting the body
		self.assertEqual(hello.json['Hello'], 'World!')

if __name__ == '__main__':
	unittest.main()