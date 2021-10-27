# Arquivo do recurso da aula 28
# Ojetivo é fazer a conversão de entradas
# https://github.com/luizomf/check-numbers-python/blob/master/chk_numbers.py

import re


def is_float(val):
    if isinstance(val, float):
        return True
    if re.search(r'^-?[0-9]+\.{1}[0-9]+$', val):
        return True

    return False


def is_int(val):
    if isinstance(val, int):
        return True
    if re.search(r'^-?[0-9]+$', val):
        return True
    return False


def is_number(val):
    return is_int(val) or is_float(val)


###########
#  USAGE  #
###########

# Float
# Int

print(is_int('-1010112'))  # True

# Numbers in general (float ou int)
print(is_number('-1010.112'))  # True

# False
print(is_number('123a'))  # Fal
# se
