import sys
import auxtools as at


# listdir = ['tests']
listdir = ['small', 'grids', 'harwellboeing']
results = at.pipe(
        at.list_files,
        at.open_files,
        at.interpret_data,
      #  at.tap,
        at.local_searches,
        at.cut_widhts,
        at.write_results,
        params=listdir
        )
print(results)