import matplotlib.pyplot as plt

sleeping= [7,8,6,11,7]
eating = [2,1,2,3,2]
working=[9,8,7,2,2]
playing = [6,7,9,8,13]

slices = [7,2,2,13]
activities = ['sleeping','eating','working','playing']
cols = ['c','m','r','b']

plt.pie(slices,
        labels=activities,
        colors=cols,
        startangle=90,
        shadow= True,
        explode=(0,0.1,0,0) ,
        autopct='%1.1f%%')

plt.title('pie chart')
plt.show()
