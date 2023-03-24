num_games = {
    'AndreJ': 17,
    'Andrey K': 27,
    'Dasha': 27,
    'Dima': 27,
    'Katya': 27,
    'Kiril': 27,
    'Nika': 27,
    'Sasha': 11,
    'Vera': 27,
}

num_visit_intents = {
    'AndreJ': 10,
    'Andrey K': 21,
    'Dasha': 10,
    'Dima': 16,
    'Katya': 23,
    'Kiril': 22,
    'Nika': 18,
    'Sasha': 11,
    'Vera': 20,
}

data = {person: num_visit_intents[person] /
        num_games[person] for person in num_games}


# data = {
#     'Sasha': 1,
#     'Katya': 0.8461538462,
#     'Kiril': 0.8076923077,
#     'Andrey K': 0.7692307692,
#     'Vera': 0.7307692308,
#     'Nika': 0.6538461538,
#     'Dima': 0.6153846154,
#     'AndreJ': 0.5625,
#     'Dasha': 0.3846153846
# }
