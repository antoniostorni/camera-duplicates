# from operator import itemgetter
# import re
# from utils import Roman
import pandas as pd


"""
550d
5d
5d mark 2
5d mark 3
5d mark ii
5d mark iii
5d mk 2
5d mk ii
5d mk iii
5d mk3
5d mk3 raw
5d mkiii
5dmk2
5dmk3
5dmk3 raw
5dmkii
5dmkiii
5mkiii
600d
60d
6d
70
70d
7d
camera eos 7d
cannon 5d mark iii
cannon 7d
cano t2i

r3d = red

"""


class DataSanitization():
    def __init__(self, file_name):
        self.sorted_names_weight = []
        self.renamed = {}
        self.file_name = file_name 

        """
            Implement solution here
        """

        # Read file
        df = pd.read_csv("duplicates.txt", sep="\n", header=None, index_col=None)

        # Normalize camera names, first letter of each word capital
        df = df[0].str.lower()

        # First drop of duplicates
        df = df.drop_duplicates()

        # Sort
        df = df.sort_values()

        # Output temp file
        df.to_csv("output.txt", index=False)