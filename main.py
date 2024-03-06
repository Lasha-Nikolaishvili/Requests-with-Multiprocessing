import json
import threading
import concurrent.futures
import requests
import time


def write_to_json_file(products_list):
    json_object = json.dumps(products_list, indent=4)
    with open('products.json', 'w') as products_json:
        products_json.write(json_object)


def fetch_product(index, products_list):
    r = requests.get(f'https://dummyjson.com/products/{index}')

    if r.status_code == 200:
        products_list.append(r.json())
    else:
        print(f'ERROR: Incorrect status code! Status Code: {r.status_code}')


def run_threads(products_list):
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        executor.map(lambda index: fetch_product(index, products_list), range(1, 101))


def main():
    start = time.perf_counter()
    products = []

    run_threads(products)
    write_to_json_file(products)

    end = time.perf_counter()
    print(f'Time taken in seconds: {end - start}')


if __name__ == '__main__':
    main()
