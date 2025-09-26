import pandas as pd

def parse_data_to_dataframe(data: list):
    df = pd.DataFrame(data)
    # print(df)
    save_to_csv(df)

def save_to_csv(dataframe: pd.DataFrame):
    dataframe.to_csv("data.csv")