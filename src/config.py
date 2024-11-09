import os

# LEETCODE_API_HOST=os.environ.get('LEETCODE_API_HOST','http://localhost')
# LEETCODE_API_PORT=os.environ.get('LEETCODE_API_PORT','3000')
# LEETCODE_API_BASE_URL= f"{LEETCODE_API_HOST}:{LEETCODE_API_PORT}"

LEETCODE_API_BASE_URL= os.environ.get('LEETCODE_API','http://localhost:3003') 

BOT_TOKEN = os.environ.get('BOT_TOKEN')
CHANNEL_ID =  int(os.environ.get('CHANNEL_ID')) 

SLEEP_TIME=3600