#!/usr/bin/python3

loginfail = 0  # counter for failed logins
loginsuccess = 0  # counter for successful POSTs
failed_ips = []  # list to store IP addresses of failed login attempts

# open the file for reading
with open("/home/student/mycode/attemptlogin/keystone.common.wsgi") as kfile:
    # loop over the file
    for line in kfile:
        # if this 'fail pattern' appears in the line...
        if "- - - - -] Authorization failed" in line:
            loginfail += 1  # increment fail counter
            # extract the IP address (assuming the IP is after "from" in the log line)
            parts = line.split(" ")
            ip_index = parts.index("from") + 1
            failed_ips.append(parts[ip_index])
        # if this 'success pattern' appears in the line...
        elif "POST /v3/auth/tokens" in line and "HTTP/1.1" in line:
            loginsuccess += 1  # increment success counter

print("The number of failed log in attempts is", loginfail)
print("The number of successful POST attempts is", loginsuccess)
print("IP addresses associated with failed login attempts:", failed_ips)

