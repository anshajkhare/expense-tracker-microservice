
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
$ python -m unittest discover tests -p '*_test.py'
```

Code Coverage:
```bash
$ coverage run --source=expense_service --branch -m unittest discover tests -p '*_test.py'
```

After running tests with code coverage, you can get the report
```bash
$ coverage report
Name                                  Stmts   Miss Branch BrPart  Cover
-----------------------------------------------------------------------
expense_service/__init__.py               2      0      0      0   100%
expense_service/service.py               23      1      0      0    96%
expense_service/tornado/__init__.py       0      0      0      0   100%
expense_service/tornado/app.py           83      4      8      3    92%
expense_service/tornado/server.py        41     41      2      0     0%
-----------------------------------------------------------------------
TOTAL                                   149     46     10      3    68%
```

Static Type Checker
```bash
$ mypy ./expense_service ./tests
```

Linter
```bash
$ flake8 ./expense_service ./tests
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

