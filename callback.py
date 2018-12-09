
import requests
r=requests.post('https://serene-wildwood-35121.herokuapp.com/oauth/changeUrl',{'clientId':'5bdb30e4203ce300150cb537','secret':"eb130fdfd5b678fdd19e4f2c8ab7e4bace85927a538caa34b7a7efb6ddc2f65b0c086bc3753abfe7c726c2e60e651a52a2995d596088de2d364e61e40453a504",'url':'http://192.168.43.169:3000/login/'})
print (r)



