import math

v1=[1,2,-4]
v2=[-1,3,4]
v3=[0,-4,2]

def vector_add(v1,v2):
    return [v1_i+v2_i for v1_i,v2_i in zip(v1,v2)]    




def vector_sum_all(v):
    res_vec=v[0]
    for i in v[1:]:
        print ("i",i)
        res_vec=vector_add(res_vec, i)
    return res_vec

def scalar_multiply(s,v):
    #print("Y", len(v))

    return [s*vi for vi in v]

def vec_mean(v):
    print("X", vector_sum_all(v))
    return scalar_multiply(1/len(v), vector_sum_all(v))

def dot(v1,v2):
    return sum(v1_i*v2_i for  v1_i,v2_i in zip(v1,v2))


def norm(v):
    return math.sqrt(norm_sq(v))


def vector_sub(v1, v2):
    return [v1_i-v2_i for v1_i, v2_i in zip(v1, v2)]

def norm_sq(v):
    return dot(v,v)


def sq_distance(v1,v2):
    return norm_sq(vector_sub(v1, v2))


def distance(v1, v2):
    return math.sqrt(sq_distance(v1,v2))



# print(vector_add(v1, v2))
# print(vector_sum_all([v1, v2, v3]))
# print(scalar_multiply(3,v1))
# print(vec_mean([v1,v2,v3]))
# print (dot(v1,v2))
# print (norm_sq(v1))
# print(norm(v1))
# print (distance(v1,v2))


#matrices
A=[[1,2,3],
   [4,5,6]]
B=[[1,2],
   [3,4],
   [5,6]]

def shape(M):
    num_rows=len(M)
    num_cols=len(M[0]) if M else 0
    return num_rows,num_cols
def get_row(M,i):
    return M[i]
def get_col(M,j):
    return [M_i[j] for M_i in M]

def make_matirx(num_rows,num_cols,entry_fn):
    return [[entry_fn(i,j) 
                for j in range(num_cols)]
                for i in range(num_rows)]

def is_diagonal(i,j):
    return 1 if i==j else 0

print (shape(A),shape(B))
print (get_row(A,1))
print(get_col(A, 1))
print(make_matirx(10, 10, is_diagonal))
