input = '1 3 | 5 6 | 2 3 | 5 5'
# chaotic evil but works
matrix = [list(x)
          for x in list(map(float, element)
                        for element
                        in ([x.split() for x in input.split('|')]))]
