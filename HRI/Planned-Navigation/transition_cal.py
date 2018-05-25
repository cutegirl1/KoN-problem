data = []
def cal_transition():
	with open('transition_costs.txt') as f:
		for line in f:
			line = line.split() # to deal with blank 
			if line:            # lines (ie skip them)
				line = [float(i) for i in line]
				data.append(line)
		'''for i in range(len(data)):
			for j in range(len(data[i])):
				print(data[i][j])'''