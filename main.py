# Genetic Algorithm testing - created by:
#       Shimon Ben-Alul
#       Hila Fox

import GAutils


def main():
    coils = GAutils.get_coils_from_excel()
    GAutils.testing_the_algorithm(coils)



if __name__ == "__main__": main()
