import re

import requests
import os


def main():
    with requests.get("https://hub.spigotmc.org/jenkins/job/BuildTools/lastSuccessfulBuild/artifact/target/BuildTools.jar") as r:
        with open("BuildTools.jar", "wb") as f:
            f.write(r.content)
    version = input("Enter Version [latest] ")
    if version == "" or version == "latest":
        version = "latest"
    os.system(f"\"C:\\Program Files\\Eclipse Adoptium\\jdk-17.0.4.8-hotspot\\bin\\java\" -jar BuildTools.jar --rev {version}")