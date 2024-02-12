import pandas as pd
import numpy as np
import random

def create_function():
    nb_terms = random.randint(2, 6)
    def myfunction(x):
        result = 0
        for _ in range(nb_terms+1):
            result *= x
            result += random.randint(-50, 50) / 10
        return result

    return myfunction


def create_csv(index):
    f = create_function()

    x_values = np.linspace(-10, 10, 100)
    y_values = f(x_values)

    df = pd.DataFrame({'x': x_values, 'y': y_values})

    # Save the DataFrame to a CSV file
    df.to_csv(f"results_{index}.csv", index=False)

def create_csvs():
    for i in range(1, 11):
        create_csv(i)

create_csvs()