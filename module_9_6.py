def all_variants(text):
    for x in range(len(text)):
        for n in range(len(text) - x):
            yield text[x:n + x+1]
a = all_variants("abc")
for i in a:
    print(i)