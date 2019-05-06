# from operator import itemgetter
# import re
# from utils import Roman
import pandas as pd

class DataSanitization():

    def __init__(self, file_name):

        # self.sorted_names_weight = []
        # self.renamed = {}

        self.file_name = file_name
        self.results = []

        """
            Implement solution here
        """

        TYPOS_REPLACE = {r'nkon': 'nikon',
                         r'cannon': 'canon',
                         r'cano ': 'canon ',
                         r'r3d': 'red',
                         r'canonc': 'canon',
                         r'canond': 'canon',
                         r'caonon': 'canon',
                         r'cine flex': 'cineflex',
                         r'go pro': 'gopro',
                         r'gopro(\d.*)': r'gopro \1',
                         r'hero(\d)': r'hero \1',
                         }

        INCOMPLETE_REPLACE = {r'^(eos.*)': r'canon \1'}

        ROMAN_NUMBERS_REPLACE = {r'iv': '4',
                                 r'iii': '3',
                                 r'ii': '2',
                                 }

        # Read file
        df = pd.read_csv(file_name, sep="\n", header=None, index_col=None)

        # Normalize camera names, all to lowercase
        df = df[0].str.lower()

        df = df.replace(TYPOS_REPLACE, regex=True)

        df = df.replace(INCOMPLETE_REPLACE, regex=True)

        df = df.replace(ROMAN_NUMBERS_REPLACE, regex=True)

        # First drop of duplicates
        df = df.drop_duplicates()

        # Sort
        df = df.sort_values()

        # remove parenthesis
        df = df.replace(r"\(.*\)", "", regex=True)

        # Replace mk with mark
        df = df.replace(r"mk", "mark", regex=True)

        # Replace mark with mark with spaces to sparate numbers or other chars
        df = df.replace(r"mark", " mark ", regex=True)

        # Replace multiple whitespace to only one
        df = df.replace('\s+', ' ', regex=True)

        # Remove staring and trailing spaces
        df = df.str.strip()

        # 2nd drop of duplicates
        df = df.drop_duplicates()


        # Output temp file
        #df.to_csv("output2.txt", index=False)

        # Save result
        self.results = df.tolist()
