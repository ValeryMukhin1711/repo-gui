class Matrix:

    def __init__(self, l_list):
        self.l_list = l_list
                
    def __str__(self):
        st =""
        for i in self.l_list:
            
            for j in i:
                st = st +f"{j}\t"

            st = st + "\n"
        return st

    def __add__(self,other):

        l = len(self.l_list)

        list_out =[]
        i = 0
        while i  < l :

            list_t =[]
            l1 = len(self.l_list[i])
            k = 0
            while  k < l1 :

                 list_t = list_t + [self.l_list[i][k] + other.l_list[i][k]]
                  
                 k +=1

            list_out = list_out + [list_t]

            i +=1
        st =""
  
        return Matrix(list_out) #st    


my_list =[1,2,3,4,5]
my_list1 =[i for i in range(6,11)]
my_list2 =[i for i in range(11,16,)]

list_list =[my_list , my_list1, my_list2]

m1=Matrix(list_list)


my_l =[11,12,13,14,15]
my_l1 =[i for i in range(15,20)]
my_l2 =[i for i in range(80,90,2)]
list_list_1 =[my_l , my_l1, my_l2]

m2=Matrix(list_list_1)

print("print m1")
print(m1)
print("print m2")
print(m2)
print("print(m1 + m2}")
print(m1 +m2)

m3 = m1 + m2
print("m3 = m1 + m2")
print("print m3")
print(m3)

