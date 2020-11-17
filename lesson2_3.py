bank_account = (1, 2, 3, 4, 5)
print(bank_account[4])

glossary = {'set': ["Установить", "Множетва", "Партия"],
            "apple": "Яблоко", 1: "Один"}

glossary['set'].append("Новой значене")
print(glossary['apple'])
print(glossary['set'])
print(glossary[1])


unique_numbers = {"a", "a", 1, 1, 1, 1, 1, 1, 1, 2}
unique_numbers.add(9)
print(unique_numbers)


for i in range(50, 101):
    print(i)
