# COMMON BUILT-IN FUNCTIONS
#range()
# for i in range(3):
#     print(i)

#zip()
# names =["Esther", "Precious", "Kennie"]
# scores = [85, 90, 75]
# for n, s in zip(names, scores):
#     print(n, "scored", s)

#map()
# nums = [1, 2, 3, 4]
# squared = list(map(lambda x: x**2, nums))
# print(squared)

#filter()
# even_nums = list(filter(lambda x: x % 2 == 0, nums))
# print(even_nums)

#Student performance & Feedback system
# name1 = input("Enter first student name: ")
# name2 = input("Enter second student name: ")
# name3 = input("Enter Third student name: ")

# score1 = int(input("Enter score for " + name1 + ": "))
# score2 = int(input("Enter score for " + name2 + ": "))
# score3 = int(input("Enter score for " + name3 + ": "))

# names = [name1, name2, name3]
# scores = [score1, score2, score3]
# print("\nStudent Data")
# for index, (n, s) in enumerate(zip(names, scores)):
#     print(f"{index + 1}. {n} - {s}")

# total = sum(scores)
# average = round(total / len(scores), 2)
# highest = max(scores)
# lowest = min(scores)

# print("\nPerformance Summary:")
# print("Total score:", total)
# print("Average Score:", average)
# print("Highest Score:", highest)
# print("Lowest Score:", lowest)

# ranked = sorted(zip(names, scores), reverse=True)
# print("\nRanking:")
# for rank, (score, name) in enumerate(ranked, 1):
#     print(f"{rank}. {name} - {score}")

# print("\nData Type Checks:")
# print("Type of names:", type(names))
# print("Type of scores:", type(scores))
# print("ID of names list:", id(names))
# print("ID of scores list:", id(scores))

# passing = list(filter(lambda s: s >= 50, scores))
# print("\nPassing Scores:", passing)

# upper_names = list(map(lambda n: n.upper(), names))
# print("\nUppercase Names:", upper_names)

# print("\nHelp on len():")
# help(len)


#USERDEFINED FUNCTION
#dEFINING A FUNCTION
# def greet():
#     print("Hello, Welcome to AI Fellowship") 

# greet()
# greet()
# greet()
#Function Arguments and Parameters
#Function with an argument - the placeholder
# def greet(name):
#     print("Hello", name, "welcome to python learning")

#calling with parameter- the actual name
# greet("Class rep")
# greet("Ridwan")

# When to use return, print() and yield keywords inside a function

# def greet(name):
#     print("Hello", name)

# result = greet("Esther")
# print("Result:", result)


#return
# def add(a, b):
#     return a + b
# result = add(4, 6)
# print("The sum is:", result)

#yield
def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1
for number in count_up_to(5) :
    print(number)