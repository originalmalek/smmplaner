# Send one posts to VK.com, Facebook, Telegram automatically 
The project makes posts to VK.com, Facebook, Telegram automatically


## Description
The code: 
The project makes posts in VK.com, Facebook, Telegram automatically publics automatically using API.  

The project uses: [VK API](https://vk.com/dev), [Facebook API](https://developers.facebook.com/), [Telegram API](https://core.telegram.org/api).  
  

## Requirements
Python >=3.7  
Register application on [VK](https://vk.com/dev) with implicit method ang get API key. 
Register application on [Facebook](https://developers.facebook.com/) 'For everything else' and get api key in [Graph explorer](https://developers.facebook.com/tools/explorer/).
Register bot in [Telegram](http://t.me/BotFather) and get key from it.
 
Create public on vk.com 
Create public on facebook
Creaet group in telegram. Add your bot as an admin.

  
Create file '.env' and add the code:
```
TELEGRAM_TOKEN=your_telegram_token
TELEGRAM_GROUP_NAME=your_telegram_group
VK_ACCESS_TOKEN=your_vk_token
VK_GROUP_ID=your_vk_group_id
FACEBOOK_ACCESS_TOKEN=your_fb_token
FACEBOOK_GROUP_ID=your_facebook_group_id
```

Install requirements modules:
```
pip install -r requirements.txt	
```


### How to use

Install requirements.  
Open and run 'main.py'.
```
python main.py image_name post_text
```

* How to get Access token [vk.com](https://vk.com/apps?act=manage):
  * Use [Implicit Flow](https://vk.com/dev/implicit_flow_user) procedure
  * Delete **redirect_url** parameter from url
  * In scope parameters enter scope=photos,groups

* How to create [vk.com](https://vk.com/apps?act=manage) app:
  * Go to page [vk.com/apps](https://vk.com/apps?act=manage)
  * Click on 'Creat App' button
  * Fill fields
  * Change platform 'Standalone'

* Where to get group id:
  * Go to page [vk.com/groups](https://vk.com/groups)
  * Click on 'Creat community' button
  * Fill fields
  * You'll see link 'https://vk.com/publicXXXXXXXXX' where XXXXXXXXX is your group id


## Project goal

The code was written for educational purpose on online course for Api developers [Devman](http://dvmn.org). 
