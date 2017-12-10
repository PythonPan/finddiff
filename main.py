# Python3
# Developed by Himangshu Pan
# Developer Contact 9332943989
# Developer E-Mail dr.himangshu.professor@gmail.com


from sys import argv
import os
import filecmp

def clearDirPath(dirpath):
	if '/' == dirpath[-1]:
		return dirpath[:-1]
	else:
		return dirpath



def makeFullFilePath(dirpath):
	dirFileNameList = os.listdir(dirpath)
	fileNameList = []
	for dirFileName in dirFileNameList:
		fileNameList.append("/".join([dirpath,dirFileName]))
	return fileNameList


def main(source, destination):
	source = clearDirPath(source)
	destination = clearDirPath(destination)

	sourceFileNameList = makeFullFilePath(source)
	destinationFileNameList = makeFullFilePath(destination)

	# print(sourceFileNameList)
	# print(destinationFileNameList)
	# print("The following files are missing....")
	print('\x1b[0;40;41m' + 'The following files are missing....' + '\x1b[0m')
	for sourceFileName in sourceFileNameList:
		Found = False
		for destinationFileName in destinationFileNameList:
			
			if filecmp.cmp(sourceFileName,destinationFileName):
				# print(sourceFileName,"==>>>", destinationFileName)
				# print('\x1b[1;32;48m' + sourceFileName + '\x1b[0m', end='')
				# print('\x1b[1;37;48m' + ' ==>>> ' + '\x1b[0m', end = '')
				# print('\x1b[1;31;48m' + destinationFileName + '\x1b[0m')
				Found = True
				# break
		if not Found:
			print('\x1b[1;31;48m' + sourceFileName + '\x1b[0m')


helpContent = """
	Please Follow the file input format..
	EX:
	main.py --source-folder=/home/himangshu/picture1 --destination-folder=/home/himangshu/picture2

	Thank You
	Please Try Again

"""
# print('\x1b[6;30;42m' + 'Success!' + '\x1b[0m')
# print('\x1b[0;40;41m' + 'Success!' + '\x1b[0m')
if __name__ == '__main__':
	try:
		if '--source-folder=' in argv[1]:
			SOURCE = argv[1].replace("--source-folder=","")
		if '--destination-folder=' in argv[2]:
			DESTINATION = argv[2].replace("--destination-folder=","")
	except:
		print(helpContent)
	if SOURCE and DESTINATION:
		main(SOURCE,DESTINATION)