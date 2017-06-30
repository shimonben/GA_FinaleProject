# Genetic Algorithm testing - created by:
#       Shimon Ben-Alul
#       Hila Fox
import os

import xlsxwriter

import GAutils


CONST_EXCEL_FILE_NAME_TO_READ = "coils40.xlsx"



def main():
    """
    This is the main method that runs the algorithm and provides the excel
    :return: NONE
    """
    if os.path.isfile(CONST_EXCEL_FILE_NAME_TO_READ):
        coils = GAutils.get_coils_from_excel()
        improvements_values = []
        for i in range(20):
            improvements_values.append(GAutils.testing_the_algorithm(coils, i))
        temp = str(GAutils.CONST_EXCEL_FILE_NAME_TO_WRITE).split("\\")
        temp = str(temp[7]) + str(improvements_values.index(max(improvements_values))) + ".xlsx"
        print("The best improvement is in file: " + temp)
    else:
        print("Excel file not found, system shutdown")
        exit()

if __name__ == "__main__":
    main()
