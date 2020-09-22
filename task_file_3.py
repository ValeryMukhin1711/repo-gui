"""
3. Создать текстовый файл (не программно), построчно
записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней
величины дохода сотрудников.
"""

 print("Start")
f = open("task_file_3.txt",'r')
my_dict ={}
line = "first"
while line !="" and line !='\n':
    line = f.readline()
    words = line.split()
    for i in words:
        try:
            sal = int(i)
        except:
            last_name = i
    b = {last_name : sal}
    my_dict.update(b)
#print(my_dict)
n_t = 0
s_t = 0
n = 0 # for sal < 20K
s = 0 # for sal < 20K
for i in my_dict:
    n_t +=1
    s_t +=my_dict[i]
    if my_dict[i] < 20000:
        n +=1
        s +=my_dict[i]

        print(i + " " + str(my_dict[i]))

print("Total average salary  - " + str(s_t/n_t))
print("Average salary for <20K  - " + str(s/n))
    

print("Stop")
