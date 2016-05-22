import main


class Steel:
    def __init__(self, thickness, width, zinc_thickness, steel_grade, name):
        # steel_grade is the chemical composition
        # zinc_thickness is the zinc layer thickness
        self.thickness = thickness
        self.width = width
        self.zinc_thickness = zinc_thickness
        self.steel_grade = steel_grade
        self.name = name

    def print_attr(self):
        atr = "Steel id: {:0>-2}, Steel grade: {:0>-2}, zinc thickness: {:07.4f}, Steel width: {:07.4f}, Steel thickness: {:07.4f}". \
            format(self.name, self.steel_grade, self.zinc_thickness, self.width, self.thickness)
        return atr
