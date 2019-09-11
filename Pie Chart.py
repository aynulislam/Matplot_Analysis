import matplotlib.pyplot as plt
import csv

passStudentx=[]

totalStudenty=[]

with open('test.csv','r') as csvfile:
    plots=csv.reader(csvfile,delimiter=',')
    for column in plots:
        passStudentx.append((column[1]))
        totalStudenty.append((column[2]))


slices=[65,70,80,85]

activities = ['Bangla','English','Economics','Math']
cols = ['c','m','r','b']



plt.pie(slices,
        labels=activities,
        colors=cols,
        startangle=90,
        shadow= True,
        explode=(0,0.1,0,0) ,
        autopct='%1.1f%%')

plt.title('Students Mark')
plt.show()

        
        
        
    
        
        
