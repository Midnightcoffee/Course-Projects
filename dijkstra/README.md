Dijstra's algorithm and Test Generator
======

This is a walk through for how to create your own tests case files and accompanying graphs.
For an example of how to turn these into unit-tests look here:

https://github.com/Midnightcoffee/Course-Projects/blob/master/dijkstra/test_dijkstra.py

You will need the file "tools.py" and "test_generator.py

You get the ability generate your own test files, its shortest path from for 2 random points and the cost:
simply run...

$python test_generator.py

from your terminal then answer the following..

number of tests? 1
graph size? 8

0 2,60 3,5 4,6
1 2,70 5,82 7,49
2 0,60 1,70 3,63 4,77 6,7 7,7
3 0,5 2,63 4,70 5,18 6,12 7,42
4 0,6 2,77 3,70 6,29
5 1,82 3,18 6,19
6 2,7 3,12 4,29 5,19
7 1,49 2,7 3,42

Graph0 failed to find lowest cost 37 with path [7, 2, 6, 3, 0, 4] with start point 7 and finish 4

and at the same time create its accompanying graph: see graphs for image

If your using python to implement dijkstra you can easily modify the program to give you this output testing your algorithm, sot that it only reports the graph/nodes that failed.

Details below...

First a quick warning these tools only work if every node is connected to every other node. which shouldn't be a problem. wink wink

I have created three tools that might be of use to you,
they along, with my unitests and datafiles are located at my github repo here.

Tool --------------------->use ------------------->         returns:

vizualizer.py     :  file_name                 visualization of graph
test_generator    :  test_generator.py         graphs/result and graphs


Notes:
python2.7, may not work with version 3
$: From terminal

vizualizer.py
file_name: str: a file of the same specifications as our assignment file
visualization of graph: file: .png

test_generator:
when you run python test_generator it will let you choose the number of graphs
and the size you wish to create. Then it "magical" will create folder "graphs"
that will contain result.txt. result.txt will tell you which graph in they
graph folder failed.

Example:  test_generator
how many tests? 3
what size graph? 10

Creates this...

   graphs/ <- folder created
      graph0.png
      graph0.txt
      graph1.png
      graph1.txt
      graph2.png
      graph2.txt
      results.txt <- results -> 

if you open results.txt
    Graph0 failed to find lowest cost 27 with path [15, 17] with start point 15 and finish 17
    Graph1 failed to find lowest cost 31 with path [0, 9] with start point 0 and finish 9
    Graph2 failed to find lowest cost 45 with path [0, 7, 17] with start point 0 and finish 17

then take a look at graph0.png for the visual aid

IF your NOT using python this can only be used to generate test files 
If you are using python you can modify test_generator:

    from dijkstra import dijkstra #FIXME change me to use your algorithm

to test your algorithm against.
