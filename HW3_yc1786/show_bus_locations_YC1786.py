
# coding: utf-8

# In[114]:


import pylab as pl
import os
import json
import pandas as pd
import sys
import csv

try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib

apikey = sys.argv[1]
bus = sys.argv[2]
csv_name = sys.argv[3]    
    
url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + apikey + "&VehicleMonitoringDetailLevel=calls&LineRef="+bus 


#print (url)
response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)


# In[106]:


data


# In[107]:


num = len(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])
num

file = open(csv_name,'w')
file.write('Latitude,Longitude,Stop Name,Stop Status\n')

# In[108]:

for i in range(num):
    
    Longitude = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    Latitude = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    try:
        stop_name = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][0]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
    except:
        stop_name = 'N/A'
    try:
        stop_status = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][0]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
    except:
        stop_status = 'N/A'
        
    file.write('%s,%s,%s,%s\n'%(Longitude,Latitude,stop_name,stop_status))

