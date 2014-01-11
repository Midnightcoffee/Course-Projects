Code is python 2.7 compatible
$ (dollar symbol) means from the command line

There are a number of good ways to test python code, if your familiar with
nosetests you can use that to test all my code at once

------------ HOW TO -TEST TOPOLOGICAL SORT ------------:

Test That we get a correct topolgical sort:
tests for topological sort are contained in  test_topological_sort.py
you can run the file by by typing

    $python test_topological_sort.py

you should see:

    ..........
    ----------------------------------------------------------------------
    Ran 10 tests in 0.001s

    OK

This tells you that inside the file this test passed

    def test_basic(self):
        graph = {
                1: {2},
                2: {3},
                3: set(),
                }
        expected = [1, 2, 3]
        returned = dfs_topological_sort(graph)
        self.assertListEqual(expected, returned)

Meaning, the object returned from dfs_topological sort on that graph
matched the expected object

You will notice there are two sets of tests for each different DFS. There are
several graphs which are greater then size 5.

------------ HOW TO GENERATE GRAPHS/ "COMPILE CODE" ------------

simply run:

    $python main.py

Which will generate a .png file with the graph

------------ HOW TO READ GRAPH------------

As the title suggests

    dfs = red
    source removal = blue

The data suggests both are linear functions that is O(|Edges| + |vertices|). But that
dfs is faster. It should be noted that source removal was faster tell i
optimized some code

Each point on the graph represents the min of n number
of runs with n=10. So for example, if the run times for a graph with 100 Edges
was  [1, 2, 3] then we would plot (100, 1). Read additional for details

------------    RESULTS  (from runtime.txt) ----------------

While ploting is nice it requires you really know the library your using well
in order to get the desired picture. Meanwhile these results tell the
story just as well...

edge count | depth first search   | source removal
        12 |    1.19209289551e-05 |    1.59740447998e-05
       300 |     0.00019097328186 |    0.000239849090576
      2700 |     0.00148415565491 |     0.00204300880432
     22800 |      0.0124578475952 |       0.019101858139
    367500 |       0.239754915237 |       0.369387865067



---------------- Profile ------------------
I also profiled my code, which breaks down the time spent at each part


    DFS

Press ENTER or type command to continue
         272720 function calls in 0.096 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.001    0.001    0.096    0.096 <string>:1(<module>)
        1    0.000    0.000    0.008    0.008 tools.py:135(copy_graph)
        1    0.004    0.004    0.004    0.004 tools.py:142(<dictcomp>)
        1    0.058    0.058    0.095    0.095 topological_sort.py:15(dfs_topological_sort)
    31250    0.003    0.000    0.003    0.000 {method 'add' of 'set' objects}
    62499    0.004    0.000    0.004    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    89481    0.015    0.000    0.015    0.000 {method 'issuperset' of 'set' objects}
        1    0.003    0.003    0.003    0.003 {method 'items' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 {method 'iterkeys' of 'dict' objects}
    31250    0.002    0.000    0.002    0.000 {method 'pop' of 'list' objects}
    58231    0.004    0.000    0.004    0.000 {method 'pop' of 'set' objects}
        1    0.000    0.000    0.000    0.000 {method 'reverse' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {next}

A lot of time is spent on issuperset, i'm not sure this is avoidable but its
a good starting place. For future optimizations


    SOURCE REMOVAL
         396882 function calls in 0.170 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.002    0.002    0.170    0.170 <string>:1(<module>)
        1    0.006    0.006    0.008    0.008 tools.py:104(<setcomp>)
        1    0.034    0.034    0.043    0.043 tools.py:82(inverse_graph)
        1    0.000    0.000    0.035    0.035 tools.py:97(find_sources)
        1    0.067    0.067    0.169    0.169 topological_sort.py:43(source_removal_topological_sort)
   121875    0.006    0.000    0.006    0.000 {len}
   121874    0.009    0.000    0.009    0.000 {method 'add' of 'set' objects}
    31250    0.002    0.000    0.002    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        2    0.031    0.015    0.031    0.015 {method 'items' of 'dict' objects}
    31250    0.002    0.000    0.002    0.000 {method 'pop' of 'set' objects}
    90625    0.011    0.000    0.011    0.000 {method 'remove' of 'set' objects}

Its hard to say from this what I would optimize next, maybe with more familiarity
I could pick something out

------------ ADDITIONAL ------------

To "time" the my algorithm i used the timeit module. As to why i took the min
of my run times consider this from the module notes
http://docs.python.org/2/library/timeit.html


    It’s tempting to calculate mean and standard deviation from the result vector
    and report these. However, this is not very useful. In a typical case,
    the lowest value gives a lower bound for how fast your machine can run the
    given code snippet; higher values in the result vector are typically not c
    aused by variability in Python’s speed, but by other processes interfering
    with your timing accuracy. So the min() of the result is probably the
    only number you should be interested in. After that, you should look at
    the entire vector and apply common sense rather than statistics.


------------- future improvements ----------------
I tried to make main.py create two graphs, one that didn't contain
the last point as its so much larger is pulls the graph to far. For some
reason i won't create them both at the same time. So if you want the smaller
points then COMMENT OUT THE TOP CODE and uncomment the bottom part.

TODO: Fix this problem!

