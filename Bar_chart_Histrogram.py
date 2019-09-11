import matplotlib.pyplot as plt

Students_Mark = [0,90,50,70,50,90,80,70, 99,75,67,88,99,98,97,45,67,86,95,80]


bins = [0,10,20,30,40,50,60,70,80,90,100]

plt.hist(Students_Mark,bins, histtype='bar',rwidth=0.8)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Student Mark')
plt.legend()
plt.show()
        
        
        
    
        
        
