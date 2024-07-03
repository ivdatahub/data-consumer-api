import pandas as pd

from etl.common.utils.common import DefaultOutputFolder as DefaultFolder


class DatasetSerializer:
    @staticmethod
    def serialize(files):
        serialized_df = pd.read_pickle("etl/views/dataset.pkl")
        print("Total rows before execution: ", serialized_df.shape[0])
        dfs = []
        for file in files:
            df = pd.read_parquet(DefaultFolder() + file)
            dfs.append(df)

        delta_df = pd.concat(dfs, ignore_index=True)

        new_df = pd.concat([delta_df, serialized_df], ignore_index=True)

        pd.to_pickle(new_df, "etl/views/dataset.pkl")
        print("Total rows after execution:: ", new_df.shape[0])
        print("New rows added: ", new_df.shape[0] - serialized_df.shape[0])
