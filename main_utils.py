import random
import datetime
from dateutil.relativedelta import *
from faker import Faker


def verification_correctness_personal_id(personal_id):
    personal_id = str(personal_id)
    if not len(personal_id) == 11 or not str.isdecimal(personal_id):
        return False
    else:
        return True


def calculate_age(personal_id):
    personal_id = str(personal_id)
    if not verification_correctness_personal_id(personal_id):
        return 'Incorrect'
    # split to extract month and evaluate is born under or above 2000
    year = str(personal_id)[:2]
    month = int(str(personal_id)[2:4])
    day = int(str(personal_id)[4:6])
    if month > 20:
        year = int('20' + str(year))
        # then person born after or equal 2000
        month = month - 20
        print(f'year: {year} month: {month}')
        age = relativedelta(datetime.date.today(), datetime.date(year, month, day)).years
    else:
        year = int('19' + str(year))
        # age = datetime.date.today() - datetime.date(year, month, day)

        # age = (datetime.date.today() - datetime.date(year, month, day)) / datetime.timedelta(days=365.2425)
        age = relativedelta(datetime.date.today(), datetime.date(year, month, day)).years
    return age


def calculate_gender(personal_id):
    EVEN_NUMBER = [0, 2, 4, 6, 8]
    personal_id = str(personal_id)
    if not verification_correctness_personal_id(personal_id):
        return 'Incorrect'
    gender = int(personal_id[10:11])
    if gender in EVEN_NUMBER:
        return 'K'
    else:
        return 'M'


def is_adult_calculation(age):
    age = int(age)
    if age >= 18:
        return True
    else:
        return False


def calculate_control_num(ten_first_num_of_personal_id):
    # calculation for that number I got from:
    # https://www.gov.pl/web/gov/czym-jest-numer-pesel?fbclid=IwAR2jC3gDCjWDJiaNejJm2jZNL_37LGtM4OB-viCQDGPnJiQSNEZgwpnWEqc
    # ten_first_num_of_personal_id must be string type
    WEIGTED_NUM = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]


    # calculate each number of 10 first personal ID from weighted numerics from Polish National Office
    num_1 = ten_first_num_of_personal_id[0]
    num_1 = int(num_1) * WEIGTED_NUM[0]
    type(num_1)
    if num_1 > 9:
        num_1 = int(str(num_1)[-1])
    num_2 = ten_first_num_of_personal_id[1]
    num_2 = int(num_2) * WEIGTED_NUM[1]
    if num_2 > 9:
        num_2 = int(str(num_2)[-1])
    num_3 = ten_first_num_of_personal_id[2]
    num_3 = int(num_3) * WEIGTED_NUM[2]
    if num_3 > 9:
        num_3 = int(str(num_3)[-1])
    num_4 = ten_first_num_of_personal_id[3]
    num_4 = int(num_4) * WEIGTED_NUM[3]
    if num_4 > 9:
        num_4 = int(str(num_4)[-1])
    num_5 = ten_first_num_of_personal_id[4]
    num_5 = int(num_5) * WEIGTED_NUM[4]
    if num_5 > 9:
        num_5 = int(str(num_5)[-1])
    num_6 = ten_first_num_of_personal_id[5]
    num_6 = int(num_6) * WEIGTED_NUM[5]
    if num_6 > 9:
        num_6 = int(str(num_6)[-1])
    num_7 = ten_first_num_of_personal_id[6]
    num_7 = int(num_7) * WEIGTED_NUM[6]
    if num_7 > 9:
        num_7 = int(str(num_7)[-1])
    num_8 = ten_first_num_of_personal_id[7]
    num_8 = int(num_8) * WEIGTED_NUM[7]
    if num_8 > 9:
        num_8 = int(str(num_8)[-1])
    num_9 = ten_first_num_of_personal_id[8]
    num_9 = int(num_9) * WEIGTED_NUM[8]
    if num_9 > 9:
        num_9 = int(str(num_9)[-1])
    num_10 = ten_first_num_of_personal_id[9]
    num_10 = int(num_10) * WEIGTED_NUM[9]
    if num_10 > 9:
        num_10 = int(str(num_10)[-1])
    # sum from 10 numbers to prepare calculation of control number substracted from 10
    total_sum_num_of_id = num_1 + num_2 + num_3 + num_4 + num_5 + num_6 + num_7 + num_8 + num_9 + num_10
    control_number = 10 - int(str(total_sum_num_of_id)[-1])
    control_number = int(str(control_number)[-1])
    return control_number


def generator_perosnal_id(n_perosnal_ids):
    list_of_ids = []
    for _ in range(0, n_perosnal_ids):
        # examples of year '93' '03' '01' '50
        # year generator: year trzymam jako string
        year = str(random.randint(0, 9)) + str(random.randint(0, 9))
        # month generator: month trzymam jako string
        if int(year) > int(str(datetime.date.today().year)[2:]):
            # 22
            # year is bigger than current then it must be before 2000 year
            month = random.randint(1, 12)
            if month < 10:
                month = '0' + str(month)
            else:
                month = str(month)
        else:
            # it could be above or below 2000
            is_after2000 = random.randint(0, 1)
            if is_after2000 == 1:
                # it is above 2000
                month = str(random.randint(1, 12) + 20)
            else:
                # it is below 2000
                month = random.randint(1, 12)
                if month < 10:
                    month = '0' + str(month)
                else:
                    month = str(month)

        # day generator trzymamy jako string
        day = random.randint(1, 12)
        if day < 10:
            day = '0' + str(day)
        else:
            day = str(day)
        pppp = str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9))
        created_number_personal_id = year + month + day + pppp
        control_num = calculate_control_num(created_number_personal_id)
        created_number_personal_id = created_number_personal_id + str(control_num)
        print(created_number_personal_id)
        list_of_ids.append(created_number_personal_id)
    return list_of_ids


def generator_first_names(n_names):
    fake = Faker(['pl_PL'])
    list_of_first_names = []
    for _ in range(0, n_names):
        list_of_first_names.append(fake.first_name())
    return list_of_first_names


def generator_last_names(n_names):
    fake = Faker(['pl_PL'])
    list_of_last_names = []
    for _ in range(0, n_names):
        list_of_last_names.append(fake.last_name())
    return list_of_last_names
































