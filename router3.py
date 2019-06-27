import os
import time
import graph_module2

def break_lines(status,temp,garph):
  lst=[]
  temp=temp.split()
  status[temp[0]]=temp[1]
  for i in range (2,len(temp)+1):
    if i!=len(temp):
      lst.append(temp[i])
    elif i==len(temp):
      temp[-1]=temp[-1].split('\n')
      lst.append(temp[-1][0])
      del lst[-2]
      graph[temp[0]]=lst
              


graph={}
status={}
file_in = open('in.txt', 'r')
while True:
    temp=[]
    temp=file_in.readline()
    if not temp:
      break
    else:
      break_lines(status,temp,graph)


while (True):
    os.system("clear")
    start=input("enter name router or host you wanna ping with:")
    end=input("ping ")
    obj=graph_module2.Graph(graph,status)
    result=obj.find_all_paths(start,end)
    if len(result) >=1:
        print("alive")
    else:
        print("dead")
    time.sleep(5)