"""
5. Создать (программно) текстовый файл, записать в него
программно набор чисел, разделенных пробелами. Программа
должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

f = open("task_file_5.txt","w+")
inp ="a"
while inp !="" and inp !='\n':
    inp = input("Input number ")
    try:
        number = int(inp)
        f.write(inp + " ")
    except:
        if inp !="":
            print(inp + " not number")
f.seek(0)        
data =f.read()
item = data.split()
sum = 0
for i in item:
    sum += int(i)
print(sum)
f.close()
