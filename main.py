# Genetic Algorithm testing - created by:
#       Shimon Ben-Alul
#       Hila Fox
import os
import GAutils

CONST_COILS_IN_BATCH = 20
CONST_EXCEL_FILE_NAME_TO_READ = "coils.xlsx"
CONST_EXCEL_FILE_NAME_TO_WRITE = "output.xlsx"


# The user will get the option to choose between priority
# or time, both equals money, so it won't be an issue.

def main():
    if os.path.isfile(CONST_EXCEL_FILE_NAME_TO_READ):
        coils = GAutils.get_coils_from_excel()
        GAutils.testing_the_algorithm(coils)
        # GAutils.testing_the_algorithm_total_and_best_improvement(coils)
        # GAutils.testing_the_algorithm_1000_runs(coils)
    else:
        print("Excel file not found, system shutdown")
        exit()


if __name__ == "__main__":
    main()
