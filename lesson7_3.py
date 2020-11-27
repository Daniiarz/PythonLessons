import wikipedia

wikipedia.set_lang("ru")

while 1:
    search = input('Что искать? ')

    results = wikipedia.search(search)
    for i in range(len(results)):
        print(i+1, results[i])

    option = int(input('Выберте вариант: '))
    summary = wikipedia.summary(results[option - 1])
    print(summary)
