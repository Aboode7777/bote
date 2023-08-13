########## - StArt CoDe - ##########
import os
try:
	import requests
except ImportError:
	os.system('pip install requests')
try:
	import random
except ImportError:
	os.system('pip install random')
try:
	import threading
except ImportError:
	os.system('pip install clear')
try:
	import json
except ImportError:
	os.system('pip install json')
try:
	from user_agent import generate_user_agent
except ImportError:
	os.system('pip install user_agent')
try:
	import time
except:
	os.system('pip install time')
try:
	from AegosPy import *
except ImportError:
	os.system('pip install AegosPy')
	os.system('pip install stdiomask')
	os.system('pip install OneClick')
Z = '\033[1;31m'
X = '\033[1;33m'
F = '\033[2;32m'
C = "\033[1;97m"
B = '\033[2;36m'
Y = '\033[1;34m'
C = "\033[1;97m"
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
id=input(f"{B}-{C} EntEr YoUr iD {X}:{F} ")
token=input(f"{B}-{C} EntEr YoUr ToKen {X}:{F} ")
time.sleep(1)
print(f"{X}[{F} ✓ {X}]{C} Done Login is Tool")
time.sleep(2)
os.system('clear')
user1='qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm'
number='6789'
def Gmail():
	rng=int("".join(random.choice(number)for i in range(1)))
	name=str("".join(random.choice(user1)for i in range(rng)))
	url = f'https://livecounts.xyz/api/tiktok-live-follower-count/search/{name}'
	response=requests.get(url).json()
	aa=0
	try:
		while True:
			aa+=1
			user=response['results'][aa]['username']
			Email=user+'@gmail.com'
			#print(user)
			Response = AegosPy.CheckTik(Email)
			if Response['Status']=='OK':
				print(f'{B}- {X}GooD TikTok {F}: {C}{Email}')
				Response = AegosPy.A_Gmail(user+'@gmail.com')
				if Response['Status']=='Available':
					print(f'{B}- {F}GooD GmAil {X}: {C}{Email}')
					Response = AegosPy.GetInfoTik(user)
					Id = Response['id']
					Name = Response['name']
					Bio = Response['bio']
					Region = Response['code-country']
					Private = Response['private']
					Followers = Response['followers']
					Following = Response['following']
					Likes = Response['likes']
					VideoCount = Response['video']
					text=('UserName : {}\nEmail : {}@gmail.com\nId : {}\nName : {}\nBio : {}\nRegion : {}\nPrivate : {}\nFollowers : {}\nFollowing : {}\nLikes : {}\nVideoCount : {}\nProgrammer : @Stef_Python'.format(user,user,Id,Name,Bio,Region,Private,Followers,Following,Likes,VideoCount))
					requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text={text}')
				else:
					print(f'{B}-{Z} BaD GmAil {F}:{C} {Email}')
			else:
				print(f'{B}-{Z} BaD TikTok {F}:{C} {Email}')
	except:Gmail()
def Yahoo():
	rng=int("".join(random.choice(number)for i in range(1)))
	name=str("".join(random.choice(user1)for i in range(rng)))
	url = f'https://livecounts.xyz/api/tiktok-live-follower-count/search/{name}'
	response=requests.get(url).json()
	aa=0
	try:
		while True:
			aa+=1
			user=response['results'][aa]['username']
			Email=user+'@yahoo.com'
			#print(user)
			Response = AegosPy.CheckTik(Email)
			if Response['Status']=='OK':
				print(f'{B}- {X}GooD TikTok {F}: {C}{Email}')
				Response = AegosPy.A_Yahoo(Email)
				if Response['Status']=='Available':
					print(f'{B}- {F}GooD YaHoo {X}: {C}{Email}')
					Response = AegosPy.GetInfoTik(user)
					Id = Response['id']
					Name = Response['name']
					Bio = Response['bio']
					Region = Response['code-country']
					Private = Response['private']
					Followers = Response['followers']
					Following = Response['following']
					Likes = Response['likes']
					VideoCount = Response['video']
					text=('UserName : {}\nEmail : {}@yahoo.com\nId : {}\nName : {}\nBio : {}\nRegion : {}\nPrivate : {}\nFollowers : {}\nFollowing : {}\nLikes : {}\nVideoCount : {}\nProgrammer : @Stef_Python'.format(user,user,Id,Name,Bio,Region,Private,Followers,Following,Likes,VideoCount))
					requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text={text}')
				else:
					print(f'{B}-{Z} BaD YaHoo {F}:{C} {Email}')
			else:
				print(f'{B}-{Z} BaD TikTok {F}:{C} {Email}')
	except:Yahoo()
