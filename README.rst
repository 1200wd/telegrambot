Telegram Bot - Monitor service
==============================

Monitoring scripts to check for various events:
* Check new bitcoin transactions for a wallet or address
* Check website status
* Monitor file changes
* Check IP address changes
* Monitor if specific services are running on an instance, such as a Bitcoin node

Sends Telegram messages with a bot and the Telegram API.


Get started
-----------

* Create a bot with Botfather with the command /newbot
* Copy the API key and place it in .token in the main telegrambot directory
* Send a message to the chat or put the Chat ID in the .chatid file in the main telegrambot directory


Send messages
-------------

If everything has been setup correctly you can send messages to Telegram
.. code-block:: bash

    $ python sendmessage.py 'Hello world!'


Monitor Bitcoin Wallet
----------------------

Check a Bitcoin wallet for changes, so new outgoing or incoming transactions.

.. code-block:: bash

    $ python check_bitcoin_wallet.py '<public_masterkey>' '[<network>]' '[<wallet_name>]'


Monitor Bitcoin Address
-----------------------

Check a specific bitcoin address for new transactions.

.. code-block:: bash

    $ python check_bitcoin_address.py '<address>' '[<network>]' '[<address_name>]'


Monitor Website
---------------

Check if specific word is found on website, to check if website is running correctly.

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



