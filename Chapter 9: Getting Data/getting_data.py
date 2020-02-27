import math

def bucketize(point,bucket_size):
    return bucket_size*math.floor(point/bucket_size)
