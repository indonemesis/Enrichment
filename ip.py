import json, webbrowser, pyperclip, time, requests, os
from dotenv import load_dotenv


string = input("Enter your string input\n")
data = json.loads(string)
IPs=[]
url = 'https://api.abuseipdb.com/api/v2/check'

#Getting credentials from dot env file [https://pypi.org/project/python-dotenv/]
load_dotenv('ip.env')
key = os.getenv('key')

headers = {
    'Accept': 'application/json',
    'Key': key
}
print("Entities in the alert: \n")
for i in range(len(data)):
    for k,v in data[i]['properties'].items():
        if k == 'accountName':
            print("Account Name : ", v)
        elif k == "address":
            IPs.append(v)
            print("IP address : ", v)
        else:
            pass

pyperclip.copy("IP enrichment:\n")

for IP_addr in IPs:
    a = "https://www.virustotal.com/gui/ip-address/%s/details" % IP_addr
    b = "https://www.abuseipdb.com/check/%s" % IP_addr
    c= "https://ipinfo.io/%s" %IP_addr

    webbrowser.open(a)
    #webbrowser.open(b)
    webbrowser.open(c)
    time.sleep(3)
    
    #Param for AbuseIPDB
    querystring = {
    'ipAddress': IP_addr,
    'maxAgeInDays': '90'
    }
    
    # API call for AbuseIPDB
    response = requests.request(method='GET', url=url, headers=headers, params=querystring)

    # Output for AbuseIPDB
    decodedResponse = json.loads(response.text)
    print (json.dumps(decodedResponse, sort_keys=True, indent=4))

    #Add useful text to clipboard
    pyperclip.copy("Checked " +a+ " , " +b+ " and " +c )
    pyperclip.copy(json.dumps(decodedResponse, sort_keys=True, indent=4))