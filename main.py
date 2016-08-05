# Genetic Algorithm testing - created by:
#       Shimon Ben-Alul
#       Hila Fox
import os

import GAutils


# The user will get the option to choose between priority
# or time, both equals money, so it won't be an issue.

def main():
    if os.path.isfile("coils.xlsx"):
        coils = GAutils.get_coils_from_excel()
        GAutils.testing_the_algorithm(coils)
    else:
        print("Excel file containing the coils not exist, system shutdown")
        exit()


if __name__ == "__main__":
    main()
