"""
Fiddler Labs coding assignment
@hkhoont - Harsh Khoont (hsk2147@columbia.edu)

Brainstorming on the Algorithm
1) The initial thought is that the question can be solved using some graph algorithms. 
2) Each cell can be a node, but they are dynamic
3) Is this a directed graph? - Relationship [A1,B2-->A1/B2] Can it be [A1/B2,A1-->B2]? Hence should be directed graph
4) Another observation is if I define the graph, there is a hierarchy established(something like a precedence in operations). 
    I will have to define each relation between nodes at a particular level. 
5)Think about the cycles. Define what do you mean by cycle in this case. 
    If this is a directed graph, cycle handling may be easy to relate
6) Stopping condition? 
    a) All cell has value in float(take care, the answer should be in float, not int)
        What's the catch with the only positive. This will help in selecting algorithms
    b) level 1 - Circular: eg A1-->A1
    c) Higher-level circular: A1-->A2-->A3-->A1. Can these types of circularity broken with connections?
    d) Non-interger/+-*//A-Z value-added
    e) Do I need to verify the postfix is correct or not?
7) How to travel the graph? BFS, DFS, or based on levels I defined if I solve similar to operations
8) RPN is equivalent to Postfix. Convert Postfix to Infix
    Infix may be easier to calculated if I can separate the whole line in the form of a list
9) Input - text(no excel). Check with the row and column convention
10) Output - print
11) Evaluation - Priority: results--> optimization of code(Space?,Speed?) 

Functions map
function - Verify if the postfix relation is correct (A1 A2 A3 +) such statement would be raise flag
function - Convert Postfix to Infix. May be needed
function - Calculate value from Postfix or Infix
Class - vertex
Class - graph or simply store it in the dictionary
function - criteria for judging the next node to compute
function - Traveling in the graph
function - reading the input
function - output print
main function

"""
#Importing the data into List
import sys
import re  
data = sys.stdin.read().splitlines()

# for i in data:
# 	print(i)

# print(data)

operations = ['+','-','*','/']

def check_empty(cell):
	"""
	Function to detect any missing operand after tokenizing

	input: Tokenised the content of the cell - type: list of strings
	output: True is any operand is None - type: Boolean
	"""
	for k in cell:
		if k=='':
			return True
	return False

def check_self_join(cell,i,j):
	"""
	Function to detect self referencing

	input: a token (may be a cell reference,int or operator) - type: str
	output: True - type: Boolean
	"""
	for c in cell:
		if c==(abcd[i]+str(j)):
			return True

def dtype_function(element):
	"""
	Function to detect type of token

	input: a token (may be a cell reference,int or operator) - type: str
	output: type: string
	"""
	if element[0] in abcd:
		return 'reference'
	elif element in operations:
		return 'operator'
	else:
		try:
			if type(int(element)) == int:
				return 'value'
		except ValueError:
			print('Input Wrong')
			return '-1'
def check_all_true(compound_index):
	"""
	Function checks if all the cell dependencies are calculated 
	If done the cell is added to queue and poped out of the opp_dict

	input: compound_index - type: str
	"""
	global queue
	global opp_dict
	tf = opp_dict[compound_index].values()
	if all(tf):
		queue.append(compound_index)
		opp_dict.pop(compound_index)

def toggle_tf_in_opp_dict5(compound_index,next_computation):
	"""
	Function to keep track for all the cell dependencies
	Also their keep status of dependencies computation to float 

	input: compound_index,list of cell - type: str,list of cell referencies
	"""
	global opp_dict
	for element5 in next_computation:
		opp_dict[element5][compound_index] = True
		check_all_true(element5)

