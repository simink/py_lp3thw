## ex39 - dictionaries

## create mapping of state to abbreviation
states = {
    'oregon': 'OR',
    'florida': 'FL',
    'california': 'CA',
    'new york': 'NY',
    'michigan': 'MI'
}

## create basic set of states and some cities
cities = {
    'CA': 'san francisco',
    'MI': 'detroit',
    'FL': 'jacksonville'
}

# add more cities
cities['NY'] = 'new york'
cities['OR'] = 'portland'

## print cities
print('-' * 10)
print("NY states has: ", cities['NY'])
print("OR state has: ", cities['OR'])

## print some states
print('-' * 10)
print("michigan's abbrv is: ", states['michigan'])
print("florida's abbrv is: ", states['florida'])

## print state then cities dict
print('-' * 10)
print("michigan's abbrv is: ", cities[states['michigan']])
print("florida's abbrv is: ", cities[states['florida']])

## print every state abbreviation
print('-' * 10)
for state, abbr in list(states.items()):
    print(f"{state} is abbreviated as {abbr}")

## print every city in state
print('-' * 10)
for abbr, city in list(cities.items()):
    print(f"{abbr} has the city {city}")

## print both
print('-' * 10)
for state, abbr in list(states.items()):
    print(f"{state} state is abbreviated as {abbr} and has city {cities[abbr]}")

## get abbr by state which is not there
print('-' * 10)
state = states.get('texas')

if not state:
    print("sorry, no texas")

# get city with default value
city = cities.get('TX', 'Does not exist')
print(f"the city for state TX is: {city}")

