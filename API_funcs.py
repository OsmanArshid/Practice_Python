import requests

# ===========================================================================================================
# ===========================================================================================================

x = requests.get('https://w3schools.com/python/demopage.htm')
print(x.text)
# used for HTML response data (as a string) only


x_data = x.json()
# used for when we retrieve actual data --> JSON --> (JSON API) from URLS

# ===========================================================================================================
# ===========================================================================================================

def get_posts():
    url = "https://blahblah.com/api/posts"

    try:
        request = requests.get(url)
        # request is the response object
        
        if request.status_code == 200:
            # json() returns a dictionary --> parsed from the response body as JSON
            return request.json()
        else:
            return None
    
    except requests.exceptions.RequestException as e:
        print("Error: ", e)
        return None

# ===========================================================================================================
# ===========================================================================================================

def get_post(post_id):
    url = f"https://blahblah.com/api/posts/{post_id}"

    try: 
        request = requests.get(url)

        if request.status_code == 200:
            return request.json()
        else:
            return None
    
    except requests.exceptions.RequestException as e:
        print("Error: ", e)
        return None

# ===========================================================================================================
# ===========================================================================================================

# some_data is a dictionary
def create_post(some_data):
    url = "https://blahblah.com/api/post"

    try:
        req = requests.post(url = url, json = some_data)

        if req.status_code == 200:
            return req.json()
        else:
            return None

    except requests.exceptions.RequestException as e:
        print("Error: ", e)
        return None

# ===========================================================================================================
# ===========================================================================================================

# parameter data is a dictionary
def update_post(post_id, data):
    url = f"https://blahblah.com/api/posts/{post_id}"

    try:
        request = requests.put(url, json=data)

        if request.status_code == 200:
            return request.json()
        else:
            return None
    
    except requests.exceptions.RequestException as e:
        print("Error: ", e)
        return None

# if the "post_id" exists, update the post
# if the "post_id" does not exist, returns error


# ===========================================================================================================
# ===========================================================================================================

# parameter data is a dictionary
def patch_post(post_id, data):
    url = f"https://blahblah.com/api/posts/{post_id}"

    try:
        # HTTP runs over TCP
        # Patch Method is sent as a JSON Patch
        request = requests.patch(url, json=data)

        if request.status_code == 200:
            return request.json()
        else:
            return None
    
    except requests.exceptions.RequestException as e:
        print("Error: ", e)
        return None

# ===========================================================================================================
# ===========================================================================================================

def delete_post(post_id):
    url = f"https://blahblah.com/api/posts/{post_id}"

    try:
        request = requests.delete(url)

        if request.status_code == 200:
            return request.json()
        else:
            return None
    
    except requests.exceptions.RequestException as e:
        print("Error: ", e)
        return None

# ===========================================================================================================
# ===========================================================================================================

def get_headers():
    url = "https://blahblah.com/api/posts"

    try:
        request = requests.head(url)

        if request.status_code == 200:
            # x.headers --> to get the headers of the response
            return request.headers
        else:
            return None
    
    except requests.exceptions.RequestException as e:
        print("Error: ", e)
        return None

# ===========================================================================================================
# ===========================================================================================================

from requests.auth import HTTPBasicAuth

def get_by_auth(username, password):
    private_url = "http://blahblah.com/api/posts"
    try:
        req = requests.get(url = private_url, auth = HTTPBasicAuth(username, password))

        if req.status_code == 200:
            return req.json()
        else:
            return None

    
    except requests.exceptions.RequestException as e:
        print("Error: ", e)
        return None
    

# ===========================================================================================================
# ===========================================================================================================
# How do you send a file with a POST request in Python?
# You can send a file with a POST request by passing a dictionary to the files parameter. For example:


url = "https://example.com/upload"
file_path = "/path/to/my/file.txt"

with open(file_path, 'rb') as file:
    # someFiles is a dictionary with key 'file' and value as file object
    someFiles = {'file' : file}
    response = requests.post(url=url, files = someFiles)

print(response.status_code)

# ===========================================================================================================
# ===========================================================================================================
# How can you handle timeouts when making HTTP requests with the Python requests module?
# You can handle timeouts by specifying the timeout parameter in your request. This parameter takes a value in seconds. For example:

def time_out_get():
    url = "blahblah.com/posts"

    try:
        response = requests.get(url, timeout = 5)  
        print(response.json())

    except requests.Timeout:
        print("The request timed out")


# ===========================================================================================================
# ===========================================================================================================
