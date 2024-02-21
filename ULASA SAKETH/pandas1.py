'''import pandas 

# Create a dictionary 'a' containing information about bikes and their passing numbers.
a={
    'bikes': ["hero","bajaj","honda","duke"] ,
    'passing': [3,2,4,5]
}
# Create a pandas DataFrame 'var' from the dictionary 'a'.
var=pandas.DataFrame(a)
# Print the DataFrame 'var' to the console.
print(var)
'''

import pandas as pd

data={ 'cars' : ["bmw","volvo","jeep"],
       'passing' : [2,4,1]
}

var=pd.DataFrame(data)
print(var)
print(pd.__version__)        #checking pandas version




