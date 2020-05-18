from random import randint, choice
from math import sqrt, floor
from os.path import realpath, exists, join, dirname
from os import makedirs
from datetime import date
from time import time
from string import ascii_letters

def coordinates_generator(total, min_x, max_x, min_y, max_y):
    """
    Function that generates random coordinates within some range
    """
    coordinates = []
    for i in range(total):
        x = randint(min_x, max_x)
        y = randint(min_y, max_y)
        coordinates.append((x, y))
    return coordinates

def weights_generator(coordinates, min_w, max_w):
    """
    Function that generates random weights for each coordinate within some range 
    """
    weights = []
    for i in range(len(coordinates)):
        coordinate_weight = randint(min_w, max_w)
        weights.append(coordinate_weight)
    return weights

def distance_matrix_generator(coordinates):
    """
    Function that generates a distance matrix from a list of coordinates
    """
    distance_matrix = []
    for i in range(len(coordinates)):
        distances = []
        for j in range(len(coordinates)):
            distance = sqrt(((coordinates[i][0] - coordinates[j][0]) ** 2) + ((coordinates[i][1] - coordinates[j][1]) ** 2))
            distances.append(int(distance))
        distance_matrix.append(distances)
    return distance_matrix

def write_file(total, coordinates, weights, distances, cluster_capacity, cluster_number, directory_path):
    """
    Function that generates a file with generated data on a given directory path
    """
    today = date.today()
    identifier = ""
    for i in range(5):
        identifier += choice(ascii_letters)
    filename = identifier + "-" + today.strftime("%b-%d-%Y") + "-" + str(total) + ".txt"
    file_path = join(directory_path, filename)
    with open(file_path, 'w') as file_object:
        header = str(cluster_number) + "     " + str(cluster_capacity) + "\n"
        file_object.write(header)
        for i in range(len(coordinates)):
            line = str(i) + "     " + str(coordinates[i]) + "     " + str(weights[i]) + "     " + str(distances[i]) + "\n"
            file_object.write(line)

def instance_generator():
    """
    Function pipelane to generate the instance with the user's input
    """

    # Get the current script's path
    path = realpath(__file__)

    # Directory creation for saving instances
    if not exists(join(dirname(path), 'Instances')):
        try:
            makedirs('Instances')
        except FileExistsError:
            print("WARNING: FILE EXISTS")

    directory_path = join(dirname(path), 'Instances')

    # Validation block for user's input TODO
    try:
        total_coordinates = int(input("ENTER the number of coordinates you want to generate: "))
    except:
        print("ERROR: USER INPUT")
    try:
        minimum_x = int(input("ENTER the minimum value for x: "))
    except:
        print("ERROR: USER INPUT")
    try:
        maximum_x = int(input("ENTER the maximum value for x: "))
    except:
        print("ERROR: USER INPUT")
    try:
        minimum_y = int(input("ENTER the minimum value for y: "))
    except:
        print("ERROR: USER INPUT")
    try:
        maximum_y = int(input("ENTER the maximum value for y: "))
    except:
        print("ERROR: USER INPUT")
    try:
        minimum_w = int(input("ENTER the minimum value for the weights: "))
    except:
        print("ERROR: USER INPUT")
    try:
        maximum_w = int(input("ENTER the maximum value for the weights: "))
    except:
        print("ERROR: USER INPUT")

    start_time = time()
    # Call generator functions
    instance_coordinates = coordinates_generator(total_coordinates, minimum_x, maximum_x, minimum_y, maximum_y)
    instance_weights = weights_generator(instance_coordinates, minimum_w, maximum_w)
    instance_distance_matrix = distance_matrix_generator(instance_coordinates)
    
    # Generate cluster capacity
    if len(instance_weights) <= 200:
        percentage = 0.20
    elif len(instance_weights) <= 500:
        percentage = 0.50
    elif len(instance_weights) <= 10000:
        percentage = 0.05
    total_clusters = int(len(instance_weights) * percentage)
    cluster_cap = int((sum(instance_weights) / total_clusters) + (sum(instance_weights) * 0.10))

    # File writing block
    write_file(total_coordinates, instance_coordinates, instance_weights, instance_distance_matrix, cluster_cap, total_clusters, directory_path)
    print("FINISHED GENERATING INSTANCE IN:", (time() - start_time), "seconds \n")