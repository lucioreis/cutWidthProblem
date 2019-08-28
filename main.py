import sys
import auxtools as at


listdir = ['small', 'grids', 'harwellboeing']
graphs = at.pipe(
        at.list_files,
        at.open_files,
        at.interpret_data,
      #  at.tap,
        at.cut_widhts,
        params=['grids']
        )
print(graphs)