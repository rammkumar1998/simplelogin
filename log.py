logs = [
    "user=alice ip=10.0.0.5",
    "user=bob ip=10.0.0.9",
    "user=alice ip=10.0.0.5",
    "user=alice ip=10.0.0.5",
    "user=carol ip=10.0.0.2",
    "user=bob ip=10.0.0.9",
    "user=bob ip=10.0.0.9",
    "user=bob ip=10.0.0.9",
    "user=alice ip=10.0.0.5",
    "user-alice ip=10.09.76.256"
]
alert = []
alert_username = {} 
username =[]
element = []
usernames_alert = []
alert_name = []
count = {}
hacker = []
for element in logs:
    alert.append(element.split(" "))
for part in alert:    
    if part[0] in alert_username and part[1] not in alert_username.values():
        alert_username.update({part[0]:part[1]})
    elif part[0] not in alert_username and part[1] not in alert_username.values():
        alert_username.update({part[0]:part[1]})
    elif part[0] in alert_username and part[1] in alert_username.values():
        usernames_alert.append(part[0])
for user in usernames_alert:
    if user in count:
        count[user]+=1
    else:
        count[user]=1
for key,value in count.items():
    if value>=3:
        hacker.append(key.split("="))
for person in hacker:
    print(f"{person[1]} has tried to login more than 2 times from same or different IP")
        



