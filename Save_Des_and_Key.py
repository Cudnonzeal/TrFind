import pandas as pd

def Save_to_db(url, des_key):
    file_path = 'Descripion_Keywords.csv'  # Path to your .xlsx file
    # Load the Excel file
    df = pd.read_csv(file_path)
    # Check if URL already exists
    if url in df['URL'].values:
        return "URL already in db"
    else:
        # Add the new row
        df.loc[len(df)] = [url, des_key]
        # Save the DataFrame back to Excel (prevent index column from being saved)
        df.to_csv(file_path)
        return df.tail()
