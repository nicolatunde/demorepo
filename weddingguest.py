confirmed_guests_list = ["Alice", "Charlie", "Eve", "Bob", "Frank", "Grace", "David", "Hannah", "Liam", "Mia"]
waitlisted_guest_list = []
print("\n\nStage 1")
print("Confirmed guests: ", confirmed_guests_list)
print("Waitlist: ", waitlisted_guest_list)

# secondscenero
# confirmed_guests_list = ["Alice", "Charlie", "Eve", "Bob", "Frank", "Grace", "David", "Hannah", "Liam"  "Mia"]
waitlisted_guest_list.append("Ken")
waitlisted_guest_list.append("Jack")
waitlisted_guest_list.append("Ivy")
print("\n\nStage 2")
print("Confirmed guests: ", confirmed_guests_list)
print("Waitlist: ", waitlisted_guest_list)
# print(waitlisted_guest_list)

# third scenero
# confirmed_guests_list = ["Alice", "Charlie", "Eve", "Bob", "Frank", "Grace", "David", "Hannah", "Liam"  "Mia"]
waitlisted_guest_list.append("Noah")
waitlisted_guest_list.append("Oliver")
print("\n\nStage 3")
print("Confirmed guests: ", confirmed_guests_list)
print("Waitlist: ", waitlisted_guest_list)

# fourth scenero
confirmed_guests_list.remove("Alice")
# print(confirmed_guests_list)
confirmed_guests_list.append(waitlisted_guest_list[0])
waitlisted_guest_list.remove(waitlisted_guest_list[0])
print("\n\nStage 4")
print("Confirmed guests: ", confirmed_guests_list)
print("Waitlist: ", waitlisted_guest_list)

# fifth scenero
print ("Charlie" in confirmed_guests_list)
print("\n\nStage 5")
print("Confirmed guests: ", confirmed_guests_list)
print("Waitlist: ", waitlisted_guest_list)

# sixth scenero
confirmed_guests_list .remove("David")
confirmed_guests_list .remove("Eve")
print("\n\nStage 6")
print("Confirmed guests: ", confirmed_guests_list)
print("Waitlist: ", waitlisted_guest_list)

# seventh scenero
confirmed_guests_list .append(waitlisted_guest_list[0])
confirmed_guests_list .append(waitlisted_guest_list[1])
waitlisted_guest_list .remove(waitlisted_guest_list[0])
waitlisted_guest_list .remove(waitlisted_guest_list[0])
print("\n\nStage 7")
print("Confirmed guests: ", confirmed_guests_list)
print("Waitlist: ", waitlisted_guest_list)

# eight scenero
waitlisted_guest_list .remove(waitlisted_guest_list[1])
print("\n\nStage 8")
print("Confirmed guests: ", confirmed_guests_list)
print("Waitlist: ", waitlisted_guest_list)

# 9thscenero
print("\n Stage 9")
print('\n Last 3 guest on confirm list is :',confirmed_guests_list[-3:len(confirmed_guests_list)])

# 10th
confirmed_guests_list .append(waitlisted_guest_list[0])
waitlisted_guest_list.remove("Noah")
print("\n\nStage 10")
print("Confirmed guests: ", confirmed_guests_list)
print("Waitlist: ", waitlisted_guest_list)


# 11th
print("\n\nStage 11")
print("\n Number of confirm guest list is:",len(confirmed_guests_list))

# 12th\
confirmed_guests_list .sort()
print("\n\nStage 12")
print("Confirmed guests: ", confirmed_guests_list)
print("Waitlist: ", waitlisted_guest_list)

# 13th

confirmed_guests_list .remove(confirmed_guests_list[3])
confirmed_guests_list[-1] = ("Collins")
confirmed_guests_list .sort()
print("\n\nStage 13")
print("Confirmed guests: ", confirmed_guests_list)
print("Waitlist: ", waitlisted_guest_list)


print("\n\nStage 14")
guests_list_for_caterer = 'guests_list_for_caterer:'
guests_list_for_caterer = guests_list_for_caterer.title()
print(guests_list_for_caterer, confirmed_guests_list)

waitlisted_guest_list.clear()
print("\n\nStage 15")
print("Confirmed guests: ", confirmed_guests_list)
print("Waitlist: ", waitlisted_guest_list)















