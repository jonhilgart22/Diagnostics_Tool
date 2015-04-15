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

class define_column_numbers():
    """Define the column numbers for each variable"""
    Placements = [ "NFM","NFD"]
    Targeting = ["Broad","Lookalike","Lookalike","LL","Convla","%"]
    Gender = ["M","W","A"]
    Country = ["US","TW","NZ","NO","AU","ZA","GB","CH","DK"]

    def __init__(self):
        self.name = 'Initial Excel file'

    def column_numbers(self, document):
        column_number_from_name = {}

        for count,item in enumerate(document):
            if item in column_number_from_name:
                pass
            else:
                column_number_from_name[item]=count
        return column_number_from_name

    def installs_1_day_post_view(self, document):
        self.name = 'Start Date Column Number'
        installs_1_day_post_view = {}

        for count, item in enumerate (document):

            if item == 'Mobile App Installs [1 Day After Viewing]':
                print "test"
                installs_1_day_post_view[item]=count
                break
            else:
                return " no installs 1 day post view column found"
        return installs_1_day_post_view

    def installs_28_day_post_click(self, document):
        installs_28_day_post_click = {}
        for count, item in enumerate(document):
            if item == "Mobile App Installs [28 Days After Clicking]":
                installs_28_day_post_click[item]=count
                break
            else:
                return "No 28 day post click column found"
        return installs_28_day_post_click

    def gender(self, document):
        gender = {}
        for count, item in enumerate(document):
            if item == 'Gender':
                gender[item]=count
                break
            else:
                return "No gender column found"
        return gender

    def age(self, document):
        age = {}
        for count, item in enumerate(document):
            if item == 'Age':
                age[item]=count
                break
            else:
                return "No age column found"
        return age

    def campaign_name(self, document):
        campaign_name = {}
        for count, item in enumerate(document):
            if item == "Campaign Name":
                campaign_name[item]=count
            else:
                return "No campaign_name column found"
        return campaign_name

    def impressions(self,document):
        impressions = {}
        for count, item in enumerate(document):
            if item == "Impressions":
                impressions[item] = count
                break
            else:
                return "No impression column found"
        return impressions

    def ad_name(self,document):
        ad_name = {}
        for count, item in enumerate(document):
            if item == "Ad Name":
                ad_name[item]=count
                break
            else:
                return "no ad_name column found"
        return ad_name

    def clicks(self,document):
        clicks= {}
        for count, item in enumerate(document):
            if item == "Clicks":
                clicks[item]=count
                break
            else:
                return "No clicks column found"
        return clicks

    def installs_1_day_post_click(self,document):
        installs_1_day_post_click = {}
        for count, item in enumerate(document):
            if item == " Mobile App Installs [1 Day After Clicking]":
                installs_1_day_post_click[item]=count
                break
            else:
                return "No 1 day post click column found"
        return installs_1_day_post_click

excel = define_column_numbers()
print excel.column_numbers(HH_13)
print excel.installs_1_day_post_view(HH_13)
print excel.installs_28_day_post_click(HH_13)
print excel.gender(HH_13)
print excel.age(HH_13)
print excel.campaign_name(HH_13)
print excel.impressions(HH_13)
print excel.ad_name(HH_13)
print excel.clicks(HH_13)
print excel.installs_1_day_post_click(HH_13)





# if item == "Campaign Name":
#                 campaign_name_column_number.append(count)
#             elif item == "Age":
#                 age_column_number.append(count)
#
#     campaign_name_column_number= []
#     age_column_number = []




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



#
# figure_1 = plt.figure()
# ax1 = figure_1.add_subplot(2,2,1)
# ax2 = figure_1.add_subplot(2,2,2)
# plt.plot(randn(50).cumsum(), 'k--')
# figure_1.show()
# plt.show()



available_countries = ()
#for delimiter in HH_13[]



# for item in campaign_name:
#     item = item.split('_')
#     for count, campaign_section in enumerate(item):
#         try:
#
#         print campaign_section



