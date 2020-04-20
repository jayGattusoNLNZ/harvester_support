# Getting ready

You need an instagram account and password for these.

For some accounts/content you migh need the instagram account to let you follow them. Try and use a easily identifiable account name. 

We can't really share accounts, because instagram looks for multiple access/logons as bot action, and blocks. 

# getting live streams

You need python (v3.x) for this to work.

From commandline...

Navigate to/make a sensible folder on your machine. 

````c:\projects\harvests\instagram_live````

Then install the tool:

````pip3 install pyinstalive````

Go into the pyinstalive folder, open the file ````pyinstalive.ini```` in notepad and set the following bits of information:

username = instagram username

password = instagram password

download_path = full path to where you want the downloads to go

There are other options, like setting the proxy if you need it etc. 

Notes and code can be found here:

https://github.com/dvingerh/PyInstaLive

You have a 24 hour window to grab any livestream archive via the insta username

from commandline:  

````pyinstalive -d "interesting_insta_account"````

You can also use a text file of accounts to download a batch, one account per line. 

E.g.

Create ````my_text_file.txt````. 

Add your accounts of interest:

* interesting_insta_account
* exciting_insta_account
* another_insta_account

Save file and from commandline run this:


````pyinstalive -b "my_text_file.txt"````

This will start a process that watches the accounts and gets any video/live streams. It happens silently - you get no notifications. 
It stops when you close the commandline window. 

## getting posts

You need python (v3.x) for this to work 

From commandline...

Navigate to/make a sensible folder on your machine. 

````c:\projects\harvests\instagram_scraper````

Then install the tool:

````pip3 install instagram-scraper````

Notes and code here 

https://github.com/rarcega/instagram-scraper

To work it, you need to be at commandline, naviate to where you want your harvests to be saved, and then run the tool

from the notes: 

Providing username and password is optional, if not supplied the scraper runs as a guest. Note: In this case all private user's media will be unavailable. All user's stories and high resolution profile pictures will also be unavailable.

instagram-scraper intersting_insta_account -u my_insta_account -p my_insta_password

This gets everything. We need to find a way of filtering by date/time. Thats on me. I'll whip up a helper if its needed
