import csv

def write_solutions_in_csv_tables(output_filename,solutions=[]):
    """
    Writes specific solutions to a CSV file.

    Args: 
        output_filename (str): The name of the output CSV file.
    """
    try:
        with open(output_filename, 'a', newline='') as outfile:
            csv_writer = csv.writer(outfile) 
            for item in solutions :
                csv_writer.writerow([item[0],item[1]])
    except Exception as e:
        print(f"An error occurred: {e}")

def get_A_B_from_to_points(x1:float, y1:float,x2:float,y2:float) -> tuple:
    """
    Get the A and B values of the line equation y = Ax + B from two points.
    :param p1: First point (x1, y1)
    :param p2: Second point (x2, y2)
    :return: A, B
    """


    if x1 == x2:
        raise ValueError("The x-coordinates of the two points cannot be the same.")

    A = (y2 - y1) / (x2 - x1)
    B = y1 - A * x1

    return A, B

def solve_equation(A:float, B:float, y0:float) -> float:
    """
    Solve the equation y = Ax + B for x given y0.
    :param A: Coefficient A
    :param B: Coefficient B
    :param x: x-coordinate
    :param y0: y-coordinate
    :return: x-coordinate of the point on the line where y = y0
    """
    if A == 0:
        raise ValueError("Coefficient A cannot be zero.")

    return (y0 - B) / A



def find_varation_indexes(mylist:list[float]) -> list[int]:
    """
    Trouve les indices des variations dans une liste de nombres.

    Args:
        mylist: Une liste de nombres.

    Returns:
        Une liste d'indices où les variations se produisent.
    """
    isIncreasing = mylist[0] < mylist[1]
    index = 0
    variation_indexes = []
    variation_indexes.append(0) 
    while index < len(mylist)-1 :
        if mylist[index] < mylist[index + 1]:
            if not isIncreasing:
                variation_indexes.append(index)
                isIncreasing = True
            else:
                pass
        elif mylist[index] > mylist[index + 1]:
            if isIncreasing:
                variation_indexes.append(index)
                isIncreasing = False
            else:
                pass
        index = index + 1
    if len(variation_indexes) < index :
        variation_indexes.append(len(mylist)-1)


    return variation_indexes

def is_y0_between_y1_and_y2(y0:float, y1:float,y2:float) -> bool:
    """
    Trouve la solution de l'équation y = y0 entre deux valeurs y0 et y1.

    Args:
        y0,y1 et y2: Trois valeurs flottantes.
    Returns:
        La solution de l'équation y = y0 entre les deux valeurs.
    """ 
    t = (y0-y1) * (y0-y2) 
    bb = t < 0 or t == 0
    return bb


def extract_xy_by_table_index(filename="tables.csv", target_table_index=None):
    """
    Extracts x and y values for a specific table index from a CSV file.

    Args:
        filename (str): The name of the CSV file to read.
        target_table_index (int): The integer index of the table to extract data from.
    """
    x_values = []
    y_values = []

 

    try:
        with open(filename, 'r', newline='') as infile:
            csv_reader = csv.reader(infile)
            header = next(csv_reader)  # Skip the header row

            table_index_column = header.index('tableIndex')
            x_column = header.index('x')
            y_column = header.index('y')

            for row in csv_reader:
                try:
                    current_table_index = int(row[table_index_column])
                    if current_table_index == target_table_index:
                        x_values.append(float(row[x_column]))
                        y_values.append(float(row[y_column]))
                except ValueError:
                    #print(f"Skipping row with invalid data: {row}")
                    pass
                except IndexError:
                    #print(f"Skipping row with missing columns: {row}")
                    pass

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except ValueError as e:
        print(f"Error: Could not find the required column in the header: {e}")
    except Exception as e:
        print(f"An error occurred while reading the CSV file: {e}")

    return x_values, y_values

 
def trouver_encadrement_dichotomie(mylist:list, x:float,debeug=False):
    """
    Trouve l'encadrement d'une valeur x dans une liste triée mylist.
    
    Args:
        mylist: Une liste triée d'éléments.
        x: La valeur à encadrer.
    
    Returns:
        Un tuple (a, b) où a et b sont les indeces éléments de mylist tels que"
    """
    m=0
    i = 0
    j = len(mylist) - 1
    if debeug :
        print("i  j     m   x  mylist[i] mylist[j] mylist[m]")
        print("-----------------------------------------------------")
        print(f"{i}  {j}     {m}   {x}  {mylist[i]}       {mylist[j]}     {mylist[m]}")
    if mylist[i] == x :
        return (i, i)
    elif mylist[j] == x : 
        return (j, j)
    else: 
        while  j-i > 1 : 
            k = (i + j) % 2 
            if k == 0 :
                m = int((i + j) / 2) 
            elif k == 1 :   
                m = int((i + j+1) / 2 ) 
            if mylist[m] == x :
                i = m
                j = m 
            
            elif (mylist[i]-x)*(mylist[m]-x) < 0 : 
                j = m
            else :
                i = m
            if debeug :
                print(f"{i}  {j}     {m}   {x}  {mylist[i]}       {mylist[j]}     {mylist[m]}")
        return (i, j)
    
 