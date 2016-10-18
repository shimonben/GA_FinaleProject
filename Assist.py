import os

import openpyxl
from openpyxl import load_workbook
import Steel

CONST_SEQUENCE_LENGTH = 20

CONST_MAX_THICKNESS = 80
CONST_MAX_WIDTH = 10
CONST_MAX_ZINC_THICKNESS = 80
CONST_MAX_STEEL_GRADE = 10
CONST_MIN_THICKNESS = 20
CONST_MIN_WIDTH = 4
CONST_MIN_ZINC_THICKNESS = 40
CONST_MIN_STEEL_GRADE = 0.1
CONST_GENERATIONS_TO_TEST = 1000


def main():
    file_name = str(CONST_GENERATIONS_TO_TEST) + " runs avg.xlsx"
    print(file_name)



if __name__ == "__main__":
    main()
