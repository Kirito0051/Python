def bayes_theorem(prior_prob, likelihood, evidence):
    
    posterior_prob = (likelihood * prior_prob) / evidence
    return posterior_prob

if __name__ == "__main__":

    prior_prob = float(input("enter prior probability :"))
    likelihood = float(input("enter likelihood :"))
    evidence = float(input("enter evidence:"))

    posterior_prob = bayes_theorem(prior_prob, likelihood, evidence)
    print("posterior posibility:", posterior_prob)
    
