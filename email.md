<!-- Hi guys. It's Mo, reaching out to you from the beyond.

I've set up the email process as much as I can. 

So far I've:

1) Added a route to send a confirmation email

2) Added a helper method before the app routes that can be used to resend confirmation emails if they haven't been received

3) On the front-end side I tried to edit the CSS of the main page so we have a consistent design pattern across the webpages. If you find these CSS edits to be unhelpful, please cancel them out during the merge! I'm aware that we're seeing 
different web page results so I could be editing things that don't exist/need to be edited for you guys.

4) I didn't get a chance to create the About template but I figured it could be done with some cute fuffle about what we offer as a service etc, using the same layout from index.

I've got the following blockers:
1) For some reason the jinja tags on the confirmation template aren't displaying the user's email on the webpage
2) The link isn't correctly accessing the GET request to send a confirmation email


To test if an email has been a received, I used Mailhog

This can be installed using the following commands:

brew update
brew install mailhog

Run using:

mailhog

If you find it easier you can use Docker. I've added the dockerfile to the module list.

This should show an email being recieved.


To test what happens if the confirmation link is clicked on, I was going to use Selenium (it can be installed using pip install Selenium then run alongside pytest).

However I haven't had time to wrap this up.

From this point we could continue with this process or do something simple like 

1) Create a gmail and replace ben@gmail.com in the app route with it to literally display the email being sent
2) Literally copy the url that would be in the confirmation email and paste it into an empty page to show it redirects to the expected webpage.

Sorry I couldn't finish it in time!

 -->