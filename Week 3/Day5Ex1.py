# Problem
# - A desease affects 1% of the population
# - A test is 95% accurate for deseased individuals and 90% accurate for non-deseased individuals
# = Find the probability of having the desease given that the test result 

def bayes_theorem(prior, sensitivity, specificity):
    evidence = (sensitivity*prior) + ((1-specificity)*(1-prior))
    posterior = (sensitivity*prior)/evidence
    return posterior

prior = 0.01 # 1% prevalence
sensitivity = 0.95 # true positive rate
specificity = 0.90 # true negative rate
posterior = bayes_theorem(prior, sensitivity, specificity)
print("Probability of Disease Given Positive Test: ", posterior)