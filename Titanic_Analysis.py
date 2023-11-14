#!/usr/bin/env python
# coding: utf-8

# In[37]:


#  printing each column name in the dataset along with its corresponding index

import pandas as pd

df = pd.read_csv('titanic.csv')

for i, column_name in enumerate(df.columns):
    print(f'Index of column "{column_name}": {i}')


# In[38]:


# assigning the variable indexes
#step 0

name_index = 3
surv_index = 1
sex_index = 4
fare_index = 9


# In[39]:


# Method from the course to skip the header
# number of data rows in the CSV file (excluding the header row)
#Step 1

import csv

def csv_reader(file):
    with open(file, 'r') as f:
        reader = csv.reader(f)
        # Skip the header row
        next(reader)
        data = list(reader)
    return data


file = 'titanic.csv'  
print("TESTING", len(csv_reader(file)))




# In[40]:


# longest name
#Step 2

def longest_passenger_name(passenger_list):
    longest_name = ''
    for passenger in passenger_list:
        name = passenger[name_index]
        if len(name) > len(longest_name):
            longest_name = name
    return longest_name


test_list = [[1,0,3,"Longest Name"],[2,0,2,"Short"]]
print("TESTING", longest_passenger_name(test_list))

filename = 'titanic.csv'  
print("TESTING", longest_passenger_name(csv_reader(filename)))


# In[41]:


# Step 3: total_survival_percentage(passenger_list)

def total_survival_percentage(passenger_list):
    total_passengers = len(passenger_list)
    total_survived = sum(int(passenger[surv_index]) for passenger in passenger_list)
    survival_percentage = total_survived / total_passengers
    return survival_percentage


test_list = [[1,0],[2,1],[3,1],[4,1]]
print("TESTING", total_survival_percentage(test_list))

filename = 'titanic.csv' 
print("TESTING", total_survival_percentage(csv_reader(filename)))


# In[42]:


# Step 4: survival_rate_gender(passenger_list)

def survival_rate_gender(passenger_list):
    male_survived = male_total = female_survived = female_total = 0
    for passenger in passenger_list:
        if passenger[sex_index] == 'male':
            male_total += 1
            male_survived += int(passenger[surv_index])
        elif passenger[sex_index] == 'female':
            female_total += 1
            female_survived += int(passenger[surv_index])
    male_survival_rate = male_survived / male_total if male_total > 0 else 0
    female_survival_rate = female_survived / female_total if female_total > 0 else 0
    return (male_survival_rate, female_survival_rate)


test_list = [[1,1,3,"alice","female"],[2,0,2,"John","male"],[3,0,1,"Jane", "female"]]
print("TESTING", survival_rate_gender(test_list))

filename = 'titanic.csv'  
print("TESTING", survival_rate_gender(csv_reader(filename)))



# In[43]:


# Step 5: average_ticket_fare(passenger_list)

fare_index = 9
def average_ticket_fare(passenger_list):
    total_fare = sum(float(passenger[fare_index]) for passenger in passenger_list)
    average_fare = total_fare / len(passenger_list) if passenger_list else 0
    return average_fare


filename = 'titanic.csv'  
print("TESTING", average_ticket_fare(csv_reader(filename)))


# In[44]:


# Step 6 :main()

def main():
    filename = 'titanic.csv'  
    passenger_list = csv_reader(filename)

   
    longest_name = longest_passenger_name(passenger_list)
    total_survival_rate = total_survival_percentage(passenger_list)  
    gender_survival_rate = survival_rate_gender(passenger_list)  
    avg_ticket_fare = average_ticket_fare(passenger_list)  

    
    print("Longest Name: ", longest_name)
    print("Total Survival Percentage: {:.2f}".format(total_survival_rate))  
    print("Male Survival Percentage: {:.2f}".format(gender_survival_rate[0]))  
    print("Female Survival Percentage: {:.2f}".format(gender_survival_rate[1]))  
    print("Average Ticket Cost: {:.2f}".format(avg_ticket_fare))  


main()


# In[ ]:




