import os

import pandas as pd

from etl.common.utils.common import DefaultOutputFolder as dir

folder_files = [file.split(".")[0] for file in os.listdir(dir())]
serialized_df = pd.read_pickle("etl/views/" + "dataset.pkl")

serialized_files = list(serialized_df["id"].unique())

delta = list(set(folder_files) - set(serialized_files))

if delta:
    print("New files to serialize: ", len(delta))
    dfs = []
    for file in folder_files:
        if file in delta:
            df = pd.read_parquet(dir() + file + ".parquet")
            dfs.append(df)

    delta_df = pd.concat(dfs, ignore_index=True)

    new_serialied_df = pd.concat([delta_df, serialized_df], ignore_index=True)

    pd.to_pickle(new_serialied_df, "etl/views/" + "dataset.pkl")
else:
    print("No new files to serialize")