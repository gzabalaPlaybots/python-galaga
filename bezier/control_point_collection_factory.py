from .control_point_quartet import ControlPointQuartet
from .control_point_quartet_collection import ControlPointQuartetCollection

class ControlPointCollectionFactory():

    @staticmethod
    def create_collection1():
        control_point_quartet_collection = ControlPointQuartetCollection()

        control_point_quartet_collection.add(ControlPointQuartet(
            713, -15,
            900, 151,
            1088, 650,
            701, 648))

        control_point_quartet_collection.add(ControlPointQuartet(
            501, 648,
            114, 646,
            208, 488,
            235, 343))

        control_point_quartet_collection.add(ControlPointQuartet(
            935, 343,
            962, 198,
            1026, -181,
            1213, -15))

        return control_point_quartet_collection

    @staticmethod
    def create_collection2():
        control_point_quartet_collection = ControlPointQuartetCollection()

        control_point_quartet_collection.add(ControlPointQuartet(
            513, -15,
            430, 11,
            204, 659,
            516, 654))

        control_point_quartet_collection.add(ControlPointQuartet(
            1016, 654,
            1328, 649,
            920, 388,
            1025, 375))

        control_point_quartet_collection.add(ControlPointQuartet(
            525, 375,
            630, 362,
            596, -41,
            513, -15))

        return control_point_quartet_collection

    @staticmethod
    def create_collection3():
        control_point_quartet_collection = ControlPointQuartetCollection()

        control_point_quartet_collection.add(ControlPointQuartet(
            1113, -15,
            965, 16,
            1263, 556,
            1116, 654))

        control_point_quartet_collection.add(ControlPointQuartet(
            516, 654,
            269, 652,
            476, 535,
            528, 393))

        control_point_quartet_collection.add(ControlPointQuartet(
            528, 393,
            480, 251,
            461, 14,
            513, -15))

        return control_point_quartet_collection

    @staticmethod
    def create_collection4():
        control_point_quartet_collection = ControlPointQuartetCollection()

        control_point_quartet_collection.add(ControlPointQuartet(
            1213, -15,
            1030, 11,
            904, 659,
            1216, 654))

        control_point_quartet_collection.add(ControlPointQuartet(
            516, 654,
            528, 649,
            220, 388,
            525, 375))

        control_point_quartet_collection.add(ControlPointQuartet(
            525, 375,
            530, 362,
            396, -41,
            513, -15))

        return control_point_quartet_collection
