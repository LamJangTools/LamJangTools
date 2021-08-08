from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import os, requests, ramdom
from time import sleep

version = requests.get('https://lamjangtools.github.io/LamJangTools/version.txt').text


os.system('cls')

def login(cookie):
	driver.get('https://cos.tv/')
	script = 'javascript:void(function(){ function setCookie(t) { var list = t.split("; "); console.log(list); for (var i = list.length - 1; i >= 0; i--) { var cname = list[i].split("=")[0]; var cvalue = list[i].split("=")[1]; var d = new Date(); d.setTime(d.getTime() + (7*24*60*60*1000)); var expires = ";domain=.cos.tv;expires="+ d.toUTCString(); document.cookie = cname + "=" + cvalue + "; " + expires; } } function hex2a(hex) { var str = ""; for (var i = 0; i < hex.length; i += 2) { var v = parseInt(hex.substr(i, 2), 16); if (v) str += String.fromCharCode(v); } return str; } setCookie("' + cookie + '"); location.href = "https://cos.tv"; })();'
	driver.execute_script(script)
	sleep(8)

def select_language(lang_num):
	while True:
		if lang_num == 1:
			lang_num = 3
			break
		elif lang_num == 2:
			lang_num = 6
			break
		else:
			lang_num = int(input('>>> Nhập sai, vui lòng nhập lại: '))
	set_language = driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/header/div/div/div[3]/div/div[2]/div/div[4]/div')
	set_language.click()
	sleep(0.8)
	set_language = driver.find_element_by_xpath(f'/html/body/div/div[1]/div[2]/header/div/div/div[3]/div/div[2]/div/div[4]/div/ul/li[{lang_num}]/a')
	set_language.click()
	sleep(3)

def follow_us():
	driver.get('https://cos.tv/channel/29812575005485056')
	sleep(3)
	follow = driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div[4]/a')
	follow.click()

def random_category():
	list_caterory = ['history', 'subscribe', 'recommended', 'nft', 'blockchain', 'gaming', 'interesting', 'pets', 'music']
	content = ramdom.choice(list_caterory)
	return content

def select_video(video_num, time_seen):
	select_video = driver.find_element_by_xpath(f'/html/body/div/div[2]/div/div/div[2]/div/div[2]/ul/li[{video_num}]/div/div[1]/a/img')
	select_video.click()
	sleep(time_seen)

def skip_noti():
	click = driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div[1]/div[1]/div[2]/div[1]/div[1]/div/div[1]/div/div[2]')
	click.click()
	sleep(1)

def play_video():
	play = driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div[1]/button')
	play.click()

def like():
	like = driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div[1]/div[1]/div[2]/div[1]/div[2]/div/div[2]/div/div[1]/div/div[3]/span[1]/div')
	like.click()
	sleep(8)

def comment(cmts):
	cmt = random.choice(cmts)
	comment = driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div[1]/div[5]/div/div[2]/div[1]/div[2]/div/div/form/div[1]/textarea')
	sleep(0.8)
	comment.send_keys(cmt)
	sleep(1.2)
	send_comment = driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div[1]/div[5]/div/div[2]/div[1]/div[2]/div/div/form/div[2]/div/div[3]/button[2]')
	send_comment.click()

def make_color():
	animation = ['[+] Tools đang LamJang bảo trì và update', '[x] Tools đang LamJang bảo trì và update']
	for ani in animation:
		print(ani, end='\r')
		sleep(0.3)

def logo():
	logo = '\033[1;36m' + f'''

			 /$$                                  /$$$$$                              
			| $$                                 |__  $$                              
			| $$        /$$$$$$  /$$$$$$/$$$$       | $$  /$$$$$$  /$$$$$$$   /$$$$$$ 
			| $$       |____  $$| $$_  $$_  $$      | $$ |____  $$| $$__  $$ /$$__  $$
			| $$        /$$$$$$$| $$ \ $$ \ $$ /$$  | $$  /$$$$$$$| $$  \ $$| $$  \ $$
			| $$       /$$__  $$| $$ | $$ | $$| $$  | $$ /$$__  $$| $$  | $$| $$  | $$
			| $$$$$$$$|  $$$$$$$| $$ | $$ | $$|  $$$$$$/|  $$$$$$$| $$  | $$|  $$$$$$$
			|________/ \_______/|__/ |__/ |__/ \______/  \_______/|__/  |__/ \____  $$
			                                                                 /$$  \ $$
			                                                                |  $$$$$$/
			                                                                 \______/ 


						\033[1;31mLamJang Tools\033[1;32m Version \033[1;34m{version}\033[1;0m

	'''
	print(logo)

# ====================================================================================================
logo()

# bắt đầu
print('''
		NHẤN PHÍM ĐỂ CHỌN NGÔN NGỮ
		[1]: TIẾNG ANH
		[2]: TIẾNG VIỆT
''')

lang_num = int(input('>>> Nhập số chọn ngôn ngữ: '))
loop = int(input('>>> Bạn tôi muốn xem/like/cmt mấy video: '))
time_seen = int(input('>>> Thời gian bạn muốn xem video? '))
print('''
>>> Nhập mỗi cmt cách nhau 1 dấu "|"
Ví dụ: LamJang chất quá | LamJang Nghệ An | SinCavn
để biểu thị cho 3 cmt đó là LamJang chất quá, LamJang Nghệ An và SinCavn

''')
cmts = input('>>> Nhập các comment: ').split(' | ')
follow = input('>>> Bạn có muốn Follow chúng tôi? [Y/N] ')
video_num = 1

os.system('cls')
logo()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(chrome_options = chrome_options)
f = open('cookies.txt', 'r', encoding='utf-8')
a = f.read().split('\n')
f.close()

cookie = a[0]
login(cookie)
select_language(lang_num)

f = open('checkfl.txt', 'r', encoding='utf-8')
check = f.read()
f.close()
if (follow in ['Y', 'y', 'YES', 'yes']) and 'unfollow' in check:
	follow_us()
	f = open('checkfl.txt', 'w+', encoding='utf-8')
	f.write('follow')
	f.close()
else:
	pass


while loop > 0:
	ids = random_category()
	driver.get(f'https://cos.tv/videos/list/{ids}')
	sleep(3)
	select_video(video_num, time_seen)
	skip_noti()
	play_video()
	like()
	comment(cmts)
	loop -= 1

sleep(10)

