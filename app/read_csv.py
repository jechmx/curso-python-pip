import csv

def read_csv(path):
  with open(path,'r') as csvfile:
    reader=csv.reader(csvfile,delimiter=',')
    header=next(reader)
    #print(header)
    data=[]
    for row in reader:
      interable=zip(header,row)
      #print(list(interable))
      country_dict={key:value for key,value in interable}
      data.append(country_dict)
    return data
      
if __name__=='__main__':
  data=read_csv('data.csv')
  print(list(map(lambda data:data['Country/Territory'],data)))