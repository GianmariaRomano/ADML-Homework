# Import the necessary libraries.
import math
import os
import random
import re
import sys
import textwrap
from collections import Counter, namedtuple
import calendar
import numpy

# 1 - Say "Hello, World!" With Python.
print("Hello, World!")

# 2 - Python If-Else.
if __name__ == '__main__':
    n = int(input().strip())
if n % 2 == 1:
    print("Weird")
else:
    if (2 <= n <= 5) or (n > 20):
        print("Not Weird")
    else:
        print("Weird")

# 3 - Arithmetic Operators.
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a + b)
    print(a - b)
    print(a * b)

# 4 - Python: Division.
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a // b)
    print(a / b)

# 5 - Loops.
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i ** 2)

# 6 - Write a Function.
def is_leap(year):
    leap = False
    
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
        else:
            leap = True
    
    return leap

year = int(input())
print(is_leap(year))

# 7 - Print Function.
if __name__ == '__main__':
    n = int(input())
s = ""
for i in range(1, n + 1):
    s += str(i)
print(s)

# 8 - List Comprehensions.
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    P = [[i] + [j] + [k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1)]
    p = [l for l in P if sum(l) != n]
    print(sorted(p))

# 9 - Find the Runner-Up Score!
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    M = max(arr)
    A = [i for i in arr if i != M]
    print(max(A))

# 10 - Nested Lists.
if __name__ == '__main__':
    students = []
    names = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name] + [score])
        names.append(name)
        scores.append(score)
    s_min = min(scores)
    Scores = sorted([s for s in scores if s != s_min])
    target = Scores[0]
    targets = []
    for student in students:
        if student[1] == target:
            targets.append(student[0])
    to_print = sorted(targets)
    for el in to_print:
        print(el)

# 11 - Finding the Percentage.
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    if query_name in student_marks:
        grades = student_marks[query_name]
        gpa = sum(grades) / len(grades)
        print(f"{gpa:.2f}")
    else:
        print(f"Student {query_name} not found.")

# 12 - Word Order.
n = int(input())
words = {}
for _ in range(n):
    word = input()
    words[word] = words.get(word, 0) + 1
print(len(words.keys()))
print(" ".join([str(v) for v in words.values()]))

# 13 - Tuples.
if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    t = tuple(integer_list)
    H = hash(t)
    print(H)

# 14 - sWAP cASE.
def swap_case(s):
    S = ""
    for c in s:
        if c.isalpha():
            if c.islower():
                S += c.upper()
            else:
                S += c.lower()
        else:
            S += c
    return S

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

# 15 - String Split and Join.
def split_and_join(line):
    return "-".join(line.split(" "))

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

# 16 - What's Your Name?
def print_full_name(first, last):
    print(f"Hello {first_name} {last_name}! You just delved into python.")

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)

# 17 - Mutations.
def mutate_string(string, position, character):
    return string[:position] + character + string[position+1:]

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

# 18 - Find a String.
def count_substring(string, sub_string):
    occurrences = 0
    for i in range(len(string) - len(sub_string) + 1):
        if string[i:i+len(sub_string)] == sub_string:
            occurrences += 1
    return occurrences

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

# 19 - String Validators.
if __name__ == '__main__':
    s = input()
    alnum = False
    alpha = False
    digit = False
    lower = False
    upper = False
    for c in s:
        if c.isalnum():
            alnum = True
            if c.isalpha():
                alpha = True
                if c.islower():
                    lower = True
                elif c.isupper():
                    upper = True
            elif c.isdigit():
                digit = True
    print(alnum)
    print(alpha)
    print(digit)
    print(lower)
    print(upper)

# 20 - Text Wrap
def wrap(string, max_width):
    return textwrap.fill(string, max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

# 21 - The Minion Game.
def minion_game(string):
    kevin = 0
    stuart = 0
    # Since generating substrings gives a runtime error, see each letter and check who gets points for those substrings.
    for i in range(len(string)):
        if string[i] in "AEIOU":
            kevin += len(s) - i
        else:
            stuart += len(s) - i
    # See who wins.
    if kevin > stuart:
        print(f"Kevin {kevin}")
    elif kevin < stuart:
        print(f"Stuart {stuart}")
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)

# 22 - Introduction to Sets.
def average(array):
    s = set(array)
    a = sum(s) / len(s)
    return round(a, 3)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

# 23 - No Idea!
n, m = list(map(int, input().split()))
arr = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))
happiness = 0
for el in arr:
    if el in A:
        happiness += 1
    elif el in B:
        happiness -= 1
print(happiness)

# 24 - Symmetric Difference.
A = set(map(int, input().split()))
N = int(input())
B = set(map(int, input().split()))
X = sorted(list(A ^ B)) # Do symmetric difference, convert to list and sort.
for x in X:
    print(x)

# 25 - Set .add().
N = int(input())
countries = set()
for _ in range(N):
    country = input()
    countries.add(country)
print(len(countries)) # Alternatively, use a counter.

