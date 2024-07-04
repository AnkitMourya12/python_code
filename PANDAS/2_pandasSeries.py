# A Pandas series is like a column in a table . it is 1D array which holds data of any type.
# here we will create a simple pandas series.
import pandas as pd
ankit = [1,7,2]
ankitnew = pd.Series(ankit)
print(ankitnew)

# labeling - label can be use to access a specified value.
import pandas as pd
ankit = [1,7,2]
ankitnew = pd.Series(ankit)
print(ankitnew[0])

# wuth Create label you can create your own name labels:
import pandas as pd
ankit = [1,7,2]
ankitnew = pd.Series(ankit, index=["x", "y", "z"])
print(ankitnew)

# labeling - label can be use to access a specified value.(after creating own label)
import pandas as pd
ankit = [1,7,2]
ankitnew = pd.Series(ankit, index=["x", "y", "z"])
print(ankitnew["x"])

# you can also use a key or value object like a dictionary, when creating a series.
# here we will create a simple pandas series from a dictionary.
import pandas as pd
cal = {"day1": 420, "day2":380, "day3":390}
ankitnew = pd.Series(cal)
print(ankitnew)

# now we will create a series using only data from day1 and day2
import pandas as pd
cal = {"day1": 420, "day2":380, "day3":390}
result = pd.Series(cal, index=["day1", "day2"])
print(result)

# DataFrame: Data sets in pandas are usually multidimentional tables,, and they re called DataFrames.
# series are like columns and dataframes is the whole table.

# we will now create a dataframe from 2 series.
import pandas as pd
ankit = {"cal": [420, 380, 390], "duration": [50, 40, 45]}
ankitnew = pd.DataFrame(ankit)
print(ankitnew)
