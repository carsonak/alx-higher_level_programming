#!/usr/bin/python3
"""Module for text_indentation"""


def text_indentation(text):
    """
    Print text broken into lines

    Parameters:
        text (str): A block of text
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    sen_txt = ""
    fwd = 0
    bck = 0
    while fwd >= 0 and bck < len(text) - 1:
        puncs = sorted([text.find(".", fwd), text.find("?", fwd),
                        text.find(":", fwd)])
        for p_i in puncs:
            if p_i >= 0:
                fwd = p_i + 1
                break
        else:
            fwd = p_i
        if fwd < 0:
            sen_txt = sen_txt + text[bck:].lstrip() + "\n\n"
        else:
            sen_txt = sen_txt + text[bck:fwd].lstrip() + "\n\n"

        # Dealing with embedded whitespaces
        bck = 0
        while bck >= 0:
            wht_spc = sorted(
                [sen_txt.find("  ", bck), sen_txt.find("\t", bck),
                 sen_txt.find("\n ", bck), sen_txt.find("\f", bck),
                 sen_txt.find("\r", bck)]
            )
            for w_i in wht_spc:
                if w_i >= 0:
                    bck = w_i
                    break
            else:
                bck = w_i

            if bck > 0:
                sen_txt = sen_txt[:bck] + " " + sen_txt[bck:].lstrip()
        bck = fwd

    print(sen_txt.rstrip(), end="")
