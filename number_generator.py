import random
import progressbar


def number_generator(total_iterations):
    file = open("number_generator.csv", "a")
    for i in range(total_iterations):
        rand_number = random.randint(1, 100)
        file.write(f"\n{i};{rand_number}")
        progressbar.progress(i,total_iterations)
    file.close()
    return

