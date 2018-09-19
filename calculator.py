from numpy import power

def add(value_1,value_2):
    return value_1 + value_2

def sub(value_1,value_2):
    return value_1 - value_2

def mult(value_1,value_2):
    return value_1 * value_2

def div(value_1,value_2):
    return value_1 / value_2

def floor(value_1,value_2):
    return value_1 // value_2

def pow_of(value_1,value_2):
    return power(value_1,value_2)

def modulo(value_1,value_2):
    return value_1 % value_2


operations = {
    "+": add,
    "-": sub,
    "*": mult,
    "/": div,
    "//": floor,
    "^": pow_of,
    "%": modulo,
}
