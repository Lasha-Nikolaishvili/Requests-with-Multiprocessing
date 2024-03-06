# Product Fetcher Program

The Product Fetcher Program is a Python application designed to concurrently fetch product information from a given API and save the data into a JSON file. It utilizes multiprocessing and multithreading to efficiently download product data from "https://dummyjson.com/products/" and demonstrates an advanced pattern for handling parallel HTTP requests in Python.

## Features

- Fetch product data concurrently using a combination of multiprocessing and multithreading.
- Write fetched data to a JSON file in a pretty-printed format.
- Error handling for HTTP request failures.

## Prerequisites

Before you run the Product Fetcher Program, ensure you have the following installed:
- Python 3.6 or higher
- `requests` library

You can install the project requirements using pip:

```bash
pip install -r requirements.txt
```

## Installation

No installation is needed. Simply clone or download this repository to your local machine.

```bash
git clone <repository-url>
```

## Usage

To run the program, navigate to the program's directory in your terminal and execute the following command:

```bash
python main.py
```

This will start the process of fetching product data concurrently. Once the data is fetched from the specified range of product IDs, it will be saved to a file named `products.json` in the same directory as the script.

### Configuration

You can adjust the number of processes used by modifying the `process_cnt` variable in the `main()` function. The default is set to 5 processes. Additionally, the number of threads per process is set to 20 by default in the `run_processes` function. Adjust these numbers based on your system's capabilities and the workload.

## Output

The output will be a file named `products.json` containing the fetched product information in JSON format. Each product information is appended as a separate dictionary in a list.

## Error Handling

The program handles HTTP request errors by printing an error message to the console including the incorrect status code received. Products that fail to fetch will not be included in the output file.