from csv_utils import save_pd_df_to_csv
from main_utils import calculate_gender, calculate_age, is_adult_calculation, verification_correctness_personal_id
from chmod_utils import permission_file_changer
import pandas as pd
import stat
import os
import json


COL_NAMES = ['pesel', 'imię', 'nazwisko']
df_pesel = pd.read_csv(
    'pesel.gz', compression='gzip', header=0, sep='\t', quotechar='"', names=COL_NAMES, encoding='utf-8'
)
# -----------------------------------------------------------------------------------------------------------------------
# I point: data processing
print('I point: data processing')
print('--------------------------------------------------------\n')

# -----------------------------------------------------------------------------------------------------------------------

# 1 number of rows
print('number of rows in pesel data frame is: ')
print(len(df_pesel.index))
print('--------------------------------------------------------\n')
# -----------------------------------------------------------------------------------------------------------------------

# 2 all distinct names sorted in alphabetical order
print('all distinct names sorted in alphabetical order')
print(df_pesel['imię'].sort_values().unique())
print('--------------------------------------------------------\n')
# -----------------------------------------------------------------------------------------------------------------------

# 3 all names which do not reapeat in df
# data_frame['name'].value_counts()
print(df_pesel.drop_duplicates(subset=['imię'], keep=False)['imię'].sort_values().to_string())
print('--------------------------------------------------------\n')
# -----------------------------------------------------------------------------------------------------------------------

# 4 print of count unique names
print(df_pesel['imię'].value_counts())
print('--------------------------------------------------------\n')
# -----------------------------------------------------------------------------------------------------------------------

# 5 from pesel gz save into wynik.txt all records for name "Jan"
# I used here contains case false to incluse all gaja big or small letters
print('Created file wynik.txt with record where name was Jan \n')
df_pesel_jan = df_pesel[df_pesel['imię'].isin(['Jan', 'jan'])]
save_pd_df_to_csv(df_pesel_jan, 'wynik.txt')
print('you are here:', os.getcwd())
print('and here you can see you really created wynik.txt file by this script')
print(os.listdir())
print('--------------------------------------------------------\n')
# -----------------------------------------------------------------------------------------------------------------------

# 6 from wynik.txt sort data by personal ID descending way and save into wynik_sorted.txt
COL_NAMES = ['pesel', 'imię', 'nazwisko']
df_pesel_jan = pd.read_csv(
    'wynik.txt', header=0, sep='\t', quotechar='"', names=COL_NAMES, encoding='utf-8'
)
df_pesel_jan_sorted = df_pesel_jan.sort_values(by=['pesel'], axis=0, ascending=False)
save_pd_df_to_csv(df_pesel_jan_sorted, 'wynik_sorted.txt')
print('save to wynik_sorted.txt from wynik.txt sort records by personal id descending way')
print('you are here:', os.getcwd())
print('here you can see you really created wynik_sorted.txt file by this script')
print(os.listdir())
print('--------------------------------------------------------\n')
# -----------------------------------------------------------------------------------------------------------------------

# 7 change options wynik_sorted.txt into only read for all users except of file owner
print('now only owner can read execute and write, others can only read')
permission = (stat.S_IRWXU | stat.S_IRGRP | stat.S_IROTH)
permission_file_changer(path='wynik_sorted.txt', permission=permission)
print('--------------------------------------------------------\n')
# -----------------------------------------------------------------------------------------------------------------------

# I point: data processing
print('II point: programming')
print('--------------------------------------------------------\n')
# -----------------------------------------------------------------------------------------------------------------------

print('From df create json format and json file calles "json_file.txt" ')

list_of_prepared_dicts = {}
for index, row in df_pesel.iterrows():
    print(row['pesel'])
    dict_of_record_df = {
        row['pesel']: {
            "imie": row['imię'],
            "nazwisko": row['nazwisko'],
            "płeć": calculate_gender(row['pesel']),
            "wiek": calculate_age(row['pesel']),
            "czy_dorosły": is_adult_calculation(row['pesel']),
            "poprawny_pesel": verification_correctness_personal_id(row['pesel']),
        },
    }
    list_of_prepared_dicts.update(dict_of_record_df)
deserved_form_of_dicts = dict(baza=list_of_prepared_dicts)
expected_json = json.dumps(deserved_form_of_dicts)
with open('json_file.txt', 'w') as outfile:
    json.dump(expected_json, outfile)

print('you are here:', os.getcwd())
print('here you can see you really created json_file.txt file by this script')
print(os.listdir())
print('--------------------------------------------------------\n')

print(' Script made everything. Program successfully finished working.')
# -----------------------------------------------------------------------------------------------------------------------
