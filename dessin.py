import matplotlib.pyplot as plt

from tools import extract_xy_by_table_index

def plot_from_file(tableIndex=1):
    """
    Plots y vs x from data in the given file.

    Args:
        filename (str): The name of the file containing the data.
                         Defaults to "tableau1.txt".
    """

    x_values, y_values = extract_xy_by_table_index(tableIndex) 

    # Plotting the data
    plt.figure(figsize=(8, 6))  # Adjust figure size for better visualization
    plt.scatter(x_values, y_values, marker='o', label='Data Points')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Plot of y vs x')
    plt.grid(True)  # Add grid for better readability
    plt.legend()
    plt.savefig('plot.png')  # Save the plot to a file
    #plt.show() #comment out plt.show()

if __name__ == "__main__":
    plot_from_file()
