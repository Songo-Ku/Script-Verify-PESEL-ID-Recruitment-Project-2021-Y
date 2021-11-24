import io
import pandas as pd
import gzip
import shutil


# 1.0 save pandas data frame to csv
def save_pd_df_to_csv(df, file_name):
    df.to_csv(file_name, sep='\t', index=False, encoding='utf-8', header=False)


