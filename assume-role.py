#!/usr/bin/env python3
import os
import json
import sys

if len(sys.argv) != 4:
    sys.exit(0)
    
account_no = sys.argv[1] #111122223333
role_name = sys.argv[2] #"Administrator"
session_name = sys.argv[3] #"aws-assumed-role-session"

cmd = "aws sts --output json assume-role --role-arn arn:aws:iam::{}:role/{} --role-session-name {}".format(account_no, role_name, session_name)
output = os.popen(cmd).read()

creds = json.loads(output)

access_key_id = creds["Credentials"]["AccessKeyId"]
secret_access_key = creds["Credentials"]["SecretAccessKey"]
session_token = creds["Credentials"]["SessionToken"]

export_access_key_id = "export AWS_ACCESS_KEY_ID={} ".format(access_key_id)
export_secret_access_key = "export AWS_SECRET_ACCESS_KEY={} ".format(secret_access_key)
export_session_token =  "export AWS_SESSION_TOKEN={} ".format(session_token)

with open("awskey", "w") as f:
    f.writelines(export_access_key_id)
    f.writelines(export_secret_access_key)
    f.writelines(export_session_token)

print(export_access_key_id)
print(export_session_token)
print(export_secret_access_key)

