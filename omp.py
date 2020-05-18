from time import time

def get_distances(cluster, distance_matrix):
    total_distance = 0
    for i in range(len(cluster)):
        median = cluster[0]
        customer = cluster[i]
        total_distance += distance_matrix[median][customer]
    return total_distance

def one_move_operator(node_v, cluster_i, cluster_j, distance_matrix, objective_function_value):
    cluster_j_clone = cluster_j.copy()
    cluster_i_clone = cluster_i.copy()
    cluster_i_clone.remove(node_v)
    cluster_j_clone.append(node_v)
    # print("NODE:", node_v, "moved from Cluster:", cluster_i, "to Cluster:", cluster_j, "\n")
    cluster_i_distance = get_distances(cluster_i, distance_matrix)
    cluster_i_new_distance = get_distances(cluster_i_clone, distance_matrix)
    cluster_j_distance = get_distances(cluster_j, distance_matrix)
    cluster_j_new_distance = get_distances(cluster_j_clone, distance_matrix)
    total_distance = objective_function_value - (cluster_i_distance - cluster_i_new_distance) + (cluster_j_new_distance - cluster_j_distance) 
    # print("Distance difference:", cluster_j_new_distance - cluster_j_distance)
    return (cluster_j_clone, total_distance)

def local_search(clusters, clusters_weights, distance_matrix, objective_function_value):
    start_time = time()
    moves = []
    for i in range(len(clusters)):
        for j in range(len(clusters)):
            for k in range(len(clusters[i])):
                if i != j and k != 0:
                    new_cluster, new_objective_function = one_move_operator(clusters[i][k], clusters[i], clusters[j], distance_matrix, objective_function_value)
                    moves.append((new_cluster, new_objective_function))
                    

    print(moves)
    print("TIME TO SOLVE:", (time() - start_time), "seconds")