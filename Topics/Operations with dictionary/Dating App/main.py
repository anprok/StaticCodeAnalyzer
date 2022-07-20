def select_dates(potential_dates):
    age = 30
    city = 'Berlin'
    hobby = "art"
    result = [i['name'] for i in potential_dates if i['age'] > age and i['city'] == city and hobby in i['hobbies']]
    return ", ".join(result)
