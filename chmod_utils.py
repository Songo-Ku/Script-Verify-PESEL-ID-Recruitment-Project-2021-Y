import os
import stat


# permissions/privileges
# https://www.tutorialspoint.com/python/os_chmod.htm
# and more examples
# https://stackoverflow.com/questions/15607903/python-module-os-chmodfile-664-does-not-change-the-permission-to-rw-rw-r-bu


# specify full path to file or only name file which is in the same file like your python script
# here are examples of possible permision like stat.S_IREAD owner only read
# https://www.tutorialspoint.com/python/os_chmod.htm
# specify like that permission=(stat.S_IREAD | stat.S_IRGRP | stat.S_IROTH) tu wszyscy tylko moga odczytac
# os.chmod(path, stat.S_IRWXU | stat.S_IRGRP | stat.S_IROTH ) tu owner moze wszystko reszta czyta
def permission_file_changer(path, permission):
    os.chmod(path, permission)





