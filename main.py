 
 
from tools import extract_xy_by_table_index, find_varation_indexes, get_A_B_from_to_points, is_y0_between_y1_and_y2, solve_equation, write_solutions_in_csv_tables

def extract_solution_for_given_table(table_index_to_extract:int ): 
    print("table index to extract")
    print(table_index_to_extract)
    x_values, y_values = extract_xy_by_table_index(target_table_index=table_index_to_extract) 
    variation_indexes = find_varation_indexes(y_values)  
    nombre_solution = 0
    solutions = []
    print("-"*20)
    for index, item in enumerate(variation_indexes) :  
        if index < len(variation_indexes)-1 :
            h = is_y0_between_y1_and_y2(-10,y_values[variation_indexes[index]],y_values[variation_indexes[index+1]]) 
            if h:
                A, B = get_A_B_from_to_points( 
                    x_values[variation_indexes[index]], 
                    y_values[variation_indexes[index]], 
                    x_values[variation_indexes[index+1]],
                    y_values[variation_indexes[index+1]])
                x = solve_equation(A, B, -10)
                solutions.append(x)
                
                print("x : ",x)
                               
                nombre_solution = nombre_solution + 1 
    print("-"*20)
    print("nombre soltuion")
    print(nombre_solution)
    solutions_with_table_index = []
    for soltion in solutions :
        solutions_with_table_index.append([soltion,table_index_to_extract])
    
    write_solutions_in_csv_tables("solutions.csv",solutions_with_table_index)
if __name__ == "__main__":
    for i in range(3):
        extract_solution_for_given_table(i+1 )
 