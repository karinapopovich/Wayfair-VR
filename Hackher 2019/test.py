import requests

data = "<play_info><app_key>RQGGg5gAZChVCaDWh9TGR2PZG9bK3ZeY</app_key><url>https://karinapopovich.github.io/final.mp3</url><service>service</service><reason>reason</reason><message>message</message><volume>20</volume></play_info>"
r = requests.post("http://192.168.1.251:8090/speaker", data)
print r.text


print "Welcome to Oculus Rift+Bose SoundTouch!"


testVar = raw_input("What is your preferred volume?")
data = '<volume>' + testVar + '</volume>'
r = requests.post("http://192.168.1.251:8090/volume", data)
print r.text


testVar2 = raw_input("Give your bose system a name ")
data = "<name>testVar2</name>"
r = requests.post("http://192.168.1.251:8090/name", data)
print r.text


print "Thank you for setting up your Bose SoundTouch!"
