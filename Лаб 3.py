class House:
    def __init__(self, id, flat_number, area, floor, room_count, street, building_type, years_of_usage):
        self.__id = id
        self.__flat_number = flat_number
        self.__area = area
        self.__floor = floor
        self.__room_count = room_count
        self.__street = street
        self.__building_type = building_type
        self.__years_of_usage = years_of_usage

    def get_id(self):
        return self.__id

    def get_flat_number(self):
        return self.__flat_number

    def get_area(self):
        return self.__area

    def get_floor(self):
        return self.__floor

    def get_room_count(self):
        return self.__room_count

    def get_street(self):
        return self.__street

    def get_building_type(self):
        return self.__building_type

    def get_years_of_usage(self):
        return self.__years_of_usage

    def set_id(self, id):
        self.__id = id

    def set_flat_number(self, flat_number):
        self.__flat_number = flat_number

    def set_area(self, area):
        self.__area = area

    def set_floor(self, floor):
        self.__floor = floor

    def set_room_count(self, room_count):
        self.__room_count = room_count

    def set_street(self, street):
        self.__street = street

    def set_building_type(self, building_type):
        self.__building_type = building_type

    def set_years_of_usage(self, years_of_usage):
        self.__years_of_usage = years_of_usage

    @staticmethod
    def calculate_age(years_of_usage):
        current_year = 2024  # Текущий год
        return current_year - years_of_usage

    def is_renovation_needed(self):
        age = House.calculate_age(self.__years_of_usage)
        return age >= 30

def get_flats_with_room_count(flats, room_count):
    return [flat for flat in flats if flat.get_room_count() == room_count]

def get_flats_with_room_count_and_floor_range(flats, room_count, min_floor, max_floor):
    return [flat for flat in flats if flat.get_room_count() == room_count and min_floor <= flat.get_floor() <= max_floor]

# Создание списка объектов House
houses = [
    House(1, 101, 70, 2, 3, "Улица 1", "Многоквартирный", 1995),
    House(2, 202, 80, 5, 4, "Улица 2", "Многоквартирный", 2005),
    House(3, 303, 60, 3, 2, "Улица 3", "Частный дом", 1980),
    House(4, 404, 90, 4, 3, "Улица 4", "Многоквартирный", 2010),
    House(5, 505, 100, 6, 4, "Улица 5", "Частный дом", 1985)
]

# Вывод списка квартир с заданным числом комнат
room_count = 3
flats_with_room_count = get_flats_with_room_count(houses, room_count)
print(f"Список квартир с {room_count} комнатами:")
for flat in flats_with_room_count:
    print(f"Квартира №{flat.get_flat_number()}, площадь: {flat.get_area()} кв.м")

print()

# Вывод списка квартир с заданным числом комнат и этажем в заданном промежутке
room_count = 4
min_floor = 3
max_floor = 5
flats_with_room_count_and_floor_range = get_flats_with_room_count_and_floor_range(houses, room_count, min_floor, max_floor)
print(f"Список квартир с {room_count} комнатами и этажем от {min_floor} до {max_floor}:")
for flat in flats_with_room_count_and_floor_range:
    print(f"Квартира №{flat.get_flat_number()}, площадь: {flat.get_area()} кв.м")