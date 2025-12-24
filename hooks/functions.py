def generate_item_names(name: str, amount: int) -> list:
    item_table = []

    for a in range(amount + 1):
        item_table.append({
            'name': name + " - " + str(a),
            'category': ["Pet " + name],
            'progression': True, # capitalized in Python, not in JSON
        })

    return item_table

def generate_location_names(name: str, amount: int) -> list:
    location_table = []

    for a in range(amount + 1):
        location_table.append({
            'name': name + " - " + str(a),
            'category': ["Pet " + name],
            'requires': "|Pet " + name + ":" + str(a) + "|"
        })

    return location_table