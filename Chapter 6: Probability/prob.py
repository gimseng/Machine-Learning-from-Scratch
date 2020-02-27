import random, math
import matplotlib.pyplot as plt

def random_kid():
    return random.choice(["boy","girl"])

both_girls=0
older_girl=0
either_girl=0


# for _ in range(10000):
#     younger=random_kid()
#     older=random_kid()
#     if older=="girl":
#         older_girl+=1
#     if older=="girl" and younger=="girl":
#         both_girls+=1
#     if older=="girl" or younger=="girl":
#         either_girl+=1

#print (round(both_girls/older_girl,2))
#print (round(both_girls/either_girl,2))

def uniform_pdf(x):
    return 1 if x>=0 and x<1 else 0

def uniform_cdf(x):
    if x<0: return 0
    elif x<1: return x
    else: return 1

# xs=[-1+x/5.0 for x in range(20)]
# ys = [uniform_pdf(x) for x in xs]
# print(xs)

# plt.plot(xs,ys)
# plt.show()
def normal_pdf(x,mu=0,sigma=1):
    sqrt_two_pi=math.sqrt(2*math.pi)
    return math.exp(-(x-mu)**2/(2*sigma**2))/(sigma*sqrt_two_pi)

xs=[x/10.0 for x in range(-50,50)]
#ys = [uniform_pdf(x) for x in xs]
# print(xs)

# plt.plot(xs,[normal_pdf(x,sigma=1) for x in xs],'-')
# plt.plot(xs, [normal_pdf(x,sigma=0.2) for x in xs],'--')
# plt.plot(xs, [normal_pdf(x,sigma=0.5) for x in xs],':')
# plt.plot(xs, [normal_pdf(x,mu=1) for x in xs],'-.')
# plt.show()

def bernoulli_trial(p):
    return 1 if random.random()<p else 0

def binomial(n,p):
    return sum(bernoulli_trial(p) for _ in range (n))

from collections import defaultdict, Counter

new_dict=defaultdict(int)
for _ in range(1000):
    new_dict[bernoulli_trial(0.6)]+=1
#print (new_dict)

# bernouli_trial --> mean= p (1) + (1-p)(0)=p.  Variance =  p(1-p)^2+(1-p)(p)^2=p(1-p).
# sum of n bernouli_trial -> mean: np, variance -> n p (1-p)


def make_hist(p,n,num_points):
    data=[binomial(n,p) for _ in range(num_points)]
    histogram=Counter(data)
    plt.bar([x-0.4 for x in histogram.keys()],
            [v/num_points for v in histogram.values()], 0.8, color='0.75')
    mu=p*n
    sigma=math.sqrt(n*p*(1-p))
    xs=range(min(data),max(data)+1)
    ys = [normal_pdf(x,mu,sigma) for x in xs]
    plt.plot(xs,ys)
    plt.show()
    #return histogram
    #print (data)

(make_hist(0.3,100,10000))
# looks normal !
