def count_sentences(text):
    i = 0
    h = 0
    lastindex = len(text)
    for i in range(0, lastindex, 1):
        if (text[i] == '!' or text[i] == '.' or text[i] == '?'):
            h += 1
        i += 1
    return h


def count_words(text):
    i = 0
    h = 1
    j = 0
    lastindex = len(text)
    for i in range(0, lastindex, 1):
        if (text[i].isspace()):
            h += 1
        i += 1
    return h


def count_letters(text):
    i = 0
    h = 0
    lastindex = len(text)
    for i in range(0, lastindex, 1):
        if (text[i].isalpha()):
            h += 1
        i += 1
    return h

# user imput


text = input('Text:')

# number of:

nletters = float(count_letters(text))
nwords = float(count_words(text))
nsentences = float(count_sentences(text))
print(nletters)
print(nwords)
print(nsentences)

# Putting it together

L = float((nletters / nwords) * 100)
S = float((nsentences / nwords) * 100)
index = float((0.0588 * L) - (0.296 * S) - 15.8)

if (int(round(index)) < 1):
    print("Before Grade 1\n")

elif (int(round(index)) > 15):
    print("Grade 16+\n")
else:
    print("Grade ", round(index), "\n")
