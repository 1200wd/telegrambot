Telegram Bot - Server and website monitoring
============================================

Monitoring scripts to check websites and services, look for file changes, check backups and detect IP address changes.

Sends Telegram messages with a bot and the telegram API.

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

Or to check website, but only send a message after a 2 number of failures. You can change the number of failures
before messaging in the python code.

.. code-block:: bash

    $ python check_website_failures.py '<url>' '<expected_word>'


Monitor File Changes
--------------------

Check for recent changes files in directory. For instance to verify if backups are working.

.. code-block:: bash

    $ python check_latestfile.py '<directory>' <alarm_after_x_minutes>


Monitor Server
--------------

Check if server is reachable with a ping command.

.. code-block:: bash

    $ python check_ping.py '<hostname or ip>'

Check current server WAN ip address. Used for home connections where ip addresses tend to change.

.. code-block:: bash

    $ python check_ip.py


Monitor Services
----------------

Check if a specific service is running on a server. Works for Ubuntu and probably other unix operating systems.

.. code-block:: bash

    $ python check_service.py '<service_name>'

Or to check for a service and only send a message after the second failure, to avoid false warnings.

.. code-block:: bash

    $ python check_service_failures.py '<service_name>'


Monitor Bitcoin Node
--------------------

Check if a Bitcoin core node is running and returns the number of blocks synced. Uses the Bitcoinlib library.

.. code-block:: bash

    $ python check_bitcoind.py '<bitcoind_url>' '[<block_count>]'



