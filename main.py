from instances_gen import instance_generator
from file_reader import read_file
from hwe import heaviest_weight_edge
from gch import greedy_construction_heuristic
from omp import local_search

def main():
    try:
        user_option = int(input("1- Create new instance \n2- Read a file\nOPTION: "))
    except:
        print("ERROR: USER INPUT")
    
    if user_option == 1:
        instance_generator()
    elif user_option == 2:
        clusters_amount, capacity, customers, weights, distance_matrix = read_file()
        solved_clusters_hwe, solved_clusters_weights_hwe, objective_function_hwe = heaviest_weight_edge(len(weights), clusters_amount, capacity, weights, distance_matrix)
        solved_clusters_gch, solved_clusters_weights_gch, objective_function_gch = greedy_construction_heuristic(len(weights), clusters_amount, capacity, weights, distance_matrix)
        local_search(solved_clusters_hwe, solved_clusters_weights_hwe, distance_matrix, objective_function_hwe)
        local_search(solved_clusters_gch, solved_clusters_weights_gch, distance_matrix, objective_function_gch)
main()