from __future__ import print_function
import time
import pychromecast

device_list = pychromecast.get_chromecasts_as_dict().keys()
if len(device_list) == 0:
    raise IOError('no cast devices in local network')

cast = pychromecast.get_chromecast(friendly_name=device_list[0])
cast.wait()
print (cast.device)
print (cast.status)

mc = cast.media_controller
mc.play_media('http://r10---sn-q4f7sne7.googlevideo.com/videoplayback?mime=video%2Fmp4&dur=283.306&upn=iRsXsWyqBk4&itag=22&ratebypass=yes&ip=2a03%3A8180%3A1001%3A16a%3A%3A8ee1&source=youtube&mm=31&mn=sn-q4f7sne7&id=o-AM6oFaf-9IXF918Fc-j1gDYz6Rr4-LJYTIS5AeQ4apjR&ms=au&mt=1454510670&mv=m&pl=40&key=yt6&initcwndbps=537500&sparams=dur%2Cid%2Cinitcwndbps%2Cip%2Cipbits%2Citag%2Clmt%2Cmime%2Cmm%2Cmn%2Cms%2Cmv%2Cnh%2Cpl%2Cratebypass%2Csource%2Cupn%2Cexpire&expire=1454532434&lmt=1447324598844667&ipbits=0&nh=IgpwcjA1LmRmdzA2KgkxMjcuMC4wLjE&fexp=9405191%2C9407610%2C9408210%2C9408522%2C9416126%2C9418200%2C9419451%2C9420452%2C9422342%2C9422571%2C9422596%2C9423661%2C9423662%2C9424006%2C9427317%2C9427365%2C9427850&sver=3&signature=90DA6BBB3CE2772928C7D165787398D81ADF1EAF.4558808405F713CC54FE4252382AE7BDBED1EB56&title=Shoot+The+Kuruvi+Official+Song+Video+From+Movie+Jil+Jung+Juk+By+Anirudh+%26+Vishal+Chandrashekhar', 'video/mp4')

time.sleep(5)
mc.pause()
time.sleep(2)
mc.play()
