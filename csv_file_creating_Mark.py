import csv

with open('Mark_List.csv','w', newline='') as fp:
    a=csv.writer(fp,delimiter=',')
    data=[['Student mark'],
          ['90'],['99'],['90'],['80'],['70'],['40'],['100'],['99'],['30'],
          ['50'],['60'],['65'],['90'],['50'],['90'],
          ]

    a.writerows(data)


