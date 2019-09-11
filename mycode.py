import csv

with open('test.csv','w', newline='') as fp:
    a=csv.writer(fp,delimiter=',')
    data=[['Stock','Sales'],
          ['100','24'],
          ['120','33'],
          ['23','50']]

    a.writerows(data)


















    
