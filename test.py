from sklearn.ensemble import RandomForestClassifier
import numpy as np

domainlist = []
class Domain:
	def __init__(self,_name,_label,_length):
		self.name = _name
		self.label = _label
		self.length = _length


	def returnData(self):
		return [self.length]

	def returnLabel(self):
		if self.label == "notdga":
			return 0
		else:
			return 1
		
def initData(filename):
	with open(filename) as f:
		for line in f:
			line = line.strip()
			if line.startswith("#") or line =="":
				continue
			tokens = line.split(",")
			name = tokens[0]
			label = tokens[1]
			length = len(name)
			
			domainlist.append(Domain(name,label,length))

def main():
	initData("train.txt")
	featureMatrix = []
	labelList = []
	for item in domainlist:
		featureMatrix.append(item.returnData())
		labelList.append(item.returnLabel())

	clf = RandomForestClassifier(random_state=0)
	clf.fit(featureMatrix,labelList)
	
	filename2 = 'test.txt'
	filename3 = 'result.txt'
	with open(filename3,'a') as resf:
         with open(filename2) as testf:
	        for line in testf:
			    line = line.strip()
			    if line.startswith("#") or line =="":
				    continue
				tokens = line.split(",")
			    tname = tokens[0]
			    tlength = [len(tname)]
			    tlable = clf.predict([tlength])	
                ttlable=""				
			    if tlable == 0
				    ttlable = "notdga"
				else:
				    ttlable = "dga"
				resf.write(str(tname)+str(",")+str(ttlable)+'\n')
			
	


if __name__ == '__main__':
	main()

