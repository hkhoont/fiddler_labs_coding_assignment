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

