Telegram Bot - Send messages
============================

Send Telegram messages and with a bot and the telegram API.

Includes some Monitoring scripts to check websites and services, look for file changes, check backups, etcetera.

Get started
-----------

* Create a bot with Botfather with the command /newbot
* Copy the API key and place it in .token in the main telegrambot directory
* Send a message to the chat or put the Chat ID in the .chatid file in the main telegrambot directory

Send messages
-------------

.. code-block:: bash

    $ python sendmessage.py 'Hello world!'


Monitor Website
---------------

Check if specifc word is found on website.

.. code-block:: bash

    $ python check_website.py '<url>' '<expected_word>'


Monitor File Changes
--------------------

Check for recent changes files in directory. For instance to verify if backups are working.

.. code-block:: bash

    $ python check_latestfile,py '<directory>' <alarm_after_x_minutes>

