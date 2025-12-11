def generate_item_names(name: str, amount: int) -> list:
	item_table = []

	for a in range(amount):
        item_table.append({
            'name': name + " - " + a,
            'category': ["Pet " + name],
            'progression': True, # capitalized in Python, not in JSON
        })

    return item_table

def generate_location_names(name: str, amount: int) -> list:
	location_table = []

	for a in range(amount):
        location_table.append({
            'name': name + " - " + a,
            'category': ["Pet " + name],
            'requires': name + " - " + a
        })

    return location_table