import file_reader
import web_fetcher


list_of_names = file_reader.read_data('data.txt')
print('The list of names are: ', list_of_names)


users = web_fetcher.fetch_user_data()

print('List of users: ', users)