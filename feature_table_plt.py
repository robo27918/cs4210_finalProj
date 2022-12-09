ls =['Survey_id', 'Ville_id', 'sex', 'Age', 'Married', 'Number_children', 
'education_level', 'total_members', 'gained_asset', 'durable_asset', 'save_asset',
'living_expenses', 'other_expenses', 'incoming_salary', 'incoming_own_farm', 'incoming_business', 
'incoming_no_business', 'incoming_agricultural', 
'farm_expenses', 'labor_primary', 'lasting_investment', 'no_lasting_investmen', 'depressed']
print(ls)

import numpy as np
from matplotlib import pyplot as plt
plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True
fig, axs = plt.subplots(1, 1)
data = ls
columns = ("Features")
axs.axis('tight')
axs.axis('off')
the_table = axs.table(cellText=data, colLabels=columns, loc='center')
plt.show()