import random, math


def sum_of_squares(v):
    return sum(v_i*v_i for v_i in v)

def difference_quotient (f,x,h):
    return (f(x+h)-f(x))/h

def partial_difference_quotient(f,v,i,h):
    w=[v_j+ (h if j==i else 0) for j, v_j in enumerate(v)]
    return (f(w)-f(v))/h

def estimate_gradient(f,v,h=0.0001):
    return [partial_difference_quotient(f,v,i,h)
            for i,_ in enumerate(v)]

def step(v,direction,step_size):
    return [v_i + step_size*direction_i
            for v_i, direction_i in zip(v,direction)]
def scalar_multiply(s,v):
    #print("Y", len(v))

    return [s*vi for vi in v]


def sum_of_squares_gradient(v):
    return [2*v_i for v_i in v]


def vector_sub(v1, v2):
    return [v1_i-v2_i for v1_i, v2_i in zip(v1, v2)]

def dot(v1, v2):
    return sum(v1_i*v2_i for v1_i, v2_i in zip(v1, v2))



def norm_sq(v):
    return dot(v,v)


def norm(v):
    return math.sqrt(norm_sq(v))

def sq_distance(v1,v2):
    return norm_sq(vector_sub(v1, v2))


def distance(v1, v2):
    return math.sqrt(sq_distance(v1,v2))

v=[random.randint(-10,10) for i in range(3)]
tolerance=0.0000001
# while True:
    
#     print (v)
#     gradient = sum_of_squares_gradient(v)
#     next_v=step(v,gradient,-0.01)
#     if distance(next_v,v)<tolerance:
#         break
#     v=next_v

def safe(f):
    def safe_f(*args,**kwargs):
        try:
            return f(*args,**kwargs)
        except:
            return float('inf')
    return safe_f

def minimize_batch(target_fn,gradient_fn,theta_0,tolerance=0.000001):
    step_sizes = [100, 10, 0.1, 0.01, 0.001, 0.0001, 0.00001]

    theta=theta_0
    target_fn=safe(target_fn)
    value=target_fn(theta)

    while True:
        gradient=gradient_fn(theta)
        next_thetas=[step(theta,gradient,-step_size)
                            for step_size in step_sizes]
        
        next_theta=min(next_thetas,key=target_fun)
        next_value=target_fn(next_theta)

        if abs(value-next_value)<tolerance:
            return theta
        else:
            theta,value = next_theta, next_value

def in_random_order(data):
    indexes=[i for i,_ in enumerate(data)]
    random.shuffle(indexes)

    for i in indexes:
        yield data[i]
    
def minimize_stochastic(target_fn, gradient_fn, x,y , theta_0, alpha=0.01):

    data=zip(x,y)
    theta=theta_0
    alpha=alpha_0
    min_theta,min_value = None, float("inf")
    iterations_with_no_improvement=0

    while iterations_with_no_improvement <100:
        value = sum(target_fn(x_i,y_i,theta) for x_i, y_i in data)

        if value<min_value:
            min_theta,min_value=thetat,value
            iterations_with_no_improvement=0
            alpha=alpha_0
        else:
            iterations_with_no_improvements+=1
            alpha=alpha*0.9

        for x_i, y_i in in_random_order(data):
            gradient_i = gradient_fn(x_i,y_i,theta)
            theta=vector_sub(theta,scalar_multiply(alpha,gradient_i))


