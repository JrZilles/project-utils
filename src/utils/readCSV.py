import pandas as pd

def read_csv(filePath:str, header:int=1)->pd.DataFrame:
    dataframe = pd.read_csv(filePath, header=header)
    return dataframe