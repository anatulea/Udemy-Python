import unittest
import cap
class TestCap(unittest.TestCase):

	def test_one_word(self):
		text = 'python'
		result = cap.cap_text(text)
		self.assertEqual(result, 'Python')

	def test_multiple_word(self):
		text = 'python is the best'
		result = cap.cap_text(text)
		self.assertEqual(result, 'Python Is The Best')

if __name__ == '__main__':
	unittest.main()