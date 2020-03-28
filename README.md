# aws_assume_role4sh
aws assume role script for shell

## Prerequisite
aws-cli
python2 or python3

## How to use
### assume role
```shell
> python3 assume-role.py [account-no] [role-name] [session-name]
> source awskey
```

### return back to original account
```shell
> source unset.sh
```
