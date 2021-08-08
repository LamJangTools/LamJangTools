from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

driver = webdriver.Chrome(chrome_options = chrome_options)

# driver.get('https://www.cos.tv')

cookie = 'serverSessionId=s%3AT1v_gyD2U3VCofl97E8AkvrPnjPDDGPH.ix%2BBBw6%2F3OMEyGxU1ORyJFbEFwiIIKOf98y9faQMZZk; XSRF-TOKEN=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIyOTgxMjU3NTAwNTQ4NTA1NiIsImlhdCI6MTYyODMxMzc5NCwiZXhwIjoxNjI4NDAwMTk0fQ.1vv_rDZXB3EHJ0-OReJj2eq5sn_KrPGMn0YKDxO90oM; isShowVideoDialog=1; uuid=308348e7-54ac-47d9-8b12-9afc3f2582a4'

def loginFacebookByCookie(cookie):
    script = 'javascript:void(function(){ function setCookie(t) { var list = t.split("; "); console.log(list); for (var i = list.length - 1; i >= 0; i--) { var cname = list[i].split("=")[0]; var cvalue = list[i].split("=")[1]; var d = new Date(); d.setTime(d.getTime() + (7*24*60*60*1000)); var expires = ";domain=.cos.tv;expires="+ d.toUTCString(); document.cookie = cname + "=" + cvalue + "; " + expires; } } function hex2a(hex) { var str = ""; for (var i = 0; i < hex.length; i += 2) { var v = parseInt(hex.substr(i, 2), 16); if (v) str += String.fromCharCode(v); } return str; } setCookie("' + cookie + '"); location.href = "https://cos.tv"; })();'
    driver.execute_script(script)


driver.get("https://cos.tv/")
loginFacebookByCookie(cookie)

sleep(10)

driver.get("https://cos.tv/videos/play/28115035769050112")
sleep(10)
# click_video = driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div[2]/div/div[2]/ul/li[1]/div/div[1]/a/img')
# click_video.click()
# sleep(10)
# click vào ô nhận thưởng để bỏ qua
click = driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div[1]/div[1]/div[2]/div[1]/div[1]/div/div[1]/div/div[2]')
click.click()
sleep(10)

driver.switch_to.new_window('window')

# sleep(10)
# # ====================================================================================================
# # click vào ô nhận thưởng để bỏ qua
# click = driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div[1]/div[1]/div[2]/div[1]/div[1]/div/div[1]/div/div[2]/div[1]/div[1]/div/div[2]/div[3]')
# click.click()
# sleep(10)
# # ====================================================================================================
# # like video
# like = driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div[1]/div[1]/div[2]/div[1]/div[2]/div/div[2]/div/div[1]/div/div[3]/span[1]/div')
# like.click()
# sleep(3)
# # ====================================================================================================
# # comment video
# comment = driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div[1]/div[5]/div/div[2]/div[1]/div[2]/div/div/form/div[1]/textarea')
# comment.send_keys("hello :))")
# # nhấn vào nút send commet
# send_comment = driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div[1]/div[5]/div/div[2]/div[1]/div[2]/div/div/form/div[2]/div/div[3]/button[2]')
# send_comment.click()