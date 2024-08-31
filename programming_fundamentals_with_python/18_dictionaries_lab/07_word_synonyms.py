n = int(input())

synonyms = {}

for _ in range(n):
    word = input()
    synonym = input()

    if word in synonyms:
        synonyms[word].append(synonym)
    else:
        synonyms[word] = [synonym]

for word in synonyms.keys():
    synonym_list = ', '.join(synonyms[word])
    print(f'{word} - {synonym_list}')
