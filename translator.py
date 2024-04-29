# a -> @
# A -> 4
# B, b -> 8
# E, e -> 3
# I, i -> !
# L, l -> 1
# O, o -> 0
# S, s -> 5

leet = {
    "a" : "@",
    "A" : "4",
    "B" : "8",
    "b" : "8",
    "E" : "3",
    "e" : "3",
    "I" : "!",
    "i" : "!",
    "L" : "1",
    "l" : "1",
    "O" : "0",
    "o" : "0",
    "S" : "5",
    "s" : "5"
}

def convert(text: str) -> str:
    next_letter = ""
    leet_letter = ""
    for i in leet:
        next_letter = i
        leet_letter = leet[i]
        text = text.replace(next_letter, leet_letter, -1)
    return print(text)
        




convert("lambda, and a better swoop through the end of all time so you ought to watch out. a,A,B,b,E,e,I,i,L,l,O,o,S,s")




