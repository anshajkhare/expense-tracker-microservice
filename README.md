
# Expense Tracker Microservice

A microservice which can support an expense tracking application.




## Installation

Get the source code

```bash
  $ git clone https://github.com/anshajkhare/expense-tracker-microservice.git
  $ cd expense-tracker-microservice
```

Setup Virtual Environment:
```bash
$ python3 -m venv .venv
$ source ./.venv/bin/activate
$ pip install --upgrade pip
$ pip3 install -r requirements.txt
```
## Running Tests

To run tests, run the following command

```bash
  python -m unittest discover tests -p '*_test.py'
```

Code Coverage:
```bash
$ coverage run --source=addrservice --branch -m unittest discover tests -p '*_test.py'
```

Static Type Checker
```bash
$ mypy ./addrservice ./tests
```

Linter
```bash
$ flake8 ./addrservice ./tests
```

## API Reference

#### Get all expenses

```http
  GET /v1/expenses
```

#### Get an expense

```http
  GET /v1/expenses/{id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **[Required]** ID of expense to be fetched |

#### Create an expense

```http
  POST /v1/expenses
```

#### Update an expense

```http
  PUT /v1/expenses/{id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **[Required]** ID of expense to be updated |

#### Delete an expense

```http
  DELETE /v1/expenses/{id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **[Required]** ID of expense to be deleted |

