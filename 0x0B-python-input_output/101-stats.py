#!/usr/bin/python3
"""Module for logger"""


def logger():
    """
    Read lines from stdin and parse into statistics

    This function reads log lines from the standard input and extracts file
    size and status code information. It prints the cumlative size and how
    many times a particaular status code ahas been invoked every ten lines
    read or after keyboard interrupt.
    """

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
    """Return a string of keys in a dict whose values are greater than 0"""

    output = ""
    for k, v in stats.items():
        if v > 0:
            output += f"{k}: {v}\n"

    return output


if __name__ == "__main__":
    logger()
