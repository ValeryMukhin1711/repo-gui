"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна
содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а
также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли
ее не включать.
Далее реализовать список. Он должен содержать словарь с
фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""

import json
print("Start\n")

my_list =[]
my_dict ={}
f=open('task_file_7.txt','r')
lines = f.readlines()

#print(s)
sum_avg = 0
num_avg = 0
for i in lines:
    k = i.split()
#    print(k)
    f_name = k[0]
    f_income = k[2]
    f_expenses = k[3]
    f_revenue = int(f_income) - int(f_expenses)
    print("revenue for " + k[0] +  " " + str(f_revenue))
    if f_revenue > 0:
        sum_avg +=f_revenue
        num_avg +=1

    temp = {f_name : f_revenue}
#    print(b)
    my_dict.update(temp)
my_list.append(my_dict)
print("average_profit "  + str(sum_avg/num_avg))
temp = {"average_profit" : sum_avg/num_avg}
my_list.append(temp)
print("\nDict firms with profit ")
print(my_dict)
print("\nList dict firms & dict profit ")      
print(my_list)
json_str = json.dumps(my_list)
print("json_str ")
print(json_str)

print("\nStop")
 
