import autoInfo

engine = autoInfo.Search()


car_num = input("Введите номер авто: ")
vin = engine.get_vin_by_number(car_num)
print(f"Пример поиска VIN по номеру авто: {vin}")
print("Пример поиска информации по номеру:")
print(engine.get_car_data_by_number(car_num))

car_vin = input("Введите VIN: ")
print("Пример поиска информации по VIN:")
print(engine.get_car_data_vin(car_vin))
