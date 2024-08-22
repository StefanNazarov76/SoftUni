string = input()
n = int(input())

repeat_string = lambda string, n: string * n
result = repeat_string(string, n)

print(result)
