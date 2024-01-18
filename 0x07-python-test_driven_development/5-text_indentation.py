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

    sn_txt = ""
    fwd = 0
    bck = 0
    while fwd >= 0 and bck < len(text) - 1:
        puncs = sorted([text.find(". ", fwd), text.find("? ", fwd),
                        text.find(": ", fwd)])
        for p_i in puncs:
            if p_i >= 0:
                fwd = p_i + 1
                break
        else:
            fwd = p_i
        if fwd < 0:
            sn_txt = sn_txt + text[bck:].lstrip() + "\n\n"
        else:
            sn_txt = sn_txt + text[bck:fwd].lstrip() + "\n\n"

        # Dealing with embedded whitespaces
        bck = 0
        while bck >= 0:
            wht_spc = sorted([sn_txt.find("  ", bck), sn_txt.find("\t", bck),
                              sn_txt.find("\n ", bck), sn_txt.find("\f", bck),
                              sn_txt.find("\r", bck)])
            for w_i in wht_spc:
                if w_i >= 0:
                    bck = w_i
                    break
            else:
                bck = w_i

            if bck > 0:
                sn_txt = sn_txt[:bck] + " " + sn_txt[bck:].lstrip()
        bck = fwd

    print(sn_txt.removesuffix("\n\n"), end="")


if __name__ == "__main__":

    text_indentation()
    """
    text_indentation(\"""Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
    Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? \
    Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: \
    Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere. \
    Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum \
    rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex illa a Dipylo \
    stadia confecimus. Sin aliud quid voles, postea. Quae animi affectio suum \
    cuique tribuens atque hanc, quam dico. Utinam quidem dicerent alium alio \
    beatiorem! Iam ruinas videres\""")
    """
