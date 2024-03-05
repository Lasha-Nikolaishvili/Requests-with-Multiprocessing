import concurrent.futures

y = 5


def my_function(x):
    print(x * y)
    return x * x


def my_func(x):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(my_function, x)
        future1 = executor.submit(my_function, x)
    return future.result(), future1.result()


def main():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        future = executor.submit(my_func, 10)
        future1 = executor.submit(my_func, 10)
        print(future.result())
        print(future1.result())


print(__name__)
if __name__ == '__main__':
    main()

