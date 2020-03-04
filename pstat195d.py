import math

def compute_prob(n_Trials, numObserved):
    p = 0.5
    combinatorial = math.factorial(numObserved)/(math.factorial(numObserved-n_Trials)*math.factorial(n_Trials))
    bernoulli = p**(n_Trials)*((1-p)**(numObserved-n_Trials))
    binomial = combinatorial*bernoulli
    return binomial

from scipy.stats import binom

def compute_prob2(n_Trials, numObserved):
    fair = 0.5
    chance = binom.pmf(k=n_Trials, n=numObserved, p=fair)
    return chance




