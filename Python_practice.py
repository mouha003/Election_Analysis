# # How many votes did you get?

# my_votes = int(input("How many votes did you get in the election? "))

# # Toal votes in the election

# total_votes = int(input("What is the total votes in the election? "))

# # Calculate the percentage of votes you received.

# percentage_votes = (my_votes / total_votes) * 100

# print("I received " + str(percentage_votes)+ "% of the total vots.")

    # counties = ["Arapahoe", "Denver", "Jefferson"]

    # if counties[1] == 'Denver':
    #     print(counties[1])

    # if counties[3] != 'Jefferson':
    #     print(counties[2])

# temperature = int(input("What is the temperature outside? "))

# if temperature > 80:
#     print("Turn on the AC")
# else:
#     print("Open the windows.")

#What is the score?

# score = int(input("What is your test score?"))

# # Determine the grade.

# if score >= 90:
#     print('Your grade is an A.')
# else:
#     if score >= 80:
#         print('Your grade is a B.')
#     else:
#         if score >= 70:
#             print('Your grade is a C.')
#         else:
#             if score >= 60:
#                 print('Your grade is a D.')
#             else:
#                 print('Your grade is an F')

counties_tuple = ["Arapahoe", "Denver", "Jefferson"]

for i in range(len(counties_tuple)):
    print(counties_tuple[i])

for county in counties_tuple:
    print(county)


counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
print()
for county in counties_dict:
    print(counties_dict.get(county))

print(counties_dict.items())
print('\n')
for county, voters in counties_dict.items():
    print(county, "county has", voters, "registered voters.",'\n')

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

# for county_dict in voting_data:
#     print(county_dict)

# print()

# for i in range(len(voting_data)):
#     print(voting_data[i]['county'],voting_data[i]['registered_voters'] )


# for county_dict in voting_data:
#     print(county_dict.values())
#     print()

# for county_dict in voting_data:
#     print()
#     for value in counties_dict:
#         print(value)

# for county_dict in voting_data:
#     print(county_dict['registered_voters'])
#     print()


for county_dict in voting_data:
    for key, value in county_dict.items():
        print(value)

