from os.path import realpath, dirname, join, isfile, exists
from os import listdir, makedirs
from time import time

def read_file():
    """
    Function that reads the data from a selected file, and extracts the weight vector and distance matrix
    """
    path = realpath(__file__)

    # Directory creation for saving output logs
    if not exists(join(dirname(path), 'Logs')):
        try:
            makedirs('Logs')
        except FileExistsError:
            print("WARNING: FILE EXISTS")

    directory_path = join(dirname(path), 'Instances')
    instances_files = [x for x in listdir(directory_path) if isfile(join(directory_path, x))]
    for i in range(len(instances_files)):
        print(str(i) + "-" + instances_files[i])
    
    try:
        instance_option = int(input("ENTER the instance you want to read: "))
    except:
        print("ERROR: USER INPUT")
    
    contents = []

    filename = join(directory_path, instances_files[instance_option])

    start_time = time()
    with open(filename, 'r') as file_object:
        header = file_object.readline()
        header = header.rstrip("\n").split("     ")
        lines = file_object.readlines()[0:]
        for line in lines:
            line = line.rstrip("\n").split("     ")
            contents.append(line)

    print("FINISHED READING TIME IN:", (time() - start_time), "seconds \n")

    instance_number_clusters = int(header[0])
    instance_cluster_capacity = int(header[1])

    instance_customers = []
    instance_weights = []
    instance_distances = []
    for i in range(len(contents)):
        instance_customers.append(int(contents[i][0]))
        instance_weights.append(int(contents[i][2]))
        instance_distances.append(contents[i][3].strip("][").split(","))

    # Turn all strings to int in the distances read from file
    distance_matrix = []
    for i in range(len(instance_distances)):
        row = []
        for j in range(len(instance_distances[i])):
            row.append(int(instance_distances[i][j]))
        distance_matrix.append(row)

    return instance_number_clusters, instance_cluster_capacity, instance_customers, instance_weights, distance_matrix

