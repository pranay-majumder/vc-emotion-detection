import numpy as np
import pandas as pd
import os
from sklearn.model_selection import train_test_split
import yaml

## Read the test_size parameter from params.yaml
test_size=yaml.safe_load(open("params.yaml",'r'))['data_ingestion']['test_size']

## Modular programming approach to data ingestion, preprocessing, and saving the data.
def load_data(data_url: str) -> pd.DataFrame:
    try:
        df=pd.read_csv(data_url)
        return df
    except pd.errors.ParserError as e:
        print(f"Error: Failed to parse the CSV file from {data_url}.")
        print(e)
        raise
    except Exception as e:
        print("Error: An unexpected error occurred while loading the data.")
        print(e)
        raise


def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    try:
        df = df.drop(columns=['tweet_id'])

        final_df = df[df['sentiment'].isin(['happiness', 'sadness'])].copy()

        final_df['sentiment'] = final_df['sentiment'].replace({
            'happiness': 1,
            'sadness': 0
        })

        return final_df

    except KeyError as e:
        print(f"Error: Missing column {e} in the dataframe.")
        raise
    except Exception as e:
        print("Error: An unexpected error occurred during preprocessing.")
        print(e)
        raise


def save_data(train_data: pd.DataFrame, test_data: pd.DataFrame, data_path: str) -> None:
    try:
        ## Inside src --> data --> raw --> train.csv and test.csv ---> if we run normaly
        ## But during "dvc run", the path will be ml-pipelines-using-dvc-main/data/raw/train.csv and ml-pipelines-using-dvc-main/data/raw/test.csv
        ## During pipeline execution, it creates the folder relative to the current working directory, not relative to the location of data_ingestion.py.
        data_path = os.path.join(data_path, 'raw')
        ## If the directory already exists, it will not raise an error due to exist_ok=True.
        os.makedirs(data_path, exist_ok=True)

        train_data.to_csv(os.path.join(data_path, "train.csv"), index=False)
        test_data.to_csv(os.path.join(data_path, "test.csv"), index=False)

    except Exception as e:
        print("Error: An unexpected error occurred while saving the data.")
        print(e)
        raise


def main():
    try:

        df = load_data(
            'https://raw.githubusercontent.com/campusx-official/jupyter-masterclass/main/tweet_emotions.csv'
        )

        final_df = preprocess_data(df)

        train_data, test_data = train_test_split(
            final_df,
            test_size=test_size,
            random_state=42
        )

        save_data(train_data, test_data, 'data')

        print("Data ingestion completed successfully.")

    except Exception as e:
        print(f"Error: {e}")
        print("Failed to complete the data ingestion process.")


if __name__ == '__main__':
    main()