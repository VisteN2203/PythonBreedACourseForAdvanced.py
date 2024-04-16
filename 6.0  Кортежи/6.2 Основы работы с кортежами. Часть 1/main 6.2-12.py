tuples = [(), (), ('',), ('a', 'b'), (), ('a', 'b', 'c'), (1,), (), (), ('d',), ('', ''), ()]
non_empty_tuples = [tuples[i] for i in range(len(tuples)) if len(tuples[i]) >= 1]

print(non_empty_tuples)




