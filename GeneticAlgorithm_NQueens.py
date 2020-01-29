import random
import numpy as np

#Number of boards in each generation
POP_SIZE = 10
#Number of parent boards being selected for reproduction
SEL_FAC = 5
#Number of queens
QUEENS = 8
#Probability of mutation
MUT_PROB = 0.01
#Max number of non attacks, counting the number of non attacking pairs
NON_ATTACKS = 28

#Calculates the fitness of the chromosome entered
def fitnessFunc(c):
    attacks = 0

    #Calculate the diagonal attacks
    for i in range(len(c)):
        for j in range(len(c)):
            if (i != j):
                d1 = abs(i-j)
                d2 = abs(c[i] - c[j])
                if (d1 == d2):
                    attacks = attacks + 1

    #Calculate the row or column attacks
    rowColAttack = abs(len(c) - len(np.unique(c)))

    attacks = attacks + rowColAttack
    totalAttacks = 28 - attacks
    return totalAttacks

#Function used to shuffle genes before using in algorithm
def shuffle(x, y):
    for i in range(x):
        a = random.randint(0, len(y)-1)
        b = random.randint(0, len(y)-1)
        y[a], y[b] = y[b], y[a]
    return y

#Selects the most fit parents for reproduction
def selectParent(population, fitnessFunc):
    fitness = 0
    fitnessTotal = []
    parent = []
    for i in range(len(population)):
        fitness += fitnessFunc(population[i])
        fitnessTotal.append(fitness)
    check = random.uniform(0, fitnessTotal[-1])
    for i in range(len(population)):
        if fitnessTotal[i] > check:
            return population[i];

#Crossover is implemented to created 2 children
def crossoverFunc(p1,p2):
    n = len(p1)
    cp = random.randint(1,n)
    child = []
    child.extend(p1[0:cp])
    child.extend(p2[cp:])
    fitnessFunc(child)
    return child

#Mutation is done if probability is met
def mutationFunc(child):
    #If random number is below mutation probability, child goes under mutation by a gene being altered
    if(random.random < MUT_PROB):
        n1 = random.randint(0,8)
        n2 = random.randint(0,8)
        temp =child[n1]
        child[n1] = child[n2];
    return child

#Genetic algorithm is ran
def geneticAlgo(population, fitness):
    #Number of generations
    n=5000
    while n > 0:
        #Variable for updated population
        update_population = []
        for i in range(len(population)):
            #Two chromosomes are selected as parents
            x=selectParent(population,fitnessFunc)
            y=selectParent(population,fitnessFunc)
            #Parent chromosomes used in crossover function
            child = crossoverFunc(x,y)
            mutationFunc(child)
        if fitnessFunc(child) == NON_ATTACKS:
            print child
            return child
        update_population.append(child)
        population = update_population
        n = n -1

    return None


#Running the program
population = []
initial_pop = range(QUEENS)
for i in range(10):
    population.append(shuffle(5,initial_pop))
geneticAlgo(population, fitnessFunc)