.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

===============================
Installing the AWS SDK for PHP
===============================

You can use any of the following methods to install the  |sdk-php|.

* Using Composer
* Using the Phar
* Using the Zip File

Installing with Composer
-----------------------

`Composer <http://getcomposer.org>`_ is the recommended way to install
the |sdk-php|. Composer is a tool for PHP that manages and installs the dependencies of your project.

1. Type the following at the command line to install Composer.

   ::

       curl -sS https://getcomposer.org/installer | php

2. Type the Composer command to install the latest stable version of the SDK.

   ::

       php composer.phar require aws/aws-sdk-php

3. Require the Composer autoloader in your scripts.

   .. code-block:: php

       <?php
       require 'vendor/autoload.php';
       ?>

For more information on how to install Composer, configure autoloading, and follow other best
practices for defining dependencies, see `getcomposer.org <http://getcomposer.org>`_.

Installing with the Packaged Phar
---------------------------------

Each release of the |sdk-php| includes a pre-packaged phar (PHP archive) containing all the classes
and dependencies you need to run the SDK. Additionally, the phar automatically registers a class
autoloader for the SDK for PHP and all its dependencies.

You can `download the packaged phar <|sdk-PHP-phar|>`_
and include it in your scripts.

.. code-block:: php

    <?php
    require '/path/to/aws.phar';



.. note::

    Using PHP with the Suhosin patch is not recommended, but common on Ubuntu and Debian distributions.
    In this case, you may need to enable the use of phars in the suhosin.ini. Without doing this,
    including a phar file in your code will cause a silent failure. To modify suhosin.ini, add the
    following line.

    ::

    ``suhosin.executor.include.whitelist = phar``

Installing via Zip
------------------

The |sdk-php| ncludes a zip file containing all the classes and dependencies you need to run the SDK.
Additionally, the zip file includes a class autoloader for the SDK for PHP and its dependencies.

To install the SDK,  `download the zip file <|sdk-PHP-dl|>`_,
hen unzip it into your project at a location of your choice. Then include the autoloader as follows in your scripts.

::

    require '/path/to/aws-autoloader.php';
