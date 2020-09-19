class M:

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
 #            print(list_t)    
#            print(l1)
            i +=1
        st =""
#        for i in self.l_list:
#            print(i)
#           for j in i:
#                print(j)
#                st = st +f"{j}\t"
#                print(f"{j}\t",end="")
#            print()
#            st = st + "\n"
#        print(f" st = {st}")    
        return M(list_out) #st    
"""
    def __add__(self,other):
          l_ = len(self)
          while i < l_-1:
              l1_ =len(self(i))
              print(l_)
          return "ADD"          
   """     
#

my_list =[1,2,3,4,5]
my_list1 =[i for i in range(6,11)]
my_list2 =[i for i in range(11,16,)]

list_list =[my_list , my_list1, my_list2]

#print(list_list)

m1=M(list_list)

#print(m1.l_list)


my_l =[11,12,13,14,15]
my_l1 =[i for i in range(15,20)]
my_l2 =[i for i in range(80,90,2)]
list_list_1 =[my_l , my_l1, my_l2]

m2=M(list_list_1)
#print(m2.l_list)
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

