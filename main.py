import random

nodeList = []
edgeList = []
with open("test.txt") as f:
  for line in f:
    temp = []
    temp.append(int(line.split()[0]))
    temp.append([int(n) for n in line.split()[1:]])
    nodeList.append(temp)

def getEdge(): 
  i = random.choice(nodeList)
  j = random.choice(nodeList[nodeList.index(i)][1])
  return [i[0],j]

# needs to remove association with removed node in all nodes
def contract(n1,n2): 
  temp1 = nodeList[n1][1]
  temp2 = nodeList[n2][1]
  for i in temp2:
    if(i!=nodeList[n1][0]):
        if(i not in temp1):
            nodeList[n1][1].append(i)
  nodeList.pop(n2)
 
def karger():
  while (len(nodeList) > 2):
    edge = getEdge()
    contract(edge[0],edge[1])
  return len(nodeList[0][1])


