class House:
    def __init__(self, id, flat_number, area, floor, room_count, street, building_type, years_of_usage):
        self.id = id
        self.flat_number = flat_number
        self.area = area
        self.floor = floor
        self.room_count = room_count
        self.street = street
        self.building_type = building_type
        self.years_of_usage = years_of_usage




    def calculate_age(self):
        current_year = 2024  # Текущий год
        return current_year - self.years_of_usage

    def is_renovation_needed(self):
        age = self.calculate_age()
        return age >= 30

def get_flats_with_room_count(flats, room_count):
    return [flat for flat in flats if flat.room_count == room_count]

def get_flats_with_room_count_and_floor_range(flats, room_count, min_floor, max_floor):
    return [flat for flat in flats if flat.room_count == room_count and min_floor <= flat.floor <= max_floor]

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
    print(f"Квартира №{flat.flat_number}, площадь: {flat.area} кв.м")

print()

# Вывод списка квартир с заданным числом комнат и этажем в заданном промежутке
room_count = 4
min_floor = 3
max_floor = 5
flats_with_room_count_and_floor_range = get_flats_with_room_count_and_floor_range(houses, room_count, min_floor, max_floor)
print(f"Список квартир с {room_count} комнатами и этажем от {min_floor} до {max_floor}:")
for flat in flats_with_room_count_and_floor_range:
    print(f"Квартира №{flat.flat_number}, площадь: {flat.area} кв.м, этаж: {flat.floor}")