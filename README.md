# harvester_support

Helper files  / tips for social media harvesting

You'll need python, obvs, and abilty the install on the device, especially via pip. 

## instagram 

You need an instagram account and password for these. 

### getting live streams

````pip3 install pyinstalive````

https://github.com/dvingerh/PyInstaLive

You have a 24 hour window to grab any livestream archive via the insta username: 

````pyinstalive -d "interesting_insta_account"````

You can alo use a text file of accounts to d a batch, one account per line

````pyinstalive -b "my_text_file.txt"````

### getting posts


````pip3 install instagram-scraper````

https://github.com/rarcega/instagram-scraper

````instagram-scraper intersting_insta_account -u  my_insta_account -p my_insta_password````

This gets everything. We need to find a way of filtering by date/time. Thats on me. I'll whip up a helper if its needed. 

## Vimeo

Use youtube-dl 

https://ytdl-org.github.io/youtube-dl/index.html

## Facebook

### facebook live video

````pip3 install fb-down````

https://pypi.org/project/fb-down/ 

URL for the video. 

````fbdown https://www.facebook.com/some_fb_account/videos/____________/````

## Tiktok

See helper file in tiktok folder



