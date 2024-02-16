# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
contact = {}

for _ in range(n):
    key, val = input().split(" ")
    contact[key] = val

try:
    while True:
        user_input = input()
        if user_input in contact:
            print(f"{user_input}={contact[user_input]}")
        else:
            print("Not found")
except EOFError:
    pass
