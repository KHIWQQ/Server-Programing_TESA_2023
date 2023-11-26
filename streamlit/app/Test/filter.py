import pandas as pd
from io import StringIO  # Use the correct module
# Sample CSV data (replace this with reading from your actual CSV file)
csv_data = """
,_id,Name,Date,Month,Year,WaterDataFront,WaterDataBack,WaterDrainRate
0,655da04e56a46349903eabc6,Huana,1,1,2016,118,105,100
1,655da04f56a46349903eabc7,Huana,2,1,2016,144,175,148
2,655da04f56a46349903eabc8,Huana,3,1,2016,149,117,136
3,655da04f56a46349903eabc9,Huana,4,1,2016,151,159,116
4,655da04f56a46349903eabca,Huana,5,1,2016,177,118,92
5,655da04f56a46349903eabcb,Huana,6,1,2017,173,103,130
6,655da04f56a46349903eabcc,Huana,7,1,2017,147,105,92
"""

# Read the CSV data into a Pandas DataFrame
df = pd.read_csv(pd.compat.StringIO(csv_data))

# Filter data for the year 2016
filtered_data_2016 = df[df['Year'] == 2016]

# Display the filtered data
print(filtered_data_2016)
