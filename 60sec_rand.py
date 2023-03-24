import random
import weigths_data

# define the dictionary with weights
people_weights = weigths_data.data

print(people_weights)
# invert the weights so that the lowest weight becomes the highest, and vice versa
inverted_weights = {person: 1/weight for person,
                    weight in people_weights.items()}

# calculate the total weight of all people
total_weight = sum(inverted_weights.values())

# normalize the weights so they add up to 1
normalized_weights = {
    person: weight/total_weight for person, weight in inverted_weights.items()}

# generate a random number between 0 and 1
rand_num = random.random()

# iterate through the people and their normalized weights until the cumulative weight
# exceeds the random number generated above
cumulative_weight = 0
for person, weight in normalized_weights.items():
    cumulative_weight += weight
    if rand_num <= cumulative_weight:
        # we have found the person whose normalized weight caused the cumulative weight
        # to exceed the random number, so we return that person
        print(person)
        break
