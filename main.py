 
 
from tools import extract_xy_by_table_index, find_varation_indexes, get_A_B_from_to_points, is_y0_between_y1_and_y2, solve_equation, trouver_encadrement_dichotomie, write_solutions_in_csv_tables

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
                debut = variation_indexes[index]
                print("debut : ",debut)
                fin = variation_indexes[index+1]
                print("fin : ",fin)
                sous_liste = y_values[debut:fin]
                #print("sous liste : ")
                #print(sous_liste)
                i,j = trouver_encadrement_dichotomie(sous_liste,-10 )
                print("i : ",i)
                print("j : ",j)
                print(  x_values[ i],  
                    y_values[i], 
                    x_values[j],
                    y_values[j])
                A, B = get_A_B_from_to_points( 
                    #x_values[variation_indexes[index]], 
                    x_values[ i], 
                    #y_values[variation_indexes[index]], 
                    y_values[i], 
                    x_values[j],
                    y_values[j])
                x = solve_equation(A, B, -10)
                solutions.append(x)
                
                print("x : ",x)
                               
                nombre_solution = nombre_solution + 1 
                print(solutions)
    print("-"*20)
    print("nombre soltuion")
    print(nombre_solution) 
    delta_x = 10000000
    if len(solutions) >1 :
        delta_x = solutions[1] - solutions[0]
    
    delta_x_with_table_index = []
    delta_x_with_table_index.append([table_index_to_extract,delta_x])
    
    write_solutions_in_csv_tables("solutions.csv", delta_x_with_table_index)
if __name__ == "__main__":
    for i in range(1):
        extract_solution_for_given_table(i+1 )
 