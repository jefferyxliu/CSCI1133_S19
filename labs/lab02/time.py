import time
time = int(time.time())
second = time%60
minute = (time//60)%60
hour = (time//3600)%24
if second < 10:
    second = '0'+str(second)
if minute < 10:
    minute = '0'+str(minute)
if hour < 10:
    hour = '0'+str(hour)
second = str(second)
minute = str(minute)
hour = str(hour)

print('The current time in Greenwich is ' + hour + ':' + minute + ':' + second)
