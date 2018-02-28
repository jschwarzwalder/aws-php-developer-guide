.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

============
Installation
============

There are 3 supported methods of installing the |sdk-php|. The
recommended way to install the SDK is through `Composer <http://getcomposer.org>`_.

Installing via Composer
-----------------------

Using `Composer <http://getcomposer.org>`_ is the recommended way to install
the |sdk-php|. Composer is a dependency management tool for PHP that
allows you to declare the dependencies your project needs and installs them
into your project.

1. Install Composer

   ::

       curl -sS https://getcomposer.org/installer | php

2. Run the Composer command to install the latest stable version of the SDK:

   ::

       php composer.phar require aws/aws-sdk-php

3. Require Composer's autoloader:

   .. code-block:: php

       <?php
       require 'vendor/autoload.php';

You can find out more on how to install Composer, configure autoloading, and
other best-practices for defining dependencies at
`getcomposer.org <http://getcomposer.org>`_.

Installing via Phar
-------------------

You can `download the packaged phar <http://docs.aws.amazon.com/aws-sdk-php/v3/download/aws.phar>`_
and simply include it in your scripts to get started:

.. code-block:: php

    <?php
    require '/path/to/aws.phar';

Each release of the |sdk-php| ships with a pre-packaged
`phar <http://php.net/manual/en/book.phar.php>`_ (PHP archive) file containing
all of the classes and dependencies you need to run the SDK. Additionally, the
phar file automatically registers a class autoloader for the |sdk-php|
and all of its dependencies when included.

.. note::

    If you are using PHP with the Suhosin patch (not recommended, but common on
    Ubuntu and Debian distributions), you may need to enable the use of phars in
    the ``suhosin.ini``. Without this, including a phar file in your code will
    cause it to silently fail. You should modify the ``suhosin.ini`` file by
    adding the line:

    ``suhosin.executor.include.whitelist = phar``

Installing via Zip
------------------

Each release of the |sdk-php| ships with a zip file containing all of the
classes and dependencies you need to run the SDK. Additionally, the zip file
includes a class autoloader for the |sdk-php| and all of its dependencies.

To get started, you must `download the zip file <http://docs.aws.amazon.com/aws-sdk-php/v3/download/aws.zip>`_,
unzip it into your project to a location of your choosing, and include the
autoloader::

    require '/path/to/aws-autoloader.php';
