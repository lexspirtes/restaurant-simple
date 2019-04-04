import unittest
from extracttransform import Etl

class fake_class:
    def __init__(self):
        self.help = 'hi'


class TestSuite(unittest.TestCase):
    test_etl = Etl()
    def test_url(self):
         self.assertEqual(self.__class__.test_etl.url, 'https://data.cityofnewyork.us/api/views/43nn-pn8j/rows.csv?accessType=DOWNLOAD')

    def test_camis_int(self):
        self.assertEqual(type(self.__class__.test_etl.test_return['camis']), int)

if __name__ == "__main__":
    unittest.main()
