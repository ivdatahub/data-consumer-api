import pandas as pd

from etl.common.utils.common import DefaultOutputFolder as dir

class DatasetSerializer:
    def __init__(self, unserialized_files: list) -> None:
        self.files = unserialized_files
        
    def serialize(self):
        serialized_df = pd.read_pickle("etl/views/" + "dataset.pkl")
        print("Serialized Dataframe Before: ", serialized_df.shape[0])
        dfs = []
        for file in self.files:
            df = pd.read_parquet(dir() + file)
            dfs.append(df)

        delta_df = pd.concat(dfs, ignore_index=True)

        new_serialied_df = pd.concat([delta_df, serialized_df], ignore_index=True)

        pd.to_pickle(new_serialied_df, "etl/views/" + "dataset.pkl")
        print("Serialized Dataframe After: ", new_serialied_df.shape[0])
        print("New Registers: ",
              new_serialied_df.shape[0] - serialized_df.shape[0])
