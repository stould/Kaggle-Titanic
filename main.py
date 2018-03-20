import pandas
import random


def judgeByAge(age, l, r):
	ans = -1
	if (int(age) < 8 or int(age) > 44):
		ans = random.randint(l, r)
	else:
		ans = random.randint(l, r - int((r - l) / 3))
	if (ans == 1):
		return True
	else:
		return False


test = pandas.read_csv('test.csv')

workers = ['Rev', 'Capt']

test['Fare'].fillna(test['Fare'].mean(), inplace=True)
test['Age'].fillna(round(test['Age'].mean()), inplace=True)

ids = []
surv = []

for index, row in test.iterrows():
	survived = False
	for i in range(len(workers)):
		if (workers[i] in row["Name"]):
			survived = True
			break
	if (survived == False):  #classes {1,2,3}
		if (int(row["Pclass"]) == 3):
			if (row["Sex"] == "male"):
				survived = judgeByAge(row["Age"], 1, 6)
			else:
				survived = judgeByAge(row["Age"], 1, 5)
		elif (int(row["Pclass"]) == 2):
			if (row["Sex"] == "male"):
				survived = judgeByAge(row["Age"], 1, 4)
			else:
				survived = judgeByAge(row["Age"], 1, 3)
		else:
			if (row["Sex"] == "male"):
				survived = judgeByAge(row["Age"], 1, 3)
			else:
				survived = judgeByAge(row["Age"], 1, 2)
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
