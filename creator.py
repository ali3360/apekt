+#!/usr/bin/env python
 +# -*- coding: utf-8 -*-
 +import redis
 +import os
 +redis = redis.Redis('localhost')
 +id = input("Enter Tabchi ID (1,2,3,4,5,...) : ")
 +sudo = input("Enter Full Sudo ID : ")
 +source = os.popen("cat base.lua").read()
 +launcher = """while true; do
 +  ./telegram-cli-1222 -p jarchi-{} -s tabchi-{}.lua
 +done""".format(id,id)
 +source2 = source.replace("jarchi-ID",str(id))
 +newsource = open("tabchi-{}.lua".format(id),"w")
 +newsource.write(source2)
 +newsource.close()
 +newlauncher = open("jarchi-{}.sh".format(id),"w")
 +newlauncher.write(launcher)
 +newlauncher.close()
 +os.popen("chmod 777 jarchi-{}.sh".format(id))
 +redis.set("tabchi:{}:fullsudo".format(id),sudo)
 +print("Done!\nNew jarchi Created...\nID : {}\nFull Sudo : {}\nRun : ./jarchi-{}.sh".format(id,sudo,id))
