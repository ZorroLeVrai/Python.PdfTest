import matplotlib.pyplot as plt
import pandas as pd

def create_pdf(index):
    file_name = f"results_{index}.csv"
    df = pd.read_csv(file_name)

    # Plot the graph
    plt.plot(df['x'], df['y'])
    plt.title("Graph of my_function")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)

    #transform to pdf
    plt.savefig(f"doc_{index}.pdf")
    #clear figure
    plt.clf()


def create_pdfs():
    for i in range(1, 11):
        create_pdf(i)

create_pdfs()