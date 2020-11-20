tasks = [["Name", "Price", "Data", 'Done'],
         ["Name", "Price", "Data", "Not"],
         ["Name", "Price", "Data", "Not"],
         ]



for i in range(len(tasks)):
    print(i+1 ,tasks[i])


choice = int(input())

tasks[choice-1][3] = "Done"

for i in range(len(tasks)):
    print(i+1 ,tasks[i])

