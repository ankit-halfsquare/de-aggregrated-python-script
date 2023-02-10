import os
import pandas as pd
from dotenv import load_dotenv
load_dotenv()


def main():
    print("Process Start")
    input_file = os.getenv('input_file')
    df = pd.read_excel(input_file)
    df = df.loc[df.index.repeat(df.Product_Quantity)].reset_index(drop=True)
    df["Product_Quantity"] = "1"
    prefix = 'deaggregrated'
    df.to_excel(f'{prefix}_{input_file}', index=False)
    print("Process End")




if __name__ == '__main__':
    main()