import pandas as pd
import os

from environment import OUT_FOLDER


# read csv
# get prices below threshold

def analysis():
    for subdir, dirs, files in os.walk(OUT_FOLDER):
        for file in files:
            print(os.path.join(subdir, file))

            if '.DS_Store' in file:
                continue

            file_path = str(os.path.join(subdir, file))
            df = pd.read_csv(file_path)
            df.reset_index()

            for index, row in df.iterrows():
                print(row['description'])
                print(row['price'])
