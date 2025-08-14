def create_edges():
    # Create edges from dataset provided in the .txt file in the path below
    # Optimized for facebook-links dataset
    # Inside the function, variable "z" represents a timestamp when a connection was made made between users "x" and "y". Not all 
    # users have timestamps available. Timestamps are not the goal of this project, so "z is ignored"
    edges = {}
    with open("myfilepath/facebook-links.txt", "r") as file:
        for line in file:
            x, y, z = line.split()
            if x not in edges:
                edges[x] = []
            edges[x].append(y)
    file.close()
    return edges

if __name__ == '__main__':
    create_edges()
