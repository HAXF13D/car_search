import autoInfo

engine = autoInfo.Search()

vin = engine.get_vin_by_number("В039РС26")
print(vin)
print(engine.get_car_data_vin(vin))
print(engine.get_car_data_by_number("В039РС26"))
