import os

API_KEY=os.environ.get('API_KEY')
API_KEY_SECRET=os.environ.get('API_KEY_SECRET')
BEARER_TOKEN=os.environ.get('BEARER_TOKEN')
ACCESS_TOKEN=os.environ.get('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET=os.environ.get('ACCESS_TOKEN_SECRET')

if __name__ == "__main__":
    print(1)
    # print(API_KEY,API_KEY_SECRET,BEARER_TOKEN,ACCESS_TOKEN,ACCESS_TOKEN_SECRET)