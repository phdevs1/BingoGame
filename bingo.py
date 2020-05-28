from random import randrange


def generate_random_number(lower, upper):
    random = randrange(lower, upper)
    return random

def generate_cards(rows, columns, lower, upper):
    card_columns = list()
    increment = upper = int(upper / 5)
    for i in range(columns):
        current_column = list()
        while len(current_column) < rows:
            candidate = generate_random_number(lower, upper)
            if candidate not in current_column:
                current_column.append(candidate)
        lower += increment
        upper += increment
        card_columns.append(current_column)
    card_columns[2][2] = ""
    return card_columns





cards = generate_cards(5,5,1,75);
print (cards)