import matplotlib.pyplot as plt
import numpy as np



avg_importance1 = [['education_level', 0.12864775137844947], ['Age', 0.12070099134498666], 
                 ['lasting_investment', 0.11574672314924608],['no_lasting_investment', 0.09450960597798809], 
                ['living_expenses', 0.07888141044720574], ]
avg_importance2 = [['Age', 0.12062999394337455], ['education_level', 0.09272657681529073], ['no_lasting_investment', 0.09217110285279022], ['durable_asset', 0.08168150501681372], ['living_expenses', 0.07825378748145077], ['lasting_investment', 0.06923965339697724], ['incoming_agricultural', 0.06891131035411567], ['save_asset', 0.06776384048261799], ['other_expenses', 0.06512700203319091], ['farm_expenses', 0.06376396257177228], ['gained_asset', 0.06219348213235356], ['total_members', 0.05430957548565105], ['Number_children', 0.032898015143710296], ['Married', 0.015690966335473844], ['incoming_business', 0.007875801750553638], ['incoming_no_business', 0.007249528395064282], ['sex', 0.005205409078741241], ['incoming_salary', 0.005133769115999646], ['incoming_own_farm', 0.005012992555451472], ['labor_primary', 0.004161725058606893]]
#first: unzip the 2d list containing label and avg_val
sep_data = list(zip(*avg_importance2))
labels = list(sep_data[0])
avg_vals = list(sep_data[1])

# sort the feature index by importance score in descending order
importances_index_desc = np.argsort(avg_vals)[::-1]
feature_labels = [labels[i] for i in importances_index_desc]

plt.figure()
plt.bar(feature_labels,avg_vals)
plt.xticks(feature_labels, rotation='vertical')
plt.ylabel('Importance')
plt.xlabel('Features')
plt.title('Feature Importance (AVG of 10-Fold CV)')
plt.tight_layout()
plt.show()