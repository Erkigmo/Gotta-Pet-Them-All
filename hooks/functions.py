def generate_location_names(name: str, amount: int) -> list:
    location_table = []

    for a in range(amount + 1):
        location_table.append({
            'name': name + " - " + str(a),
            'category': ["Pet " + name],
            'requires': "|Pet " + name + ":" + str(a) + "|"
        })

    return location_table