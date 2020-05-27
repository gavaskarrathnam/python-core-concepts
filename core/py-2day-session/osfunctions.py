import os
from datetime import date
from datetime import datetime

path = os.getcwd()
print("Current working directory : %s " % path)

'''
strftime arguments date

%Y / %y - Year
%B / %b - Month
%A / %a - Day
%D / %d - Date

'''
today = date.today()
today_with_format = (str(today.day) + '-' + str(today.month) + '-' + str(today.year))
os.mkdir(today_with_format)
os.makedirs(today_with_format, )


now = datetime.now()
print(now.strftime("%d"+"-"+"%b"+"-"+"%Y"))


print("".join(reversed("12345")))

