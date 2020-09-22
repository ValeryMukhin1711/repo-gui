"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и
считывающую построчно данные. При этом английские числительные должны
заменяться на русские. Новый блок строк должен записываться в новый
текстовый файл.
"""

print("Start")
f = open("task_file_4.txt",'r')
f_out =open("task_file_4_out.txt",'w+')
lines = f.readlines()
print(lines)
for i in lines:
#    print("i = " + i)
    s_1= i.replace("One","Odin")
    s_2= s_1.replace("Two","Dva")
    s_3= s_2.replace("Three","Tree")
    s_4= s_3.replace("Four","Chetyre")
    f_out.write(s_4)
    print ("string = " + s_4,end="")
#d_1 = lines.replace("One","Odin")
'''
d_2 = d_1.replace("Two","Dva")
d_3 = d_2.replace("Three","Tree")
d_1 = d_3.replace("Four","Chetyre")
'''
"""
lines = data.split('\n')

lines_out =""

for i in lines:
    print(i)
    l_1 = i.replace("One","Odin")
    print(l_1)
    lines_out += l_1 +'\n'
    print("lines_out ",end='')
    print(lines_out)
print("lines[0] ",end="")

#new_line = lines[0].replace("One","")
#print(lines[0])
#print(new_line)
print(lines)
words = data.split()
print(words)
data.replace("O",'Y')
#line.replace(line[-1],'')
print(data)

f_out.write(d_1)
f_out.seek(0)
"""
print("\nRead from file\n")
f_out.seek(0)
data_n = f_out.read()
print(data_n)

f.close()
f_out.close()


print("Stop")
