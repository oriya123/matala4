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
    try:
        adress="תל אביב"
        api_key="AIzaSyCClFfCKHUrEUbLlQ2sR6hj8s6Wz2suEow"
        url="https://maps.googleapis.com/maps/api/distancematrix/json?origins=%s&destinations=%s&key=%s" %(adress,distance1,api_key)
        response=requests.get(url).json()
        url2="https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s" %(distance1,api_key)
        response2=requests.get(url2).json()
        distance =response['rows'][0]['elements'][0]['distance']['text']
        duration = response['rows'][0]['elements'][0]['duration']['value']
        latitude = response2['results'][0]['geometry']['location']['lat']
        longitude = response2['results'][0]['geometry']['location']['lng']
        if((duration/3600)<1):
            duration=duration/60
            duration=str(duration) +""+ 'min'
        else:
            hours=int(duration/3600)
            min=round(((duration%3600)/3600)*60,2)
            duration=str(hours)+' hours '+ str(min)+ ' min '
        detailsPerCity = (distance, duration) + (latitude, longitude) 
        destinationsPerCity[distance1] = detailsPerCity
    except:
        print("לא מזהה את הערך" +" "+ distance1)
    
    
destinationsPerCity=dict()
places ()
        







