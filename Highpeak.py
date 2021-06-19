def combinations(arr, data, start,end, index, r):
    if (index == r):
    	combis.append([i for i in data])
    	return
    i = start
    while(i <= end and end - i + 1 >= r - index):
        data[index] = arr[i]
        combinations(arr, data, i + 1,end, index + 1, r)
        i += 1
def min_max_diff(combin):
	l=[i[1] for i in combin]
	mi=min(l)
	ma=max(l)
	return ma-mi

inputf=open('sample_input.txt','r+')
goodies=[]
f=0
for line in inputf:
	if line.strip()=='':
		continue
	if line.startswith("Number of employees:"):
		no_of_emp=int(line.strip().split()[-1])
	if line.startswith("Goodies and Prices:"):
		f=1
		continue
	if f==1:
		l=line.strip().split(': ')
		goodies.append([l[0],int(l[1])])
combis=[]
data=[0]*no_of_emp
combinations(goodies,data,0,len(goodies)-1,0,no_of_emp)
mi=2**32-1
result=0
for combin in combis:
	rmin=min_max_diff(combin)
	if rmin<mi:
		result=combin
		res_min=rmin
		mi=rmin
inputf.close()
outputf=open('sample_output.txt','w+')
outputf.write('The goodies selected for distribution are:\n')
outputf.write('\n')
for i in result:
	outputf.write(i[0]+': '+str(i[1])+'\n')
outputf.write('\n')
outputf.write("And the difference between the chosen goodie with highest price and the lowest price is "+str(res_min))