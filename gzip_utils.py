import os
import gzip
# import stat
# import sys
# import shutil



# 2.0 read csv and save into gz format
# https://docs.python.org/3/library/gzip.html
# https://www.codegrepper.com/code-examples/python/convert+file+to+.gz+in+python  # example
def convert_csv_to_gz(file_path, name_save_f_gz):
    f_in = open(file_path, 'rb')
    f_out = gzip.open(name_save_f_gz, 'wb')
    f_out.writelines(f_in)
    f_out.close()
    f_in.close()


