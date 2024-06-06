import random
import matplotlib.pyplot as plt

def roll_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1 + die2

def monte_carlo_simulation(num_rolls):
    results = [0] * 13  # Можливі суми від 2 до 12

    for _ in range(num_rolls):
        result = roll_dice()
        results[result] += 1

    probabilities = [count / num_rolls for count in results]
    return probabilities

def plot_probabilities(probabilities):
    sums = range(2, 13)
    plt.bar(sums, probabilities[2:13], color='skyblue')
    
    for i, prob in enumerate(probabilities[2:13], start=2):
        plt.text(i, prob, f'{prob:.4f}', ha='center', va='bottom')

    plt.xlabel('Сума чисел на кубиках')
    plt.ylabel('Ймовірність')
    plt.title('Ймовірності сум при киданні двох кубиків (Метод Монте-Карло)')
    plt.show()

if __name__ == "__main__":
    num_rolls = 100000  # Кількість кидків
    probabilities = monte_carlo_simulation(num_rolls)
    plot_probabilities(probabilities)
