# Amirhossein Ghaffarzadeh
# 120734223
# aghaffarzadeh@myseneca.ca
# 2024-02-03


def isPrime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

def getPrimeNumbers(n):
    return [x for x in range(2, n+1) if isPrime(x)]

n = 20
prime_numbers = getPrimeNumbers(n)
print(f"Prime numbers between 2 and {n}: {prime_numbers}")


# -------------------------



import matplotlib.pyplot as plt
def graphSnowfall(t):
    ranges = {
        '0-10': 0,
        '11-20': 0,
        '21-30': 0,
        '31-40': 0,
        '41-50': 0
    }

    with open(t, 'r') as file:
        for line in file:
            snowfall = int(line.strip())

            if 0 <= snowfall <= 10:
                ranges['0-10'] += 1
            elif 11 <= snowfall <= 20:
                ranges['11-20'] += 1
            elif 21 <= snowfall <= 30:
                ranges['21-30'] += 1
            elif 31 <= snowfall <= 40:
                ranges['31-40'] += 1
            elif 41 <= snowfall <= 50:
                ranges['41-50'] += 1

    labels = list(ranges.keys())
    values = list(ranges.values())

    plt.figure(figsize=(10, 6))
    plt.bar(labels, values, color='skyblue')
    plt.xlabel('Snowfall Range (cm)')
    plt.ylabel('Occurrences')
    plt.title('Snowfall Accumulation Ranges')
    plt.show()


# -------------------------


def wordCount(t):
    word_dict = {}

    with open(t, 'r') as file:
        for line_num, line in enumerate(file, 1):
            clean_line = ''.join(char.lower() if char.isalnum() or char.isspace() else ' ' for char in line)
            words = clean_line.split()

            for word in words:
                if word in word_dict:
                    word_dict[word].append(line_num)
                else:
                    word_dict[word] = [line_num]

    return word_dict


# -------------------------


def stats_decorator(func):
    def wrapper(*args, **kwargs):
        numbers = func(*args, **kwargs)
        if numbers:
            print("Numbers read:", numbers)
            print("Count of numbers read:", len(numbers))
            print("Average of the numbers:", sum(numbers) / len(numbers))
            print("Maximum of the numbers:", max(numbers))
        else:
            print("No numbers read.")
        return numbers
    return wrapper

@stats_decorator
def process_line(line):
    numbers = [int(item) for item in line.split() if item.isdigit()]
    return numbers

def printStats(t):
    with open(t, 'r') as file:
        for line in file:
            process_line(line)


# -------------------------
            


Approach 1:
Uses a function doubleL(n) to make a list where each number from 0 to n-1 is doubled. 
It does this by adding each doubled number to a list and then giving back this list.


Approach 2:
Does something similar but in a shorter way using a list comprehension,
 which makes the list of doubled numbers directly. 


Approach 3:
Has a function doubleG(n) that is a bit different because
it doesn't make a list all at once. Instead, it gives out each doubled number one by one when asked.


The function doubleG(n) is called a generator function. It's good because it doesn't use as much memory.
Instead of making a whole list at once, it gives each doubled number when needed. 
This is especially helpful when dealing with a lot of numbers because it saves memory.