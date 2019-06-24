from burp import IBurpExtender
import sys
import json
#currently this pulls in the IPs from "test-ips.txt" and loads them as options - works

class BurpExtender(IBurpExtender):
  #required
  def registerExtenderCallbacks(self,callbacks):
    #set our extension name
    callbacks.setExtensionName("Import Raw IPs")
    #write message to alerts tab
    #callbacks.issueAlert("hello alerts")
    basejson = """
    {
        "target":{
            "scope":{
                "exclude":[
                    {
                        "enabled":true,
                        "file":"logout",
                        "protocol":"any"
                    },
                    {
                        "enabled":true,
                        "file":"logoff",
                        "protocol":"any"
                    },
                    {
                        "enabled":true,
                        "file":"exit",
                        "protocol":"any"
                    },
                    {
                        "enabled":true,
                        "file":"signout",
                        "protocol":"any"
                    }
                ],
                "include":[
                ]
            }
        }
    }
    """
    ipfile = open('test-ips.txt') #open file of IPs (one per line)
    iplist = ipfile.readlines()
    dictjson = json.loads(basejson) #load base json data structure
    for ip in iplist:
      newip = {"enabled":True, "host":ip.strip(), "protocol":"any"}
      dictjson['target']['scope']['include'].append(newip) #appends new IP entry to python dict

    callbacks.loadConfigFromJson(json.dumps(dictjson))

    #jsonout = open("jsonout.txt", "w")
    #jsonout.write(json.dumps(dictjson))
    #print("wrote to jsonout.txt")


    