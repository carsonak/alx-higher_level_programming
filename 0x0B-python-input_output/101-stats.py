#!/usr/bin/python3
""""""
import sys


def logger():
    """"""

    try:
        ln_cnt = 0
        total_size = 0
        stats = {"200": 0, "301": 0, "400": 0, "401": 0,
                 "403": 0, "404": 0, "405": 0, "500": 0}
        while True:
            line = input()
            s_code, f_size = line.rsplit(maxsplit=2)[-2:]
            total_size += int(f_size)
            if stats.get(s_code, None) is not None:
                stats[s_code] += 1

            ln_cnt += 1
            if not ln_cnt % 10:
                print(f"File size: {total_size}\n{get_codes(stats)}", end="")

    except KeyboardInterrupt:
        print(f"File size: {total_size}\n{get_codes(stats)}", end="")


def get_codes(stats: dict[str, int]):
    output = ""
    for k, v in stats.items():
        if v:
            output += f"{k}: {v}\n"

    return output


if __name__ == "__main__":
    logger()