def Hotmail():
	rng=int("".join(random.choice(number)for i in range(1)))
	name=str("".join(random.choice(user1)for i in range(rng)))
	url = f'https://livecounts.xyz/api/tiktok-live-follower-count/search/{name}'
	response=requests.get(url).json()
	aa=0
	try:
		while True:
			aa+=1
			user=response['results'][aa]['username']
			Email=user+'@hotmail.com'
			#print(user)
			Response = AegosPy.CheckTik(Email)
			if Response['Status']=='OK':
				print(f'{B}- {X}GooD TikTok {F}: {C}{Email}')
				Response = AegosPy.A_Hotmail(Email)
				if Response['Status']=='Available':
					print(f'{B}- {F}GooD Hotmail {X}: {C}{Email}')
					Response = AegosPy.GetInfoTik(user)
					Id = Response['id']
					Name = Response['name']
					Bio = Response['bio']
					Region = Response['code-country']
					Private = Response['private']
					Followers = Response['followers']
					Following = Response['following']
					Likes = Response['likes']
					VideoCount = Response['video']
					text=('UserName : {}\nEmail : {}@hotmail.com\nId : {}\nName : {}\nBio : {}\nRegion : {}\nPrivate : {}\nFollowers : {}\nFollowing : {}\nLikes : {}\nVideoCount : {}\nProgrammer : @Stef_Python'.format(user,user,Id,Name,Bio,Region,Private,Followers,Following,Likes,VideoCount))
					requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text={text}')
				else:
					print(f'{B}-{Z} BaD HotMail {F}:{C} {Email}')
			else:
				print(f'{B}-{Z} BaD TikTok {F}:{C} {Email}')
	except:Hotmail()
def Aol():
	rng=int("".join(random.choice(number)for i in range(1)))
	name=str("".join(random.choice(user1)for i in range(rng)))
	url = f'https://livecounts.xyz/api/tiktok-live-follower-count/search/{name}'
	response=requests.get(url).json()
	aa=0
	try:
		while True:
			aa+=1
			user=response['results'][aa]['username']
			Email=user+'@aol.com'
			#print(user)
			Response = AegosPy.CheckTik(Email)
			if Response['Status']=='OK':
				print(f'{B}- {X}GooD TikTok {F}: {C}{Email}')
				Response = AegosPy.A_Aol(Email)
				if Response['Status']=='Available':
					print(f'{B}- {F}GooD AoL {X}: {C}{Email}')
					Response = AegosPy.GetInfoTik(user)
					Id = Response['id']
					Name = Response['name']
					Bio = Response['bio']
					Region = Response['code-country']
					Private = Response['private']
					Followers = Response['followers']
					Following = Response['following']
					Likes = Response['likes']
					VideoCount = Response['video']
					text=('UserName : {}\nEmail : {}@aol.com\nId : {}\nName : {}\nBio : {}\nRegion : {}\nPrivate : {}\nFollowers : {}\nFollowing : {}\nLikes : {}\nVideoCount : {}\nProgrammer : @Stef_Python'.format(user,user,Id,Name,Bio,Region,Private,Followers,Following,Likes,VideoCount))
					requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text={text}')
				else:
					print(f'{B}-{Z} BaD AoL {F}:{C} {Email}')
			else:
				print(f'{B}-{Z} BaD TikTok {F}:{C} {Email}')
	except:Aol()
def MailRu():
	rng=int("".join(random.choice(number)for i in range(1)))
	name=str("".join(random.choice(user1)for i in range(rng)))
	url = f'https://livecounts.xyz/api/tiktok-live-follower-count/search/{name}'
	response=requests.get(url).json()
	aa=0
	try:
		while True:
			aa+=1
			user=response['results'][aa]['username']
			Email=user+'@mail.ru'
			#print(user)
			Response = AegosPy.CheckTik(Email)
			if Response['Status']=='OK':
				print(f'{B}- {X}GooD TikTok {F}: {C}{Email}')
				Response = AegosPy.A_MailRu(Email)
				if Response['Status']=='Available':
					print(f'{B}- {F}GooD MailRu {X}: {C}{Email}')
					Response = AegosPy.GetInfoTik(user)
					Id = Response['id']
					Name = Response['name']
					Bio = Response['bio']
					Region = Response['code-country']
					Private = Response['private']
					Followers = Response['followers']
					Following = Response['following']
					Likes = Response['likes']
					VideoCount = Response['video']
					text=('UserName : {}\nEmail : {}@mail.ru\nId : {}\nName : {}\nBio : {}\nRegion : {}\nPrivate : {}\nFollowers : {}\nFollowing : {}\nLikes : {}\nVideoCount : {}\nProgrammer : @Stef_Python'.format(user,user,Id,Name,Bio,Region,Private,Followers,Following,Likes,VideoCount))
					requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text={text}')
				else:
					print(f'{B}-{Z} BaD MailRu {F}:{C} {Email}')
			else:
				print(f'{B}-{Z} BaD TikTok {F}:{C} {Email}')
	except:MailRu()
try:
	choice=input(f"{X}[{C} 1 {X}]{B} - {C}Domin Gmail\n{X}[{C} 2 {X}]{B} -{C} Domin Yahoo\n{X}[ {C}3{X} ]{B} - {C}Domin HotMail\n{X}[{C} 4{X} ]{B} - {C}Domin Aol\n{X}[{C} 5 {X}]{B} - {C}Domin Mail.Ru\n{X}[{C} 0 {X}]{B} - {C}Account is Programmer\n\n{C} Choice {X}:{F} ")
	if choice=='1':
		Gmail()
	elif choice=='2':
		Yahoo()
	elif choice=='3':
		Hotmail()
	elif choice=='4':
		Aol()
	elif choice=='5':
		MailRu()
	elif choice=='0':
		from webbrowser import *
		link='https://t.me/Stef_Python'
		open(link)
		print(f'{X}[ {F}✓ {X}] {C} User Programmer : @Stef_Python')
except:os.system('clear');print(Z+'- Error Number')
######### - Code expired - #########
