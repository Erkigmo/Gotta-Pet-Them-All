def generate_item_names(name: str, amount: int) -> list:
	for a in range(amount):
        item_table.append({
            'name': name + " - " + a,
            'category': ["Pet " + name],
            'progression': True, # capitalized in Python, not in JSON
        })

def generate_item_names(name: str, amount: int) -> list:
	for a in range(amount):
        item_table.append({
            'name': name + " - " + a,
            'category': ["Pet " + name],
            'requires': name + " - " + a
        })