import sys
import auxtools as at


listdir = ['tests']
graphs = at.pipe(
        at.list_files,
        at.open_files,
        at.interpret_data,
      #  at.tap,
        at.cut_widhts,
        params=listdir
        )
print(graphs)