import time as t
import matplotlib.pyplot as plt
from math import floor

print("This program will help you to type a word faster, you need to input the word you wanna practise and then practise for 5 times")
time=[]
def type():
    x=input("hey! enter a word that you wanna practise")
    mistakes=0
    b=[]
    for i in range(5):
        start = t.time()
        y= input('type fast')
        end= t.time()
        b.append(y)
        time.append(end-start)
    for j in b:
        if j!=x:
            mistakes+=1
    print('hey you did %i mistakes' % mistakes)
    print(time)
type()
x=[1,2,3,4,5]
y=[time[0],time[1],time[2],time[3],time[4]]
name=["1st attempt","2nd attempt","3rd attempt","4th attempt","5th attempt"]
plt.ylabel('time taken')
plt.xticks(x,name)
plt.bar(x,y)
plt.show()