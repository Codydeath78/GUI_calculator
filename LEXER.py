import string
import re


def CutOneLineTokens(thing):
    full = ""
    thing_1 = ""
    thing_2 = ""
    thing_3 = ""
    thing_4 = ""
    key = re.match(r"\b(if|else|int|float)\b", thing)
    iden = re.match(r"[a-zA-Z0-9]\d", thing)
    op =  re.match(r"[=+>*/]", thing)
    lit = re.match(r"\b\d+\b", thing)
    if key:
         thing_1 = key.group()


    #iden = re.match(r"[a-zA-Z0-9]\d", thing)
    if iden:
        thing_2 = iden.group()


    if op:
        thing_3 = op.group()

    if lit:
        thing_4 = lit.group()
    #if re.match(r"\b(if|else|int|float)\b", thing):  # finished
        # print(f"{thing}: Keywords")
        #full = key = ("<key," + thing + ">")
   # if re.match(r"[a-zA-Z0-9]\d", thing):  # finished
        # print(f"{thing}: identifiers")
     #   full = iden = ("<iden," + thing + ">")
   # elif re.match(r"[=+>*/]", thing):  # finished \>
        # print(f"{thing}: operators")
    #    full = op = ("<op," + thing + ">")
   # elif re.match(r"\b\d+\b", thing):  # finished
        # print(f"{thing}: int literal")
      #  full = lit = ("<lit," + thing + ">")
   # elif re.match(r"[()\":;]", thing):  # finished
        # print(f"{thing}: separators")
      #  full = sep = ("<sep," + thing + ">")
    else:
        #print(f"{thing}: No specific pattern matched.")
         print("No match")

    #print("[" + key + iden + op + lit + "]")
    print("["+thing_1 +thing_2 +thing_3+thing_4+"]" )



if __name__ == '__main__':
    s = "int A1 = 5"
    CutOneLineTokens(s)
