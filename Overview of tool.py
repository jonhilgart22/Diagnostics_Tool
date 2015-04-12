__author__ = 'jonathanhilgart'


import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from numpy.random import randn





HH_13 = pd.read_csv('/Users/jonathanhilgart/Documents/Ampush/Hothead_13_4115.csv')



def main():
    """Main entry point for the script."""
    pass

# column_names = {}
# for item in HH_13:
#     column_names.append(item)



#define the numbers for each column

def column_numbers(document):
    column_number_from_name = {}
    campaign_name_column_number= []
    age_column_number = []

    for count,item in enumerate(document):

        column_number_from_name[item]=count
        if item == "Campaign Name":
            campaign_name_column_number.append(count)
        elif item == "Age":
            age_column_number.append(count)
        else:
            pass
    return column_number_from_name

print column_numbers(HH_13)


all_start_dates = HH_13['\xef\xbb\xbf"Start Date"']
all_spent = HH_13['Amount Spent (USD)']
campaign_name = HH_13 ['Campaign Name']

##get unique start dates
average_spend_by_date = {}
unique_dates = []


#getting erro below , look into this

# def get_unique_characters(data):
#     unique_character = []
#     for count, info in enumerate(data):
#         #if info in unique_character:
#          #   pass
#         else:
#             unique_character.append(data)
#     return unique_character
#
# print get_unique_characters(all_start_dates)


        # for spend in all_spent:
        #     print spend, "spend"
        #     current_sum = spend.sum()
        #     if all_start_dates[date] == date:
        #         print date , "date"
                # average_spend_by_date[date]=current_sum
                # print "passed"
            # else:
            #     print "failed"




figure_1 = plt.figure()
ax1 = figure_1.add_subplot(2,2,1)
ax2 = figure_1.add_subplot(2,2,2)
plt.plot(randn(50).cumsum(), 'k--')
figure_1.show()
plt.show()

Placements = [ "NFM","NFD"]
Targeting = ["Broad","Lookalike","Lookalike","LL","Convla","%"]
Gender = ["M","W","A"]
Country = ["US","TW","NZ","NO","AU","ZA","GB","CH","DK"]

available_countries = ()
#for delimiter in HH_13[]



# for item in campaign_name:
#     item = item.split('_')
#     for count, campaign_section in enumerate(item):
#         try:
#
#         print campaign_section



