from time import time
from operator import itemgetter

def heaviest_weight_edge(points, number_clusters, cluster_capacity, weights, distance_matrix):
    start_time = time()
    customers = [x for x in range(points)]
    weights_clone = weights.copy()
    clusters = []
    clusters_weights = []

    # Create data matrixes where results will be stored
    for i in range(number_clusters):
        clusters.append([])
        clusters_weights.append([])

    problem_data = []
    for i in range(len(weights)):
        problem_data.append((customers[i], weights_clone[i]))

    problem_data = sorted(problem_data, key=itemgetter(1), reverse=True)
    j = 0
    while(len(problem_data) > 0):
        if j < number_clusters:
            clusters[j].append(problem_data[0][0])
            clusters_weights[j].append(problem_data[0][1])
            if sum(clusters_weights[j]) > cluster_capacity:
                clusters[j].remove(problem_data[0][0])
                clusters_weights[j].remove(problem_data[0][1])
            else:
                del problem_data[0]
            j += 1
        else:
            j = 0


    objective_function_value = 0
    for i in range(len(clusters)):
        for j in range(len(clusters[i])):
            objective_function_value += distance_matrix[clusters[i][0]][clusters[i][j]]
    print("HWE OBJECTIVE FUNCTION RESULT:", objective_function_value)
    
    for i in range(len(clusters)):
        print("Cluster:", i, "Storage:", str(sum(clusters_weights[i])) + "/" + str(cluster_capacity))
    print("TIME TO SOLVE:", (time() - start_time), "seconds")
    return clusters, clusters_weights, objective_function_value