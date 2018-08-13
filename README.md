# Price Formatter
---
The script leads the price to a good view
---

## Description
+ Software Interfase - to use it on the site
+ Command Line Interface - to start in manual mode from the console project

## Example start from the console
```bash
python format_price.py 123456.7890
```

### Example result in console
```bash
123 456.789
```

## Example use script in your project
```python
from format_price import format_price

format_price(price)
```

## Example start tests
```bash
python -m unittest -v tests.py
```

### Results test
```bash
test_on_incorrect_price (tests.FormatPriceTestCase) ... ok
test_on_insignificant_zeros (tests.FormatPriceTestCase) ... ok
test_on_leading_zeros (tests.FormatPriceTestCase) ... ok
test_without_int_part (tests.FormatPriceTestCase) ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.003s

OK
```

## Requirements
```bash
Python ver 3.5 (or higher)
```

## Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