# 26 - Set .discard(), .remove() & .pop().
n = int(input())
s = set(map(int, input().split()))
N = int(input())
for _ in range(N):
    command = input().split() # Either "pop", "discard x" or "remove x".
    if command[0] == "pop":
        s.pop()
    elif command[0] == "discard":
        s.discard(int(command[1]))
    elif command[0] == "remove":
        s.remove(int(command[1]))
print(sum(s))

# 27 - Set .union() Operator.
n = int(input())
N = set(map(int, input().split()))
b = int(input())
B = set(map(int, input().split()))
J = N | B
print(len(J))

# 28 - Set .intersection() Operator.
N = set(map(int, input().split()))
b = int(input())
B = set(map(int, input().split()))
J = N & B
print(len(J))

# 29 - Set .difference() Operator.
n = int(input())
N = set(map(int, input().split()))
b = int(input())
B = set(map(int, input().split()))
J = N - B
print(len(J))

# 30 - Set .symmetric_difference() Operator.
n = int(input())
N = set(map(int, input().split()))
b = int(input())
B = set(map(int, input().split()))
J = N ^ B
print(len(J))

# 31 - Set Mutations.
a = int(input())
A = set(map(int, input().split()))
N = int(input())
for _ in range(N):
    next_command = input().split() # Command and set length.
    next_set = set(map(int, input().split()))
    if next_command[0] == "update":
        A |= next_set
    elif next_command[0] == "intersection_update":
        A &= next_set
    elif next_command[0] == "difference_update":
        A -= next_set
    elif next_command[0] == "symmetric_difference_update":
        A ^= next_set
print(sum(A))

# 32 - The Captain's Room.
K = int(input())
arr = list(map(int, input().split()))
rooms = set(arr)
captain = ((sum(rooms) * K) - sum(arr)) // (K - 1)
print(captain)

# 33 - Check Subset.
T = int(input())
for _ in range(T):
    a = int(input())
    A = set(map(int, input().split()))
    b = int(input())
    B = set(map(int, input().split()))
    print(A - B == set())

# 34 - Check Strict Superset.
A = set(map(int, input().split()))
n = int(input())
check = True
for _ in range(n):
    N = set(map(int, input().split()))
    if not A > N:
        check = False
        break
print(check)

# 35 - Lists.
if __name__ == '__main__':
    N = int(input())
    lst = []
    for _ in range(N):
        command = input().split()
        if command[0] == "insert":
            lst.insert(int(command[1]), int(command[2]))
        elif command[0] == "print":
            print(lst)
        elif command[0] == "remove":
            lst.remove(int(command[1]))
        elif command[0] == "append":
            lst.append(int(command[1]))
        elif command[0] == "sort":
            lst.sort()
        elif command[0] == "pop":
            lst.pop()
        elif command[0] == "reverse":
            lst.reverse()

# 36 - Merge the Tools!
def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        substring = string[i:i+k]
        s = ""
        used = set()
        for c in substring:
            if c not in used:
                s += c
                used.add(c)
        print(s)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

# 37 - collections.Counter().
X = int(input())
shoes = Counter(list(map(int, input().split())))
N = int(input())
money = 0
for _ in range(N):
    shoe_size, cost = map(int, input().split())
    if shoes[shoe_size] != 0:
        money += cost
        shoes[shoe_size] -= 1
print(money)

# 38 - collections.namedtuple().
N = int(input())
Student = namedtuple('Student', input().split())
total = 0
for _ in range(N):
    student = Student(*input().split())
    total += int(student.MARKS)

print(total / N)

# 39 - Calendar Module.
date = list(map(int, input().split())) # [MM, DD, YYYY]
day = {0:"MONDAY", 1:"TUESDAY", 2:"WEDNESDAY", 3:"THURSDAY", 4:"FRIDAY", 5:"SATURDAY", 6:"SUNDAY"} # Convention used by calendar.
print(day[calendar.weekday(date[2], date[0], date[1])])

# 40 - Exceptions.
T = int(input())
for _ in range(T):
    a, b = input().split()
    try:
        print(int(a) // int(b))
    except ZeroDivisionError as e:
        print("Error Code:", e)
    except ValueError as e:
        print("Error Code:", e)

# 41 - Arrays.
def arrays(arr):
    return numpy.array(arr[::-1], float)

arr = input().strip().split(' ')
result = arrays(arr)
print(result)

# 42 - Shape and Reshape.
nums = input().strip().split(" ")
arr = numpy.array(nums, int)
print(numpy.reshape(arr, (3, 3)))

# 43 - Transpose and Flatten.
a = []
N, M = list(map(int, input().split()))
for _ in range(N):
    row = list(map(int, input().split()))
    a.append(row)
A = numpy.array(a)
print(numpy.transpose(A))
print(A.flatten())

# 44 - Concatenate.
a = []
b = []
N, M, P = list(map(int, input().split()))
for _ in range(N):
    a.append(list(map(int, input().split())))
for _ in range(M):
    b.append(list(map(int, input().split())))
A = numpy.array(a)
B = numpy.array(b)
print(numpy.concatenate((A, B)))

# 45 - Zeros and Ones.
dims = tuple(map(int, input().split()))
print(numpy.zeros(dims, dtype=int))
print(numpy.ones(dims, dtype=int))

# 46 - Eye and Identity.
# numpy.set_printoptions(legacy='1.13') # If needed to have the correct solution.

N, M = list(map(int, input().split()))
print(numpy.eye(N, M))

# 47 - Array Mathematics.
a = []
b = []

N, M = list(map(int, input().split()))
for _ in range(N):
    a.append(list(map(int, input().split())))
for _ in range(N):
    b.append(list(map(int, input().split())))

A = numpy.array(a)
B = numpy.array(b)

print(numpy.add(A, B))
print(numpy.subtract(A, B))
print(numpy.multiply(A, B))
print(A // B)
print(numpy.mod(A, B))
print(numpy.power(A, B))

# 48 - Map and Lambda Function.
cube = lambda x: x**3

def fibonacci(n):
    if n == 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        l = [0, 1, 1]
        for _ in range(3, n):
            l.append(l[-1] + l[-2])
        return l

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))

