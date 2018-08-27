import random


# generate random source list
def generate_source_list():
    lenght = random.randint(10, 15)
    source_list = random.sample(range(0, 50), lenght)
    print(source_list)
    return source_list


# new list with only even items
def list_comprehension(list):
    final_list = [item for item in list if item % 2 == 0]
    return final_list


a = generate_source_list()
print(list_comprehension(a))
