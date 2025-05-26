# iterable => list, dictionaires, tuples, sets


# shopping_list = ["yam", "eggs", "sardine", "oil", "tomato", "maggi", "salt", "pepper", "chicken", "onions", "sardine"]


# print(shopping_list[-2])

# print("before: ", shopping_list)
# shopping_list.remove("onions")

# shopping_list[-2] = "fish"
# shopping_list[4] = "tomatoes"

# shopping_list.append("curry")
# print("yam" not in shopping_list)
# list methods work in place
# print("after:  ", shopping_list)


# Create a list called means_of_transport containing bicycle, keke, plane, car, train, ship, boat, canoe, rocket
# Give me the first 3 items in the list
# Give me the 4th item in the list
# Check if plane is in the list
# Give me the second to the last item using -ve indexing.
# Add lorry to the end of the list
# Remove keke from the list
# Change `bicycle` to `bike`

# means_of_transport = ["bicycle", "keke", "plane", "car", "train", "ship", "boat", "canoe", "rocket"]
# means_of_transport[0] = 'bike'
# print(means_of_transport[5:8])
# means_of_transport[5:8] = ['yatch']

# means_of_transport[3:5] = ['van', 'jet']


# means_of_transport = ["bicycle", "keke", "plane", "car", "train", "ship", "boat", "canoe", "rocket"]

# print("before: ", means_of_transport)
# means_of_transport.insert(1, "trailer")
# means_of_transport.insert(0, "limo")
# print(len(means_of_transport))
# print(type(means_of_transport))

# print("after:  ", means_of_transport)


# means_of_transport = ("bicycle", "keke", "plane", "car", "train", "ship", "boat", "canoe", "rocket")
# print(type(means_of_transport))
# means_of_transport = list(means_of_transport)
# print(means_of_transport)
# print(type(means_of_transport))


# days = "Thursday Friday"
# print(list(days))
# print(days.split())


# means_of_transport = ["bicycle", "keke", "plane", "car", "train"]
# other_means_of_transport = ("ship", "boat", "canoe", "rocket")

# means_of_transport.extend(other_means_of_transport)
# print(means_of_transport)

# import copy

# tv_shows = ["friends", "Big Brother Naija", "Young Sheldon", "Food Network", "Silo", "Blacklist", "Blindspot"]
# print("before: ", tv_shows)
# # tv_shows.remove("something")

# # tv_shows.clear()
# # tv_shows = []
# tv_shows.sort(key=str.upper)
# tv_shows.reverse()
# tv_shows = tv_shows[::-1]
# copy_tv_shows = tv_shows.copy()
# copy_tv_shows = copy.deepcopy(tv_shows)
# print('copyjkbjnjnjbjkjbjk',copy_tv_shows)

# del tv_shows[1]
# popped_item = tv_shows.pop(3)
# print(popped_item)

# print("after:  ", copy_tv_shows)

# nums = [78, 24, 5678, 1, 35667, 87]
# nums.sort(reverse=True)
# print(nums)


# # means_of_transport = ["bicycle", "keke", "plane", "car", "train"]
# # other_means_of_transport = ["ship", "boat", "canoe", "rocket"]
# # means_of_transport.extend(other_means_of_transport)
# # print(means_of_transport)
# # all_transport_means = means_of_transport + other_means_of_transport
# # print(all_transport_means)


# # matrix = [
# #     [1, 2, 3],
# #     [4, 5, 6],
# #     [7, 8, 9]
# # ]

# # print(matrix[1][2])
# # print(matrix[2][1])
# # print(matrix[-3][-2])


# nested_list = [
#     ["Alice", "Bob"],
#     [10, 20, 30],
#     [True, False]
# ]
# print(nested_list[1][1])
# print(nested_list[0][1][1])
# print(nested_list[0][0][1:])
# print(nested_list[1][0] + nested_list[1][2])

# nested_list[2][1] = 100
# print(nested_list[2][1] is 100)
# print(nested_list)


# means_of_transport = ["bicycle", "keke", "plane", "car", "train", "ship", "boat", "canoe", "rocket"]
# means_of_transport[0] = 'bike'
# print(means_of_transport[5:8])
# means_of_transport[5:8] = ['yatch']
# print(means_of_transport)


# means_of_transport = ["bicycle", "keke", "plane", "car", "train", "ship", "boat", "canoe", "rocket"]

# print("before: ", means_of_transport)
# means_of_transport.insert(1, "trailer")
# means_of_transport.insert(0, "limo")
# print(len(means_of_transport))
# print(type(means_of_transport))

# print("after:  ", means_of_transport)

tv_shows = ["friends", "Big Brother Naija", "Young Sheldon", "Food Network", "Silo", "Blacklist", "Blindspot", "2", "1"]
tv_shows.sort()
print(tv_shows)