# 49 - Validating Email Addresses With a Filter.
def fun(s):
    try:
        username, rest = s.split("@")
        website, extension = rest.split(".")
    except ValueError:
        return False
    if (not username) or (not website) or (not extension):
        return False
    if not all(c.isalnum() or c in "-_" for c in username):
        return False
    if not website.isalnum():
        return False
    if not extension.isalpha() or len(extension) > 3:
        return False
    return True

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)

# 50 - Sum and Prod.
a = []
N, M = tuple(map(int, input().split()))
for _ in range(N):
    a.append(list(map(int, input().split())))
A = numpy.array(a)
S = numpy.sum(A, axis=0)
P = numpy.prod(S)
print(P)

# 51 - Floor, Ceil and Rint.
# numpy.set_printoptions(legacy='1.13') # If needed to have the correct solution.

A = numpy.array(list(map(float, input().split())))
print(numpy.floor(A))
print(numpy.ceil(A))
print(numpy.rint(A))

# 52 - Min and Max.
a = []
N, M = tuple(map(int, input().split()))
for _ in range(N):
    a.append(list(map(int, input().split())))
A = numpy.array(a)
m = numpy.min(A, axis=1)
M = numpy.max(m)
print(M)

# 53 - Mean, Var and Std.
# numpy.set_printoptions(legacy='1.13') # If needed to have the correct solution.
a = []
N, M = tuple(map(int, input().split()))
for _ in range(N):
    a.append(list(map(int, input().split())))
A = numpy.array(a)
print(numpy.mean(A, axis=1))
print(numpy.var(A, axis=0))
print(round(numpy.std(A), 11))

# 54 - Dot and Cross.
a = []
b = []
N = int(input())
for _ in range(N):
    a.append(list(map(int, input().split())))
for _ in range(N):
    b.append(list(map(int, input().split())))
A = numpy.array(a)
B = numpy.array(b)
C = numpy.dot(A, B)
print(C)

# 55 - Inner and Outer.
A = numpy.array(list(map(int, input().split())))
B = numpy.array(list(map(int, input().split())))
print(numpy.inner(A, B))
print(numpy.outer(A, B))

# 56 - Polynomials.
P = numpy.array(list(map(float, input().split())))
x = float(input())
y = numpy.polyval(P, x)
print(y)

# 57 - Linear Algebra.
a = []
N = int(input())
for _ in range(N):
    a.append(list(map(float, input().split())))
A = numpy.array(a)
D = numpy.linalg.det(A)
print(round(D, 2))

# Challenge 1 - Birthday Cake Candles.
    frequencies = {}
    for candle in candles:
        frequencies[candle] = frequencies.get(candle, 0) + 1
    tallest = max(frequencies, key=frequencies.get)
    return frequencies[tallest]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()

# Challenge 2 - Number Line Jumps.
def kangaroo(x1, v1, x2, v2):
    # Goal: Check whether there exists some j such that x1 + (v1 x j) = x2 + (v2 x j).
    # This means that j = (x2 - x1) / (v1 - v2)
    if (v1 > v2) and (x2 - x1) % (v1 - v2) == 0:
        return "YES"
    else:
        return "NO"
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()

# Challenge 3 - Viral Advertising.
def viralAdvertising(n):
    people_reached = 5 # By default.
    cumulative_likes = 0
    for i in range(n):
        likes = people_reached // 2
        cumulative_likes += likes
        people_reached = (3 * likes)
    return cumulative_likes

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()

# Challenge 4 - Recursive Digit Sum.
def superDigit(n, k):
    S = sum([int(i) for i in n]) * k
    if S < 10:
        # Single digit.
        return S
    return superDigit(str(S), 1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()

# Challenge 5 - Insertion Sort (Part 1).
def insertionSort1(n, arr):
    to_insert = arr[n - 1]
    idx = n - 1
    while idx > 0 and to_insert < arr[idx - 1]:
        arr[idx] = arr[idx - 1]
        idx -= 1
        print(*arr, sep = " ")
    arr[idx] = to_insert
    print(*arr, sep = " ")

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)