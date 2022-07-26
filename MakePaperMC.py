import requests

def main():
    api = "https://papermc.io/api/v2"
    name = input("Enter the server type [paper/waterfall/velocity]: ")
    version = input("Enter Version [latest] ")
    r = requests.get(f"{api}/projects/{name}")
    json = r.json()
    if version == "" or version == "latest":
        version = json["versions"][-1]
    else:
        if version not in json["versions"]:
            print("Version not found")
            return
    r = requests.get(f"{api}/projects/{name}/versions/{version}")
    json = r.json()
    latest_build = json["builds"][-1]
    print(f"Downloading {json['project_name']} {json['version']} build {latest_build}")
    print(f"{api}/projects/{name}/versions/{version}/builds/{str(latest_build)}/downloads/{name}-{version}-{latest_build}.jar")
    with requests.get(f"{api}/projects/{name}/versions/{version}/builds/{str(latest_build)}/downloads/{name}-{version}-{str(latest_build)}.jar") as r:
        with open(f"{name}-{version}-{str(latest_build)}.jar", "wb") as f:
            f.write(r.content)
