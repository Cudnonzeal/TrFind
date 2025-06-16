import pandas as pd


def Save_to_db(url: str, des_key: str):
  file_path = 'Description_Keywords.xlsx'  # Path to your .xlsx file
  df = pd.read_excel(file_path)
  if url in df['URL'].values:
    print("URL already in db")
    return
  else:
    df.loc[len(df)] = [url, des_key]
    df.to_excel(file_path)
    print("URL and Des_Key added")
