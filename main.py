import json
import multiprocessing
import concurrent.futures
import requests
import time


def write_to_json_file(products_list):
    print(__name__, products_list)
    json_object = json.dumps(products_list, indent=4)
    with open('products.json', 'w') as products_json:
        products_json.write(json_object)


def fetch_product(index, products_list):
    r = requests.get(f'https://dummyjson.com/products/{index}')
    if r.status_code == 200:
        products_list.append(r.json())
    else:
        print(f'ERROR: Incorrect status code! Status Code: {r.status_code}')


def run_threads(start_i, end_i, products_list):
    print('in threads')
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        executor.map(lambda index: fetch_product(index, products_list), range(start_i, end_i))


def run_processes():
    intervals = [(1, 21), (21, 41), (41, 61), (61, 81), (81, 101)]
    print('in process')

    # Create a Manager object
    manager = multiprocessing.Manager()

    # Create a shared list using the Manager
    products = manager.list()

    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(run_threads, start_i, end_i, products) for start_i, end_i in intervals]
        for future in concurrent.futures.as_completed(futures):
            future.result()

    return products


def main():
    start = time.perf_counter()
    products = run_processes()
    write_to_json_file(list(products))

    end = time.perf_counter()
    print(f'Time taken in seconds: {end - start}')


print(__name__)


if __name__ == '__main__':
    main()
