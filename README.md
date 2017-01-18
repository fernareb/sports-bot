# Seattle Sports Bot

Our office is located in the oldest neighborhood in Seattle, Pioneer Square, which is great for gorgeous rooftop views, happy hours, food trucks, and gamedays -- unless you're not actually attending the game. If you're not attending the game, our close proximity to the stadiums means you might get stuck in the Gameday Gridlock if you don't plan carefully.

After dreaming about a slackbot that could let me know if it was a gameday in Seattle while I was getting ready in the morning, and failing to find a great source to build it from, I found [gametonight.in](gametonight.in) and decided to do it myself. #learnandgrowcourageously

The slackbot is, of course, an ode to Gary Payton and works by sending one of two messages to a Slack Channel every morning at 7am based on the JSON endpoint.

## Get Your Own Bot
You can setup your own version of the `Seattle Sports Bot` in a few easy steps. I recommend making a channel on slack for testing and another for the final product.

### Project Setup
1. Clone [the repository](https://github.com/rsamuelson/seattle-sports-bot.git)
2. Get your [Incoming Web Hook URL](https://api.slack.com/incoming-webhooks) from Slack.
3. Copy [bot_settings_pub.py](/bot_settings_pub.py) and rename is `bot_settings.py`
4. Insert the following configuration information for your bot, including the Slack Incoming Webhook URL and Message
5. Open terminal and commit your changes.
7. To test your app, run the `sports-bot.py` script and you should receive a message from Gary Payton in your Slack test channel.

### Deploy bot on Heroku
Okay so you've got it working, but now you need to schedule it so it lets you know when you wake up in the morning.

1. Open [Procfile](/Procfile) and add `worker: python sports-bot.py` and hit save.
3. Create a Heroku Account, if you don't already have one
4. Verify your Heroku account with a CC
5. Download and install [Heroku Toolbelt](https://devcenter.heroku.com/articles/quickstart#step-2-install-the-heroku-toolbelt)
6. Authenticate Heroku via command line - [instructions from Heroku](https://devcenter.heroku.com/articles/authentication)
7. In terminal, `heroku create` to generate your app, which will allow us to schedule your bot to give you a daily update in slack
8. In terminal, `git commit -am "<update procfile for testing>"`
9. Type `git push heroku master` to push your script to your Heroku app
10. Test your Heroku app by typing `heroku run worker` - if it worked, you should receive another message in your test slack channel

#### Schedule Your Bot
To schedule your bot, login to Heroku's dashboard and add the `Scheduler` add-on.

[false]:/img/false_text.png
[true]:/img/true_text.png
