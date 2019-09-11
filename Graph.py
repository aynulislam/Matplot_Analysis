import matplotlib.pyplot as plt
import csv

passStudentx=[]

totalStudenty=[]

with open('test.csv','r') as csvfile:
    plots=csv.reader(csvfile,delimiter=',')
    for column in plots:
        passStudentx.append((column[1]))
        totalStudenty.append((column[2]))



plt.plot(passStudentx,totalStudenty,label='Loaded from file!')
plt.xlabel('Pass Student')
plt.ylabel('Total Student')

plt.title('Students Mark')
plt.legend()
plt.show()

        
        
        
    
        
        
