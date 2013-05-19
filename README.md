text-ddg
========

A Flask app for querying DuckDuckGo via text messages (SMS).

Getting the server running with virtualenv and gunicorn looks something like this:

```sh
$ git clone git://github.com/rpicard/text-ddg.git
$ cd text-ddg
$ virtualenv env
$ . env/bin/activate
$ pip install -r requirements.txt
$ gunicorn app:app -p text-ddg.pid -D
```

To get going, you'll need to set up a TwiML app on Twilio. Leave the voice URL blank and set the SMS request URL to the server where the app will be running. When someone sends a text to the associated phone number, Twilio will send a GET request to your application and respond to the sender with the SMS specified by this application.

You can text my server at `813-419-1902` for an example.

#### License

Copyright (c) Robert Picard

All rights reserved.

Licensed under the [MIT license](http://opensource.org/licenses/MIT).