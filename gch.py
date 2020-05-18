from time import time
from random import randint
from operator import itemgetter

def greedy_construction_heuristic(points, number_clusters, cluster_capacity, weights, distance_matrix):
    start_time = time()
    customers = [x for x in range(points)]
    weights_clone = weights.copy()
    distance_matrix_clone = distance_matrix.copy()
    clusters = []
    clusters_weights = []

    # Create data matrixes where results will be stored
    for i in range(number_clusters):
        clusters.append([])
        clusters_weights.append([])


    # Add the data to a list
    problem_data = []
    for i in range(len(weights)):
        problem_data.append([customers[i], weights_clone[i]])

    # Select random seeds
    for i in range(number_clusters):
        seed = randint(0, number_clusters)
        clusters[i].append(problem_data[seed][0])
        clusters_weights[i].append(problem_data[seed][1])
        del problem_data[seed]
    
    # Calculate regret value
    for i in range(len(problem_data)):
        regret_value = 0
        customer_to_cluster_distances = []
        for j in range(number_clusters):
            cluster_id = clusters[j][0]
            customer_id = problem_data[i][0]
            customer_to_cluster_distances.append(distance_matrix_clone[cluster_id][customer_id])
        customer_to_cluster_distances = sorted(customer_to_cluster_distances)
        first_nearest_node = customer_to_cluster_distances[0]
        second_nearest_node = customer_to_cluster_distances[1]
        regret_value = abs(first_nearest_node - second_nearest_node)
        problem_data[i].append(regret_value)
    
    problem_data = sorted(problem_data, key=itemgetter(2), reverse=True)
    while(len(problem_data) > 0):
        distance_value = 0
        cluster_id = 0
        cluster_distances = []
        for j in range(len(clusters)):
            median = clusters[j][0]
            customer = problem_data[0][0]
            distance_value = distance_matrix_clone[median][customer]
            cluster_distances.append((j, distance_value))

        #min_distances = sorted(cluster_distances, key=itemgetter(1), reverse=False)
        #print(min_distances)
        FLAG = True
        while(FLAG):
            min_dist = min(cluster_distances, key=itemgetter(1))
            # min_dist_index = min_dist[0][0]
            min_dist_index = min_dist[0]
            clusters_weights[min_dist_index].append(problem_data[0][1])
            if sum(clusters_weights[min_dist_index]) <= cluster_capacity:
                clusters[min_dist_index].append(problem_data[0][0])
                del problem_data[0]
                FLAG = False
            else:
                clusters_weights[min_dist_index].remove(problem_data[0][1])
                # del min_distances[0]
                cluster_distances.remove(min_dist)
                
    
    objective_function_value = 0
    for i in range(len(clusters)):
        for j in range(len(clusters[i])):
            objective_function_value += distance_matrix[clusters[i][0]][clusters[i][j]]
    print("GCH OBJECTIVE FUNCTION RESULT:", objective_function_value)

    for i in range(len(clusters)):
        print("Cluster:", i, "Storage:", str(sum(clusters_weights[i])) + "/" + str(cluster_capacity))
    print("TIME TO SOLVE:", (time() - start_time), "seconds")
    return clusters, clusters_weights, objective_function_value