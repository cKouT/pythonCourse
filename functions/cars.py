def make_car(manufacturer, model, **car_infos):
	profile = {}
	profile ['manufacturer'] = manufacturer
	profile['model'] = model

	for key, value in car_infos.items():
		profile[key] = value

	return profile

car = make_car('peugeot', '206', couleur='blanche', puissance='70cv')
print(car)