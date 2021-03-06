import GAutils
import math

CONST_THICKNESS_PENALTY = 0.1
CONST_WIDTH_PENALTY = 0.2
CONST_ZINC_THICKNESS_PENALTY = 0.4
CONST_STEEL_GRADE_PENALTY = 0.3


def calculate_max_penalty():
    """
    This method calculate the maximum penalty possible
    :return: the maximum penalty
    """
    thickness_penalty = (GAutils.CONST_MAX_THICKNESS - GAutils.CONST_MIN_THICKNESS) * CONST_THICKNESS_PENALTY
    width_penalty = (GAutils.CONST_MAX_WIDTH - GAutils.CONST_MIN_WIDTH) * CONST_WIDTH_PENALTY
    zinc_thickness_penalty = (GAutils.CONST_MAX_ZINC_THICKNESS - GAutils.CONST_MIN_ZINC_THICKNESS) * CONST_ZINC_THICKNESS_PENALTY
    steel_grade_penalty = (GAutils.CONST_MAX_STEEL_GRADE - GAutils.CONST_MIN_STEEL_GRADE) * CONST_STEEL_GRADE_PENALTY
    max_penalty = thickness_penalty + width_penalty + zinc_thickness_penalty + steel_grade_penalty
    return max_penalty


class Steel:
    """
    This represent the steel (coil) attributes and behaviour
    """
    def __init__(self, thickness, width, zinc_thickness, steel_grade, id):
        """
        Initializing a coil for the sequencing
        :param thickness: coil thickness
        :param width: coil width
        :param zinc_thickness: coil zinc thickness required
        :param steel_grade: coil steel grade - its composition
        :param id: coil id based on the excel file read
        """
        # steel_grade is the chemical composition
        # zinc_thickness is the zinc layer thickness
        self.thickness = thickness
        self.width = width
        self.zinc_thickness = zinc_thickness
        self.steel_grade = steel_grade
        self.id = id

    def print_attr(self):
        """
        Debug purposes
        :return: String of the full attributes of the coil
        """
        atr = "Steel id: {:0>-2}, Steel grade: {:0>-2}, zinc thickness: {:07.4f}, Steel width: {:07.4f}, Steel thickness: {:07.4f}". \
            format(self.id, self.steel_grade, self.zinc_thickness, self.width, self.thickness)
        return atr

    def calculate_penalty(self, coil2):
        """
        Checks the penalty between two coils transition
        :param coil2: the post coil to check with
        :return: the penalty of the transition between two consecutive coils
        """
        thickness_dif = math.fabs(self.thickness - coil2.thickness)
        width_dif = math.fabs(self.width - coil2.width)
        zinc_thickness_dif = math.fabs(self.zinc_thickness - coil2.zinc_thickness)
        steel_grade_dif = math.fabs(self.steel_grade - coil2.steel_grade)
        penalty = ((thickness_dif/GAutils.CONST_THICK_DIF) * CONST_THICKNESS_PENALTY) + \
                  ((width_dif/GAutils.CONST_WIDTH_DIF) * CONST_WIDTH_PENALTY) + \
                  ((zinc_thickness_dif/GAutils.CONST_ZINC_DIF) * CONST_ZINC_THICKNESS_PENALTY) + \
                  ((steel_grade_dif/GAutils.CONST_STEEL_DIF) * CONST_STEEL_GRADE_PENALTY)
        return penalty


