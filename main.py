from panflute import *
import sys

headers = []


def text_filter(elem, doc):
    if isinstance(elem, Header):
        if stringify(elem) in headers:
            sys.stderr.write(
                    "Repeated header: " + stringify(elem) + "\n")
        else:
            headers.append(stringify(elem))

    if isinstance(elem, Header) and elem.level >= 3:
        return Header(Str(stringify(elem).upper()), level=elem.level)

    if type(elem) == Str:
        if str(elem.text) == "BOLD":
            name = [Str(elem.text)]
            return Strong(*name)


def main(doc=None):
    return run_filter(text_filter, doc=doc)


if __name__ == "__main__":
    main()
