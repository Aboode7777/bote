import requests, random, re

class proxies:
	def get():
		channel = random.choice(["ProxyMTProto","proxymtprotoir"])
		proxies = list(set(re.findall(f'url_button" href="(.*?)"', requests.get(f"https://t.me/s/{channel}").text.replace("amp;", ""))))
		return proxies

print(proxies.get())
