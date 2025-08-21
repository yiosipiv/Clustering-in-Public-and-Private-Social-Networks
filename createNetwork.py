import time
import random
import numpy as np
import multiprocessing as mp
import matplotlib.pyplot as plt
import formatDataset as dataDict

def convert(seconds):
    return time.strftime("%H:%M:%S", time.gmtime(seconds))

def split_edges(edges):
    # Function 2
    # split edges into four separate buckets 
    split = [{} for _ in range(4)]
    while True:
        for subdict in split:
            if not edges:
                create_vertices(split)
                return 0
            key, val = edges.popitem(last=False)
            subdict[key] = val

def create_vertices(edge):
    # Function 3
    # this will take a subdictionary of the output of Function 2, gather keys of each subdictionary
    vertices = []
    print(edge)
    for key, value in edge.items():
        vertices.append(key)
    return vertices
