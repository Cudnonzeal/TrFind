import pandas as pd

def Save_to_db(url: str, des_key: str):
    file_path = 'Descripion_Keywords.xlsx'  # Path to your .xlsx file
    # Load the Excel file
    df = pd.read_excel(file_path)
    # Check if URL already exists
    if url in df['URL'].values:
        print("URL already in db")
        return
    else:
        # Add the new row
        df.loc[len(df)] = [url, des_key]
        # Save the DataFrame back to Excel (prevent index column from being saved)
        df.to_excel(file_path, index=False)
        print("URL and Des_Key added")
