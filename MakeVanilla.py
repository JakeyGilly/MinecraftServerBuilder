import requests
import json
def main():
    r = requests.get("https://launchermeta.mojang.com/mc/game/version_manifest.json")
    jsoncontent = r.json()
    inputted = False
    while not inputted:
        versioninput = input("Enter version [latest]: ")
        if versioninput == "" or versioninput == "latest":
            inputted2 = False
            while not inputted2:
                releaseinput = input("Release or Snapshot [R/S]: ")
                if releaseinput.upper() == "R":
                    release = True
                    versioninput = jsoncontent["latest"]["release"]
                elif releaseinput.upper() == "S":
                    release = False
                    versioninput = jsoncontent["latest"]["snapshot"]
                inputted2 = True
            inputted = True
        else:
            for version in jsoncontent["versions"]:
                if version["id"] == versioninput:
                    inputted = True
                    break
    for version in jsoncontent["versions"]:
        if version["id"] == versioninput:
            with requests.get(version["url"]) as r:
                if release:
                    with open("_release.json", "wb") as f:
                        f.write(r.content)
                else:
                    with open("_snapshot.json", "wb") as f:
                        f.write(r.content)
    with open("_release.json" if release else "_snapshot.json", "r") as f:
        content = f.read()
        jsoncontent = json.loads(content)
        with requests.get(jsoncontent["downloads"]["server"]["url"]) as r:
            with open("minecraft_server." + versioninput + ".jar", "wb") as f:
                f.write(r.content)
