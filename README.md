# Fiddler labs coding assignment
The following is the solution for the spreadsheet calculator in Python as part of coding assignment

## Contents of the repo ##

1. Readme file
2. Problem Statement [Pdf](https://github.com/hkhoont/fiddler_labs_coding_assignment/blob/master/Fiddler%20Labs%20Coding%20Assignment.pdf)
3. Sample Input [Text](https://github.com/hkhoont/fiddler_labs_coding_assignment/blob/master/input.txt)
4. Python3 code [calculator.py](https://github.com/hkhoont/fiddler_labs_coding_assignment/blob/master/calculator.py)
### Work in progress
5. Python3 code with bonus (for operators ++ and --) [calculator1.py](link)
6. Python3 code with bonus (for neagitve numbers) [calculator2.py](link)

## How to run the files and get the results ##

1. Download Python file and input.txt
2. Run `cat [text_filename.txt] | python [python_filename.py]`

## Understanding and thoughts ##

Brainstorming on the Algorithm
1) The initial thought is that the question can be solved using some graph algorithms  *(done)*
2) Each cell can be a node, but they are dynamic  *(addressed)*
3) Is this a directed graph? - Relationship [A1,B2-->A1/B2] Can it be [A1/B2,A1-->B2]? Hence should be directed graph(addressed)
4) Another observation is if I define the graph, there is a hierarchy established(something like a precedence in operations)
5)Think about the cycles. Define what do you mean by cycle in this case. 
    * If this is a directed graph, cycle handling may be easy to relate
6) Stopping condition?  *(addressed)*
    * All cell has value in float(take care, the answer should be in float, not int)
        What's the catch with the only positive. This will help in selecting algorithms
    * level 1 - Circular: eg A1-->A1
    * Higher-level circular: A1-->A2-->A3-->A1. Can these types of circularity broken with connections?
    * Other than integer, operator or cell reference
    * Do I need to verify the postfix is correct or not?
7) How to travel the graph? BFS, DFS, or based on levels I defined if I solve similar to operations  *(somehtting like BFS)*
8) RPN is equivalent to Postfix. Convert Postfix to Infix  *(no need)*
    * Infix may be easier to calculated if I can separate the whole line in the form of a list
9) Input - text(no excel). Check with the row and column convention  *(addressed)*
10) Output - print  *(addressed)*
11) Evaluation - Priority: results--> optimization of code Space?,Speed?  *(next version)*

Functions map
    - function - Verify if the postfix relation is correct (A1 A2 A3 +) such statement would be raise flag  *(not considered, this is problem in itself)*
    - function - Convert Postfix to Infix. May be needed  *(no need, computed postfix)*
    - function - Calculate value from Postfix or Infix  *(no need, computed postfix)*
    - Class - vertex  *(no need, used adj list)*
    - Class - graph or simply store it in the dictionary  *(no need, used adj list)*
    - function - criteria for judging the next node to compute  *(done)*
    - function - Traveling in the graph  *(done)*
    - function - reading the input  *(done)*
    - function - output print  *(done)*
    - main function  *(done)*

