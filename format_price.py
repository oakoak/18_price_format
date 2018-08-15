import argparse


def get_zero(int_part):
    if int_part % 1000 < 100 and int_part // 1000 > 0:
        if int_part % 1000 < 10:
            return " 00"
        else:
            return " 0"
    if int_part // 1000 > 0:
        return " "
    return ""


def format_fraction_part(fraction_part_str):
    fraction_part = int(fraction_part_str)
    if fraction_part != 0:
        nice_fraction_part = "." + "0" * (len(fraction_part_str) -
                                          len(str(fraction_part)))
        while fraction_part % 10 == 0:
            fraction_part //= 10
        nice_fraction_part += str(fraction_part)
        return nice_fraction_part
    else:
        return ""


def format_price(price):
    if not isinstance(price, str):
        return None
    try:
        float(price)
    except ValueError:
        return None

    nice_price = ""
    parts_price = price.split(".")
    if parts_price[0] != "":
        int_part = int(parts_price[0])
    else:
        int_part = 0

    if len(parts_price) == 2 or price[0] == ".":
        nice_price += format_fraction_part(parts_price[-1])

    if int_part == 0:
        nice_price = "0" + nice_price

    while int_part != 0:
        nice_price = get_zero(int_part) + str(int_part % 1000) + nice_price
        int_part //= 1000
    return nice_price


def get_parse_argv():
    parser = argparse.ArgumentParser(
        description="Price formatter"
    )
    parser.add_argument(
        "price",
        help="Price"
    )
    return parser.parse_args()


if __name__ == '__main__':
    arguments = get_parse_argv()
    formatted_price = format_price(arguments.price)
    print(formatted_price)
