import time
import os
codeTTL = 10 # Value is always in minutes
baseURL = "https://example.com/" # Example: https://example.com
jwtSecret = os.environ.get('JWT_SECRET') # Change it to your value
tokenMetaData = {}
tokenMetaData['iat'] = int(time.time())
tokenMetaData['nbf'] = int(time.time())
tokenMetaData['exp'] = int(time.time()) + codeTTL * 60
tokenMetaData['iss'] = baseURL
emailMetaData = {"smtp-server":os.environ.get('SMTP_SERVER'),"port":587,"username":os.environ.get('EMAIL_USERNAME'),"password":os.environ.get('EMAIL_PASSWORD'),"subject":"One Time Code","text":"One Time Code: "}