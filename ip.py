import json, webbrowser, pyperclip, time

string = input("Enter your string input\n")
data = json.loads(string)
IPs=[]
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
    webbrowser.open(b)
    webbrowser.open(c)
    time.sleep(3)
    pyperclip.copy("Checked " +a+ " , " +b+ " and " +c )