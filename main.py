import random

# dictionary
nodeList = {}
with open("kargerMinCut.txt") as f:
  for line in f:
    temp = []
    temp.append(int(line.split()[0]))
    temp.append([int(n) for n in line.split()[1:]])
    nodeList[temp[0]] = temp[1]

def getEdge(): 
  i = random.choice(list(nodeList))
  j = random.choice(nodeList[i])
  return [i,j]

def contract(n1,n2): 
  for i in nodeList[n2]:
    if(i!=n1):
        nodeList[n1].append(i)
  nodeList.pop(n2)
  for key,value in nodeList.items():
    value[:] = [n1 if x==n2 else x for x in value]
    value[:] = [x for x in value if x!=key]

def karger():
  while (len(nodeList) > 2):
    edge = getEdge()
    contract(edge[0],edge[1])
  val = len(list(nodeList.values())[0])
  return val


