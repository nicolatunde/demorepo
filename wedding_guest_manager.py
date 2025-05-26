# Stage 1
confirmed_guests = ["Alice", "Charlie", "Eve", "Bob", "Frank", "Grace", "David", "Hannah", "Liam", "Mia"]
waitlist = []
print("\n\nStage 1")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)


# Stage 2
waitlist.extend(["Ken", "Jack", "Ivy"])
print("\n\nStage 2")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)


# Stage 3
waitlist.append("Noah")
waitlist.append("Oliver")
print("\n\nStage 3")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)