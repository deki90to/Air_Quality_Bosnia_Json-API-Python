from tkinter import *
import requests
import json

root = Tk()
root.title('Air Quality')
root.geometry('300x200')

try:
	api_request = requests.get('https://www.airnowapi.org/aq/observation/latLong/current/?format=application/json&latitude=44.640248&longitude=20.164318&distance=150&API_KEY=780A1A21-FCDC-41EC-8123-586D0525F8BE')
	api = json.loads(api_request.content)
	city = api[0]['ReportingArea']
	date = api[0]['DateObserved']
	time = api[0]['HourObserved']
	day = api[0]['LocalTimeZone']
	category = api[0]['Category']['Name']

except Exception as e:
	api = 'Error'

label = Label(root, text='' + 'City: ' + city +  '\nDate: ' + date \
	+ '\nTime: ' + str(time)+'h' + '\nDay: ' + day + '\nCategory: ' + category, \
	font=('Helvetica', 20), background='white')
label.pack()

root.mainloop()