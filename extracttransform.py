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
        response = urllib.urlopen(self.url)
        my_csv = csv.DictReader(response)
        rows = list(my_csv)
        return rows

    def clean_data_iteration(self, data):
        for i, row in enumerate(data):
            #cleaning keys to lowercase with underscore
            data_clean = {k.lower().replace(" ", "_"): v for k,v in row.items()}
            #naming keys for values to be changed to int
            int_cols = ['camis', 'zipcode', 'phone', 'score']
            #naming keys for values to be changed to date
            date_cols = ['inspection_date', 'record_date', 'grade_date']
            #string columns
            string_cols = set(data_clean.keys()) - set(int_cols) - set(date_cols)
            #data_clean = {k:(int(v) if k in int_cols else v) for k,v in data.items()}
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
