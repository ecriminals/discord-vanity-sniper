from requests import Session

class Client:
    def __init__(self, id: int = "", token: str = ""):
        self.session = Session()
        self.token = token
        self.id = id

    def headers(self):
        return {
            "authority": "discord.com",
            "x-discord-locale": "en-US",
            "x-debug-options": "bugReporterEnabled",
            "accept-language": "en-US",
            "authorization": self.token,
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9007 Chrome/91.0.4472.164 Electron/13.6.6 Safari/537.36",
            "accept": "*/*",
            "origin": "https://discord.com",
            "sec-fetch-site": "same-origin",
            "sec-fetch-mode": "cors",
            "sec-fetch-dest": "empty",
        }

    def snipe(self, vanity: str = ""):
        if vanity != None:
            base = self.session.get(
                f"https://discord.com/api/v9/invites/{vanity}",
                headers=Client.headers(self),
            ).text

        if "vanity_url_code" in base:
            return f">> [system ] {vanity} taken. :: {self.id}"

        elif "Unknown Invite" in base:
            snipe = self.session.patch(
                f"https://discord.com/api/v9/guilds/{self.id}/vanity-url",
                headers=Client.headers(self),
                json={"code": vanity},
            ).text

        if vanity in snipe:
            return f">> [system] {vanity} sniped! :: {self.id}"
        else:
            return snipe
