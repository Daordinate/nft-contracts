from numpy import integer


def string_to_integer(input_string : str) -> (int) : 
    integer = int.from_bytes(input_string.encode(), byteorder="big")

    return integer




