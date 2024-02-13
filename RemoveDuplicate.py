def RemoveDuplicate():
	File = open("EQSolutions.txt",'r+')

	EQs = []
	EQsNoDuplicate = ()

	for L in File:
		EQs.append(L)

	EQsNoDuplicate = set(EQs)

	File.seek(0)
	File.truncate(0)
	print("Total Solutions: ",len(EQs))
	print("Total Unique Solutions: ",len(EQsNoDuplicate))
	for L in EQsNoDuplicate:
		File.write(L)

	File.close()
if __name__ == '__main__':
	RemoveDuplicate()