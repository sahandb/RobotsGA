#imports
import numpy as np
import matplotlib.pyplot as plt
import random
from copy import deepcopy
#import robby
#rw = robby.World(10, 10)

#cans number
soda_cans_position = np.random.randint(0,9,[20,2])
#population number 
population = np.random.randint(0,6,[200,243])
fit_sum_list = list()
mean_fit_sum_list = list()

#selection
def selection(roulette,n):
    probabilities = list()
    for j in range(n):
        rand = random.random()
        for i in range(len(population)):
            if rand <= roulette[i]:
                probabilities.append(population[i])
                break
    return probabilities

#fittness function , how points evaluation
def fitness(population):
    population_fitness = list()
    for i in range(len(population)):
        point = 0
        robot = population[i]
        position = [0,0]
        for j in range(243):
            position, bend = movement(robot[j],position)
            if position[0] > 9:
                position[0] = 9
                point -= 5
            if position[1] > 9:
                position[1] = 9
                point -= 5
            if position[0] < 0:
                position[0] = 0
                point-= 5
            if position[1] <0 :
                position[1] = 0
                point -= 5
            if bend ==1:
                if position in soda_cans_position:
                    point += 10
                    bend -= 1
                else:
                    point -= 1
                    bend -= 1
        population_fitness.append(point)
    return population_fitness

#emcoding movements from 0 to 6 (state 5 just stay)
def movement(command,position):
    bend = 0
    if command == 0:
        position[0] += 1
    elif command == 1:
        position[1] += 1
    elif command == 2:
        position[0] -= 1
    elif command == 3:
        position[1] -= 1
    elif command == 4:
        randomMove = random.randint(0, 3)
        if randomMove == 0:
            position[0] += 1
        elif randomMove == 1:
            position[1] += 1
        elif randomMove == 2:
            position[0] -= 1
        elif randomMove == 3:
            position[1] -= 1
    elif command == 6:
        bend = 1
    return position, bend

#cossover one-point with random split
def crossover(parent1,parent2):
    split = random.randint(0,242)
    parent1 = deepcopy(parent1)
    parent2 = deepcopy(parent2)
    child1 = np.concatenate((parent1[0:split],parent2[split:]))
    child2 = np.concatenate((parent2[0:split] ,parent1[split:]))
    return child1, child2

#mutation less than 0.005 random
def mutation(a):
    for i in range(243):
        rand = random.random()
        if rand <= 0.005 :
            a[0][i] = random.randint(0,6)
    return a

#main algorithm
def GA(population, iter):
    parent_gen = population
    for i in range(iter):
        fit = fitness(parent_gen)
        fit_sum = float(sum(fit))

        mean_fit_sum = float(fit_sum/243)
        print("{}.{} {}".format(i+1 , "fitness :", fit_sum))
        #list for plot
        fit_sum_list.append(fit_sum)

        mean_fit_sum_list.append(mean_fit_sum)
        #Roulette Selection
        portion_fitness = [f / fit_sum for f in fit]
        roulette = [sum(portion_fitness[:i + 1]) for i in range(len(portion_fitness))]
        
        offspring = list()
        #crossover in algorithm
        for j in range(243):
            parent1,parent2 = selection(roulette,2)
            child1, child2 = crossover(parent1,parent2)
            offspring.append(child1)
            offspring.append(child2)
        #miutation in algorithm
        for j in range(243):
            parent = selection(roulette,1)
            child = mutation(parent)
            offspring.append(child)
        
#main     
GA(population,700)

#plot
plt.plot(range(700), fit_sum_list)
plt.show()

plt.plot(range(700), mean_fit_sum_list)
plt.show()


#plt.plot(range(243), pop[0])
#plt.plot(range(200), pop[1])
#plt.show()

#plt.plot(range(100), np.log(fit_sum_list))
#plt.show()