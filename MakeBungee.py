import requests

def main():
    with requests.get("https://ci.md-5.net/job/BungeeCord/lastSuccessfulBuild/artifact/bootstrap/target/BungeeCord.jar") as r:
        with open("Bungeecord.jar", "wb") as f:
            f.write(r.content)