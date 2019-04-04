import urllib
import csv
import datetime

class Etl:
    def __init__(self):
        #URL for the csv data
        self.url = 'https://data.cityofnewyork.us/api/views/43nn-pn8j/rows.csv?accessType=DOWNLOAD'
        self.uncleaned = self.data_dictionary()
        print('data loaded')
        self.data = self.clean_data_iteration(self.uncleaned)
        print('data cleaned')

    #creates dictionary of CSV extracted from URL
    def data_dictionary(self):
        """
        opens and reads csv in self.url

        Returns
        ----------
        the csv in self.url as a list of dictionaries (each row is a dict)
        """
        #opening URL
        response = urllib.urlopen(self.url)
        #importing CSV as series of dictionaries
        my_csv = csv.DictReader(response)
        #changes my_csv to a list of dictionaries
        rows = list(my_csv)
        return rows

    def clean_data_iteration(self, data):
        """
        cleans each row of data for it to match model

        Parameters
        ----------
        data : list of dictionaries
            uncleaned data provided by data_dictionary()

        Returns
        ----------
        cleaned list of dictionaries
        """
        for i, row in enumerate(data):
            #cleaning keys to lowercase with underscore
            data_clean = {k.lower().replace(" ", "_"): v for k,v in row.items()}
            #naming keys for values to be changed to int
            int_cols = ['camis', 'zipcode', 'phone', 'score']
            #naming keys for values to be changed to date
            date_cols = ['inspection_date', 'record_date', 'grade_date']
            #string columns
            string_cols = set(data_clean.keys()) - set(int_cols) - set(date_cols)
            #changing datatypes of columns where necessary
            for col in int_cols:
                try:
                    data_clean[col] = int(data_clean[col])
                except ValueError:
                    data_clean[col] = None
            for col in date_cols:
                try:
                    data_clean[col] = datetime.datetime.strptime(data_clean[col], '%m/%d/%Y').date()
                except ValueError:
                    data_clean[col] = None
            for col in string_cols:
                data_clean[col] = data_clean[col].title()
            data[i] = data_clean
        return data
