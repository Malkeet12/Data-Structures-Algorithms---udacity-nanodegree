# names = input("enter name:").title().split(",")
# assignments = input("enter number of assignements:").split(",")
# grades = input("enter grades:").split(",")
#
# for index, name in enumerate(names):
#     message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
#     submit before you can graduate. You're current grade is {} and can increase \
#     to {} if you submit all assignments before the due date.\n\n".format(names[index], assignments[index],
#                                                                          grades[index],
#                                                                          int(grades[index]) + int(assignments[index]), )
#     print(message)

#
# def party_planner(cookies, people):
#     leftovers = None
#     num_each = None
#     # TODO: Add a try-except block here to
#     #       make sure no ZeroDivisionError occurs.
#     try:
#         num_each = cookies // people
#         leftovers = cookies % people
#     except ZeroDivisionError:
#         print("enter valid number")
#
#     return(num_each, leftovers)
#
# # The main code block is below; do not edit this
# lets_party = 'y'
# while lets_party == 'y':
#
#     cookies = int(input("How many cookies are you baking? "))
#     people = int(input("How many people are attending? "))
#
#     cookies_each, leftovers = party_planner(cookies, people)
#
#     if cookies_each:  # if cookies_each is not None
#         message = "\nLet's party! We'll have {} people attending, they'll each get to eat {} cookies, and we'll have {} left over."
#         print(message.format(people, cookies_each, leftovers))
#
#     lets_party = input("\nWould you like to party more? (y or n) ")

