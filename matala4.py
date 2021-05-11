import requests
def places ():
    file= open("dests.txt",encoding="utf8")
    destinations_list=list()
    for line in file:
            destinations_list.append(line.strip()) 
    for i in range(len(destinations_list)):
        distance(destinations_list[i]) 
    print(destinationsPerCity)
    listdistance=list()
    for k,v in destinationsPerCity.items():
        listdistance.append((v[0],k))
    listdistance.sort()
    print("The 3 furthest cities from Tel-aviv are:")
    listdistance=listdistance[-3:]
    for i in listdistance:
        print(i)

def distance(distance1):
    adress="תל אביב"
    api_key="מופיע בקובץ שהוגש במודל"
    url="https://maps.googleapis.com/maps/api/distancematrix/json?origins=%s&destinations=%s&key=%s" %(adress,distance1,api_key)
    response=requests.get(url).json()
    url2="https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s" %(distance1,api_key)
    response2=requests.get(url2).json()
    distance = response['rows'][0]['elements'][0]['distance']['text']
    duration = response['rows'][0]['elements'][0]['duration']['text']
    latitude = response2['results'][0]['geometry']['location']['lat']
    longitude = response2['results'][0]['geometry']['location']['lng']
    detailsPerCity = (distance, duration) + (latitude, longitude) 
    destinationsPerCity[distance1] = detailsPerCity 

    
    
destinationsPerCity=dict()
places ()
        


        
# ThreeHighest = nlargest(3, distanceandcity, key = distanceandcity.get)
# print("Dictionary with 3 highest values:")
# print(ThreeHighest)