def evaluate4(compound_index):
	"""
	Function computes postfix formual to integer. Saves it in new spreadsheet:excel
	Also initiate the updation of the status by calling toggle_tf_in_opp_dict5
	
	input: compound_index - type: str
	"""
	global excel
	global right_dict
	global opp_dict
	row4_label = compound_index[0]
	row4 = dict_alphabet[row4_label]
	column4 = int(compound_index[1:])
	stack = []
	cell4 = re.split(r'\s{1,}', data_2d[row4][column4])
	for element4 in cell4:
		element_type4 =dtype_function(element4)
		if element_type4=='value':
			if not element4:
				print('Wrong input')
				return -1
			stack.append(float(element4))	

		elif element_type4=='reference':
			element4_row_label = element4[0]
			element4_row = dict_alphabet[element4_row_label]
			element4_column = int(element4[1:])

			element4_value = excel[element4_row][element4_column]
			if not element4_value:
				print('Wrong input')
				return -1
			stack.append(element4_value)

		elif element_type4 == 'operator':
			# no need to convert to infix. In fact postfix is better the way I am implementing the algorithm
			operand1 = stack.pop()
			operand2 = stack.pop()
			#operands should be already in float from previous steps
			if element4 == '/':
				stack.append(float(operand2 / operand1))

			elif element4 == '*':
				stack.append(float(operand2 * operand1))

			elif element4 == '+':
				stack.append(float(operand2 + operand1))

			elif element4 == '-':
				stack.append(float(operand2 - operand1))
	#Storing the Grid			
	answer = stack.pop()
	# print(answer)
	excel[row4][column4] = answer
	# print(excel)

	#Prep for the next iteration
	if compound_index in right_dict:
		next_computation = right_dict.get(compound_index,[])
		right_dict.pop(compound_index)
		toggle_tf_in_opp_dict5(compound_index,next_computation)
	else:
		return


size = data[0].split(' ')
col = int(size[0])
row = int(size[1])
print(col,row)

#dictionary for storing directed graph, format: keys: cells, values: dict with dependencies
right_dict={}

#dictionary for storing opposite directed graph, format: keys: cells, values: list of cells having input as key
opp_dict={}
queue=[]

import string
abcd =  [chr(i) for i in range(ord('A'), ord('Z')+1)]
# print(abcd)
dict_alphabet={}
for i,char in enumerate(abcd):
	dict_alphabet[char] = i

excel = [[None for _ in range(col+1)] for _ in range(row)]

data_2d = [[None]+data[i:i+col] for i in range(1, col*row+1, col)]
del(data)
# print(data_2d)
# print(len(data_2d),len(data_2d[0]))
# print(len(excel),len(excel[0]))

for i in range(row):
	for j in range(1,col+1):
		compound_index = abcd[i]+str(j)
		cell = re.split(r'\s{1,}', data_2d[i][j])
		#cell = data_2d[i][j].split(' ')

		flag = check_empty(cell)
		if flag==True:
			print('Some of the values in the Excel sheet are not defined')
			raise ValueError	

		flag = check_self_join(cell,i,j)
		if flag==True:
			print('The cell is self joined with itself')
			raise ValueError

		if len(cell)==1:
			element = cell[0]
			element_type =dtype_function(element)
			if element_type=='value':
				excel[i][j]=float(element)
				queue.append(compound_index)

			elif element_type=='reference':
				element_row_label = element[0]
				element_row = dict_alphabet[element_row_label]
				element_column = int(element[1:])

				excel[i][j] = data_2d[element_row][element_column]

				if compound_index not in opp_dict:
					opp_dict[compound_index] = {}
				opp_dict[compound_index][element] = False

				if element not in right_dict:
					right_dict[element] = []
				right_dict[element].append(compound_index)

		else:
			#flag=0 means the cell has only simple postfix computation, with no dependencies	
			flag=0 

			for element in cell:
				element_type=dtype_function(element)

				if element_type=='reference':
					flag=1
					if compound_index not in opp_dict:
						opp_dict[compound_index] = {}
					opp_dict[compound_index][element] = False

					if element not in right_dict:
						right_dict[element] = []
					right_dict[element].append(compound_index)
				elif element_type=='-1':
					print('Wrong Input')

			if flag==0:
				queue.append(compound_index)

# print(excel)
while queue:
	compound_index = queue.pop(0)
	evaluate4(compound_index)

# Print
for i in range(row):
	for j in range(1,col+1):
		print(format(excel[i][j], '.5f'))	
