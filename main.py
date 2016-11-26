# Genetic Algorithm testing - created by:
#       Shimon Ben-Alul
#       Hila Fox
import os

import xlsxwriter

import GAutils

CONST_COILS_IN_BATCH = 40
CONST_EXCEL_FILE_NAME_TO_READ = "coils40.xlsx"
CONST_EXCEL_FILE_NAME_TO_WRITE = "output 40 coils and 0.5 thresh.xlsx"


# The user will get the option to choose between priority
# or time, both equals money, so it won't be an issue.

def main():
    if os.path.isfile(CONST_EXCEL_FILE_NAME_TO_READ):
        coils = GAutils.get_coils_from_excel()
        print(GAutils.testing_the_algorithm(coils))
        '''
        lst_1000_penalty = []
        run = []
        sum_of_penalties = 0
        for i in range(1000):
            print(i)
            run.append(i)
            temp = GAutils.testing_the_algorithm(coils)
            lst_1000_penalty.append(temp)
            sum_of_penalties += temp
        workbook = xlsxwriter.Workbook("Penalty improvement.xlsx")
        worksheet = workbook.add_worksheet()
        bold = workbook.add_format({'bold': 1})
        headings = ['Iteration', 'Penalty improvement', '', 'AVG improvement']
        worksheet.write_row('A1', headings, bold)
        worksheet.write_column('A2', run)
        worksheet.write_column('B2', lst_1000_penalty)
        worksheet.write("D2", float(sum_of_penalties/1000))
        '''
    else:
        print("Excel file not found, system shutdown")
        exit()

if __name__ == "__main__":
    main()
