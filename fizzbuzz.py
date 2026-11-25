def fizzbuzz(n):
    for i in range(1, n + 1):
        if i % 5 == 0:
            print("Buzz")
        else:
            print(i)


if __name__ == "__main__":
    fizzbuzz(int(input("N: ")))
