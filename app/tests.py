import unittest
from extracttransform import Etl
import datetime

class TestSuite(unittest.TestCase):
    #instance of ETL class
    test_etl = Etl()
    
    #checking that URL in ETL class is correct
    def test_url(self):
         self.assertEqual(self.__class__.test_etl.url, 'https://data.cityofnewyork.us/api/views/43nn-pn8j/rows.csv?accessType=DOWNLOAD')

    #testing dtype for int columns
    def test_int_cols(self):
        for x in self.__class__.test_etl.data:
            self.assertTrue(type(x.get('camis')) == int or type(x.get('camis')) == None)
            self.assertTrue(type(x.get('phone')) == int or type(x.get('phone')) == None)
            self.assertTrue(type(x.get('zipcode')) == int or type(x.get('zipcode')) == None)
            self.assertTrue(type(x.get('score')) == int or type(x.get('score')) == None)

    #testing date col
    def test_date_col(self):
        for x in self.__class__.test_etl.data:
            inspect_date = x.get('inspection_date')
            record_date = x.get('record_date')
            grade_date = x.get('grade_date')
            self.assertTrue(isinstance(inspect_date, datetime.date) or type(inspect_date) == None)
            self.assertTrue(isinstance(record_date, datetime.date) or type(record_date) == None)
            self.assertTrue(isinstance(grade_date, datetime.date) or type(grade_date) == None)

    #make sure no data is lost between cleaning: length of lists
    def test_lengths(self):
        unclean = len(self.__class__.test_etl.uncleaned)
        clean = len(self.__class__.test_etl.data)
        self.assertEqual(unclean, clean)

    #make sure no data is lost between cleaning: length of each dictionary
    def test_dict_lengths(self):
        unclean = self.__class__.test_etl.uncleaned
        clean = self.__class__.test_etl.data
        for i, x in enumerate(unclean):
            self.assertEqual(len(x), len(clean[i]))


if __name__ == "__main__":
    unittest.main()
