
# coding: utf-8

# In[114]:


import pylab as pl
import os
import json
import pandas as pd
import sys

try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib

apikey = sys.argv[1]
bus = sys.argv[2]
#csv_name = sys.argv[]    
    
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

print('Number of Active Bus:', num)
print('Bus Line:', bus)

# In[109]:


for i in range(num):
    
    Longitude = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    Latitude = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']

    print('Bus',i,'is at latitude:' , Latitude , ' and longitude:' , Longitude)
