# C_VERSIONS_CACHE="$PWD/version_manifest.json"
# curl -sS https://launchermeta.mojang.com/mc/game/version_manifest.json > "$MC_VERSIONS_CACHE"
# read -p "Version [latest]: " input
# input="${input:-latest}"
# if [[ "$input" == "latest" ]]; then
# 	read -p "Release or Snapshot [R/S]: " input2
# 	if [[ "$input2" == "S" ]]; then
# 		JSON="$PWD/_snapshot.json"
# 		LATEST_SNAPSHOT="$(cat $MC_VERSIONS_CACHE | jq -r '{latest: .latest.snapshot} | .[]')"
# 		echo "Version:  $LATEST_SNAPSHOT"
# 		SNAPSHOT_URL="$(cat $MC_VERSIONS_CACHE | jq -r "{versions: .versions} | .[] | .[] | select(.id == \"$LATEST_SNAPSHOT\") | {url: .url} | .[]")"
# 		curl -sS "$SNAPSHOT_URL" > "$JSON"
# 		SNAPSHOT_SERVER_JAR_URL="$(cat $JSON | jq -r '{url: .downloads.server.url} | .[]')"
# 		if [ ! -f "$LOCAL_SNAPSHOT_JAR" ]; then
# 		  wget "$SNAPSHOT_SERVER_JAR_URL"
# 		fi
# 		ln -sf "minecraft_server.$LATEST_SNAPSHOT.jar" "$JSON"
# 		rm "$JSON" "$MC_VERSIONS_CACHE"
# 	elif [[ "$input2" == "R" ]]; then
# 		JSON="$PWD/_release.json"
# 		LATEST_RELEASE="$(cat $MC_VERSIONS_CACHE | jq -r '{latest: .latest.release} | .[]')"
# 		echo "Version:  $LATEST_RELEASE"
# 		RELEASE_URL="$(cat $MC_VERSIONS_CACHE | jq -r "{versions: .versions} | .[] | .[] | select(.id == \"$LATEST_RELEASE\") | {url: .url} | .[]")"
# 		curl -sS "$RELEASE_URL" > "$JSON"
# 		RELEASE_SERVER_JAR_URL="$(cat $JSON | jq -r '{url: .downloads.server.url} | .[]')"
# 		if [ ! -f "$LOCAL_RELEASE_JAR" ]; then
# 		  wget "$RELEASE_SERVER_JAR_URL"
# 		fi
# 		ln -sf "minecraft_server.$LATEST_RELEASE.jar" "$JSON"
# 		rm "$JSON" "$MC_VERSIONS_CACHE"
# 	fi
# else
# 	JSON="$PWD/_$input.json"
# 	echo "Version:  $input"
# 	URL="$(cat $MC_VERSIONS_CACHE | jq -r "{versions: .versions} | .[] | .[] | select(.id == \"$input\") | {url: .url} | .[]")"
# 	curl -sS "$URL" > "$JSON"
# 	SERVER_JAR_URL="$(cat $JSON | jq -r '{url: .downloads.server.url} | .[]')"
# 	if [ ! -f "$JAR" ]; then
# 	  wget "$SERVER_JAR_URL"
# 	fi
# 	ln -sf "minecraft_server.$input.jar" "$JSON"
# 	rm  "$JSON" "$MC_VERSIONS_CACHE"
# fi
import os
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
