"""
       File : main.py
     Author : Drew Verlee
       Date : 17.10.13.
      Email : drew.verlee@gmail.com
     GitHub : https://github.com/Midnightcoffee/
Description : comparing two topological sorting algorithms: dfs, source removal
"""



if __name__ == '__main__':
    from topological_sort import dfs_topological_sort, source_removal_topological_sort
    from tools import file_to_graph, run_time_anyalsis, line_plot_compare,\
        write_results
    file_names = ['graph7.txt', 'graph125.txt', 'graph1000.txt',
            'graph8000.txt', 'graph100000.txt']
    dfs_rt_results = []
    sr_rt_results = []
    edge_counts = []
    for file_name in file_names:
        graph, edge_count = file_to_graph(file_name)
        edge_counts.append(edge_count)
        number = 1
        repeat = 10
        dfs_rt_results.append(run_time_anyalsis(dfs_topological_sort, 
            graph, number, repeat))
        sr_rt_results.append(run_time_anyalsis(source_removal_topological_sort, 
            graph, number, repeat))

    # comment out if you want to create the graph without the final point
    # plot_name = '''Compare topological sort: dfs(red) vs source removal(blue):
# min of {0} runs'''.format(repeat)
    # dfs_plot_type = 'ro'
    # rt_plot_type = 'bo'
    # dfs_package = ('depth-first-search',  edge_counts, dfs_rt_results, dfs_plot_type)
    # rt_package = ('source-removal',  edge_counts, sr_rt_results, rt_plot_type)
    # line_plot_compare((dfs_package, rt_package), plot_name, 'edges', 'seconds')

    # it seems reasonable to try and plot without the final and larger point
    # UN COMMENT to create 
    plot_name = '''without final points topological sort: dfs(red) vs source removal(blue):
min of {0} runs'''.format(repeat)
    dfs_plot_type = 'ro'
    rt_plot_type = 'bo'
    dfs_package_small = ('depth-first-search',  edge_counts[0:-1], dfs_rt_results[0:-1], dfs_plot_type)
    rt_package_small = ('source-removal',  edge_counts[0: -1], sr_rt_results[0:-1], rt_plot_type)
    line_plot_compare((dfs_package_small, rt_package_small), plot_name, 'edges', 'seconds')


    write_results(edge_counts, dfs_rt_results, sr_rt_results, 'runtimes.txt')



