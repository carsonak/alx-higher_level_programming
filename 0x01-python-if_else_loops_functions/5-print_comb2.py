#!/usr/bin/python3
for num in range(99):
    print(f"{num:0>2}", end=", ")
else:
    print(f"{num + 1:0>2}")
