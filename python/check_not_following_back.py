import json

# File paths
following_file_path = 'C:/Users/Ardian/Downloads/following.json'
followers_file_path = 'C:/Users/Ardian/Downloads/followers_1.json'

def extract_usernames(json_file_path, key=None):
    with open(json_file_path, 'r') as file:
        data = json.load(file)
    
    usernames = set()
    
    if key:
        # For following file
        if key in data:
            data = data[key]
    
    # For both files, data should be a list
    for entry in data:
        for item in entry.get('string_list_data', []):
            usernames.add(item.get('value'))
    
    return usernames

# Extract usernames from both files
following_users = extract_usernames(following_file_path, 'relationships_following')
follower_users = extract_usernames(followers_file_path)

# Find users who are not following you back
not_following_back = following_users - follower_users

# Print the results
if not_following_back:
    print("These users are not following you back:")
    for user in not_following_back:
        print(user)
else:
    print("Everyone you follow is following you back!")
