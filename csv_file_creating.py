import csv

with open('test.csv','w', newline='') as fp:
    a=csv.writer(fp,delimiter=',')
    data=[['Subject Name','Number of Pass students','Number of Students'],
          ['Economics','80','110'],
          ['English','70','100'],
          ['Bangla','65','90'],
          ['Math','65','120']]

    a.writerows(data)


