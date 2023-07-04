import csv
import itertools
import sys

PROBS = {

    # Unconditional probabilities for having gene
    "gene": {
        2: 0.01,
        1: 0.03,
        0: 0.96
    },

    "trait": {

        # Probability of trait given two copies of gene
        2: {
            True: 0.65,
            False: 0.35
        },

        # Probability of trait given one copy of gene
        1: {
            True: 0.56,
            False: 0.44
        },

        # Probability of trait given no gene
        0: {
            True: 0.01,
            False: 0.99
        }
    },

    # Mutation probability
    "mutation": 0.01
}


def main():

    # Check for proper usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python heredity.py data.csv")
    people = load_data(sys.argv[1])
    
    # Keep track of gene and trait probabilities for each person
    probabilities = {
        person: {
            "gene": {
                2: 0,
                1: 0,
                0: 0
            },
            "trait": {
                True: 0,
                False: 0
            }
        }
        for person in people
    }

    # Loop over all sets of people who might have the trait
    names = set(people)
    for have_trait in powerset(names):

        # Check if current set of people violates known information
        fails_evidence = any(
            (people[person]["trait"] is not None and
             people[person]["trait"] != (person in have_trait))
            for person in names
        )
        if fails_evidence:
            continue

        # Loop over all sets of people who might have the gene
        for one_gene in powerset(names):
            for two_genes in powerset(names - one_gene):

                # Update probabilities with new joint probability
                p = joint_probability(people, one_gene, two_genes, have_trait)
                update(probabilities, one_gene, two_genes, have_trait, p)

    # Ensure probabilities sum to 1
    normalize(probabilities)

    # Print results
    for person in people:
        print(f"{person}:")
        for field in probabilities[person]:
            print(f"  {field.capitalize()}:")
            for value in probabilities[person][field]:
                p = probabilities[person][field][value]
                print(f"    {value}: {p:.4f}")


def load_data(filename):
    """
    Load gene and trait data from a file into a dictionary.
    File assumed to be a CSV containing fields name, mother, father, trait.
    mother, father must both be blank, or both be valid names in the CSV.
    trait should be 0 or 1 if trait is known, blank otherwise.
    """
    data = dict()
    with open(filename) as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row["name"]
            data[name] = {
                "name": name,
                "mother": row["mother"] or None,
                "father": row["father"] or None,
                "trait": (True if row["trait"] == "1" else
                          False if row["trait"] == "0" else None)
            }
    return data


def powerset(s):
    """
    Return a list of all possible subsets of set s.
    """
    s = list(s)
    return [
        set(s) for s in itertools.chain.from_iterable(
            itertools.combinations(s, r) for r in range(len(s) + 1)
        )
    ]


def joint_probability(people, one_gene, two_genes, have_trait):
    """
    Compute and return a joint probability.

    The probability returned should be the probability that
        * everyone in set `one_gene` has one copy of the gene, and
        * everyone in set `two_genes` has two copies of the gene, and
        * everyone not in `one_gene` or `two_gene` does not have the gene, and
        * everyone in set `have_trait` has the trait, and
        * everyone not in set` have_trait` does not have the trait.
    """
    n_people = {person:[] for person in people}
    
    for person in people:
        if person in one_gene:
            n_people[person].append(1)
        elif person in two_genes:
            n_people[person].append(2)
        else:
            n_people[person].append(0)
        
        if person in have_trait:
            n_people[person].append(True)
        else:
            n_people[person].append(False)
    for person in people:
        if people[person]["father"] != None and people[person]["mother"] != None:
            n_people[person].append(n_people[people[person]["mother"]][0])
            n_people[person].append(n_people[people[person]["father"]][0])

    j_probability = 1
    for person in people:
        gene_value = n_people[person][0]
        trait_value = n_people[person][1]

        # has no parents
        if len(n_people[person]) == 2:
            gene = PROBS["gene"][gene_value]
            trait = PROBS["trait"][gene_value][trait_value]
            j_probability *= gene*trait
        
        # has parentss
        else:
            mother_value = n_people[person][2]
            father_value = n_people[person][3]
            trait = PROBS["trait"][gene_value][trait_value]
            # if he has one gene 
            if gene_value == 1:
                gene = prob(father_value) * (1 - prob(mother_value)) + prob(mother_value) * (1 - prob(father_value))
                j_probability *= gene*trait
            # if he has 2 genes
            elif gene_value == 2:
                gene = prob(father_value) * prob(mother_value)
                j_probability *= gene*trait
            # if he has 0 genes
            else:
                gene = (1-prob(father_value)) * (1-prob(mother_value))
                j_probability *= gene*trait

    return j_probability
    
def prob(n):
    if n == 0:
        return PROBS["mutation"]
    elif n == 1:
        return 0.5
    else:
        return (1 - PROBS["mutation"])


def update(probabilities, one_gene, two_genes, have_trait, p):
    """
    Add to `probabilities` a new joint probability `p`.
    Each person should have their "gene" and "trait" distributions updated.
    Which value for each distribution is updated depends on whether
    the person is in `have_gene` and `have_trait`, respectively.
    """
    for person in probabilities:
        if person in one_gene:
            gene = 1
        elif person in two_genes:
            gene = 2
        else:
            gene = 0
        
        trait = person in have_trait
        
        probabilities[person]["gene"][gene] += p
        probabilities[person]["trait"][trait] += p


def normalize(probabilities):
    """
    Update `probabilities` such that each probability distribution
    is normalized (i.e., sums to 1, with relative proportions the same).
    """
    for person in probabilities:
        total = 0
        for i in range(3):
            total += probabilities[person]["gene"][i]
        factor = 1/total 
        for i in range(3):
            probabilities[person]["gene"][i] *= factor 

        total = 0
        for i in [True, False]:
            total += probabilities[person]["trait"][i]
        factor = 1/total 
        for i in [True, False]:
            probabilities[person]["trait"][i] *= factor


if __name__ == "__main__":
    main()
