import datetime 


def strToDateObj(dString):
	lDateStr = dString.split("/")
	lDateStr.reverse()
	iYear = int(lDateStr[0])
	iMonth = int(lDateStr[1])
	iDay = int(lDateStr[2])
	DateObj = datetime.date(iYear,iMonth,iDay)
	#returns Date Object
	return DateObj

dString = '24/12/2000'

TestList =['Wens',100,'25/12/2015']

def objDateToString(DateObj):
	StrDate = str(DateObj) # Date obj To String
	StrDate = StrDate.replace("-","/")
	print(StrDate)
	StrDate = StrDate.split("/")
	StrDate.reverse()
	sDate = ""
	for date in StrDate:
		sDate = sDate + str(date)+"/"
	#returns String Date		
	return sDate.strip("/")

DateObj= strToDateObj(dString)
StrDate = objDateToString(DateObj)
print('Date String: ' + StrDate)
print('Date Object: ' + str(DateObj))

BDate = datetime.date(1900,1,30)
print('BDate: ' +str(BDate))

if BDate  > DateObj:
	print(True)
else:
	print(False)	
 
TestList[2] = strToDateObj(TestList[2])

print(TestList)

if TestList[2]  > DateObj:
	print(True)
else:
	print(False)
