from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
from random import randint
#import pandas as pd

chromedriver_path = r'C:\Users\Ani\Desktop\insa\chromedriver.exe'  # Change this to your own chromedriver path!
webdriver = webdriver.Chrome(executable_path=chromedriver_path)
sleep(2)
webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
sleep(3)

username = webdriver.find_element_by_name('username')
username.send_keys('<your username>')
password = webdriver.find_element_by_name('password')
password.send_keys('<youar passwd>')

button_login = webdriver.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[4]/button") ##react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(3) > button
button_login.click()
sleep(10)
#.NoSuchElementException -- erroe when it cant find an elemnet
notnow = webdriver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button')
notnow.click() #comment these last 2 lines out, if you don't get a pop up asking about notifications

hashtag_list = ['console','ps5','rog','tech']

prev_user_list = [] #- if it's the first time you run it, use this line and comment the two below
# prev_user_list = pd.read_csv('20181203-224633_users_followed_list.csv', delimiter=',').iloc[:,1:2] # useful to build a user log
# prev_user_list = list(prev_user_list['0'])

new_followed = []
tag = 0
followed = 0
likes = 0
comments = 0

for hashtag in hashtag_list:
    webdriver.get('https://www.instagram.com/explore/tags/'+ hashtag_list[tag] + '/')
    tag += 1
    sleep(5)
 # try:
   #     re_tag = webdriver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/span[2]').text
    #    print(re_tag)
  #except:
    #select the first post of the given hashtag
    first_thumbnail = webdriver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div')

    first_thumbnail.click()
    sleep(2)
    try:
        for x in range(1,10):
            username = webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[1]/a').text # it will assign the username to username variable 
            if username not in prev_user_list: # If we already follow, do not click the unfollow buttom
                
                if webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').text == 'Follow':

                    webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').click()

                    new_followed.append(username)
                    followed += 1

                    # Liking the picture
                    button_like = webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button').click()

                  #  button_like.click()
                    likes += 1
                    sleep(10)

                    # Comments and tracker
                    comm_prob = randint(1,5)
                  #  print(f'{hashtag}_{x}: {comm_prob}')
                    #if comm_prob > 7:
                    comments += 1
                    webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[2]/button').click()
                    comment_box = webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/textarea')

                    if (comm_prob < 4):
                            comment_box.send_keys('Really cool! Please Check Out my Page too')
                            sleep(1)
                    elif (comm_prob > 3):
                            comment_box.send_keys('Nice work :)')
                            sleep(1)
                    elif comm_prob == 2:
                            comment_box.send_keys('Awesome!!')
                            sleep(1)
                    elif comm_prob == 1:
                            comment_box.send_keys('So cool! :)')
                            sleep(1)
                        # Enter to post comment
                    webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/button').click()
                        #comment_box.send_keys(Keys.ENTER)
                    sleep(15)

                    #Next picture
                    #webdriver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a').click()
                    webdriver.find_element_by_link_text('Next').click()

                    sleep(17)
            else:
                    #webdriver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a[2]').click()
                    webdriver.find_element_by_link_text('Next').click()
                    sleep(20)
    # some hashtag stops refreshing photos (it may happen sometimes), it continues to the next hashtags
    except:
        continue

for n in range(0,len(new_followed)):
    prev_user_list.append(new_followed[n])

#updated_user_df = pd.DataFrame(prev_user_list)
#updated_user_df.to_csv('{}_users_followed_list.csv'.format(strftime("%Y%m%d-%H%M%S")))
print(f'Liked {likes} photos.')
print(f'Commented {comments} photos.')
print(f'Followed {followed} new people.')
