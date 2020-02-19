
class Building:

    """Common base class for all buildings"""

    building_height = 0

    def __init__(self, building_height):
        self.building_height = building_height


building_1 = Building(5)
print(building_1.building_height)
