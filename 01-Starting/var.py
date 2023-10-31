#!/usr/bin/env python3

def my_var():
    for i in [42, "42", "quarante-deux", 42.0, 42 == 42, [42], {42: 42}, (42,), set()]:
        print(f'{i} has a type {type(i)}')

if __name__ == "__main__":
    my_var()
