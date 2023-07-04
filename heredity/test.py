#{'Harry': {'name': 'Harry', 'mother': 'Lily', 'father': 'James', 'trait': None}, 
# 'James': {'name': 'James', 'mother': None, 'father': None, 'trait': True}, 
# 'Lily': {'name': 'Lily', 'mother': None, 'father': None, 'trait': False}}

# {'Arthur': {'name': 'Arthur', 'mother': None, 'father': None, 'trait': False}, 
# 'Charlie': {'name': 'Charlie', 'mother': 'Molly', 'father': 'Arthur', 'trait': False}, 
# 'Fred': {'name': 'Fred', 'mother': 'Molly', 'father': 'Arthur', 'trait': True}, 
# 'Ginny': {'name': 'Ginny', 'mother': 'Molly', 'father': 'Arthur', 'trait': None}, 
# 'Molly': {'name': 'Molly', 'mother': None, 'father': None, 'trait': False}, 
# 'Ron': {'name': 'Ron', 'mother': 'Molly', 'father': 'Arthur', 'trait': None}}

# {'Arthur': {'name': 'Arthur', 'mother': None, 'father': None, 'trait': False}, 
# 'Hermione': {'name': 'Hermione', 'mother': None, 'father': None, 'trait': False}, 
# 'Molly': {'name': 'Molly', 'mother': None, 'father': None, 'trait': None}, 
# 'Ron': {'name': 'Ron', 'mother': 'Molly', 'father': 'Arthur', 'trait': False}, 
# 'Rose': {'name': 'Rose', 'mother': 'Ron', 'father': 'Hermione', 'trait': True}}
from heredity import joint_probability

# people = {'Lily': {"mother": None, "father": None},
#           'James': {"mother": None, "father": None},
#           'Harry': {"mother": "Lily", "father": "James"}}
# one_gene = {'Harry'}
# two_genes = {'James'}
# have_trait = {'James'}

people = {'Lily': {"mother": None, "father": None},
          'James': {"mother": None, "father": None},
          'Harry': {"mother": "Lily", "father": "James"}}
one_gene = {'James'}
two_genes = {'Harry','Lily'}
have_trait = {'James', 'Lily'}

probabilities = {
        person: {
            "gene": {
                2: 0.1,
                1: 0.2,
                0: 0.1
            },
            "trait": {
                True: 0.2,
                False: 0.5
            }
        }
        for person in people
    }

p = joint_probability(people, one_gene, two_genes, have_trait)
# print(probabilities)
for person in probabilities:
    total = 0
    for i in range(3):
        total += probabilities[person]["gene"][i]
    factor = 1/total 
    for i in range(3):
        probabilities[person]["gene"][i] *= factor 

    total = 0
    for i in [True, False]:
        total += probabilities[person]["gene"][i]
    factor = 1/total 
    for i in [True, False]:
        probabilities[person]["gene"][i] *= factor
print(probabilities)  