import random

def rouletteSelection(population):
    chosen = []
    genes = population.getPop()
    count = 0
    while (count < 2):
        temp = random.uniform(0, population.getFitnessProb())
        for gene in genes:
            range = gene.getRange()
            max = range[1]
            min = range[0]
            if temp < max and temp > min:
                if count == 0:
                    chosen.append(gene)
                    count += 1
                else:
                    if chosen[0] != gene:
                        chosen.append(gene)
                        count += 1
    return chosen
