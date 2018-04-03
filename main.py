import pandas
import random

def getByProb(prob):
  num = prob
  den = 100.0
  rand_num = random.random()
  if(rand_num < (num/den)):
    return True
  return False

def judgeByAge(age, pa, pb):
	ans = -1
	if (int(age) < 8 or int(age) > 44):
		ans = getByProb(pa)
	else:
		ans = getByProb(pb)
	if (ans == 1):
		return True
	else:
		return False


test = pandas.read_csv('test.csv')

workers = ['Rev', 'Capt']

#test['Fare'].fillna(test['Fare'].mean(), inplace=True)
test['Age'].fillna(round(test['Age'].mean()), inplace=True)

ids = []
surv = []

for index, row in test.iterrows():
  canGo = True
  survived = False
  if(canGo and row["Fare"] == ""):
    if (row["Sex"] == "male"):
      survived = judgeByAge(row["Age"], 20, 15)
    else:
      survived = judgeByAge(row["Age"], 85, 75)
    canGo = False
	
  for i in range(len(workers)):
    if(canGo != True):
      break
    if (workers[i] in row["Name"]):
      survived = True
      break
  		
  if (canGo == True):  #classes {1,2,3}
    if (int(row["Pclass"]) == 3):#Third class, almost all died.
      if (row["Sex"] == "male"):
        survived = judgeByAge(row["Age"], 20, 15)
      else:
        survived = judgeByAge(row["Age"], 30, 25)
    elif (int(row["Pclass"]) == 2):#Second class, more less half survived
      if (row["Sex"] == "male"):
        survived = judgeByAge(row["Age"], 42, 36)
      else:
        survived = judgeByAge(row["Age"], 52, 45)
    else:#First class, almost everyone survived
      if (row["Sex"] == "male"):
        survived = judgeByAge(row["Age"], 52, 45)
      else:
        survived = judgeByAge(row["Age"], 65, 60)
      if (survived == True):
        ids += [row["PassengerId"]]
        surv += ["1"]
      else:
        ids += [row["PassengerId"]]
        surv += ["0"]

output = pandas.DataFrame(
    {
        'PassengerId': ids,
        'Survived': surv
    },
    columns=['PassengerId', 'Survived'])
    
output.to_csv('output.csv', index=False)
