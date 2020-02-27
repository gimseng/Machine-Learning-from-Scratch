import math, random
from collections import Counter
import matplotlib.pyplot as plt

def bucketize(point,bucket_size):
    return bucket_size*math.floor(point/bucket_size)

def make_histogram (points, bucket_size):
    return Counter(bucketize(point,bucket_size) for point in points)

def plot_histogram(points,bucket_size,title=""):
    histogram=make_histogram(points,bucket_size)
    plt.bar(histogram.keys(),histogram.values(),width=bucket_size)
    plt.title(title)
    plt.show()

random.seed(0)

#uniform=[200*random.random()-100 for _ in range(10000)]


plot_histogram([1,1,2,2,2,3,3,10,10,8,8,11,12,13,1,0,1,1,1],2)