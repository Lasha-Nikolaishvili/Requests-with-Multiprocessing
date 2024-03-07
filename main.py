import json
import multiprocessing
import concurrent.futures
import requests


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


def run_threads(thread_cnt, start_i, end_i, products_list):
    with concurrent.futures.ThreadPoolExecutor(max_workers=thread_cnt) as executor:
        executor.map(lambda index: fetch_product(index, products_list), range(start_i, end_i))


def run_processes(process_cnt):
    thread_cnt = 20
    intervals = [(x * thread_cnt + 1, (x + 1) * thread_cnt + 1) for x in range(process_cnt)]

    manager = multiprocessing.Manager()
    products = manager.list()

    with concurrent.futures.ProcessPoolExecutor(max_workers=process_cnt) as executor:
        futures = [executor.submit(run_threads, thread_cnt, start_i, end_i, products) for start_i, end_i in intervals]
        for future in concurrent.futures.as_completed(futures):
            future.result()

    return products


def main():
    process_cnt = 5

    products = run_processes(process_cnt)
    write_to_json_file(list(products))


if __name__ == '__main__':
    main()
