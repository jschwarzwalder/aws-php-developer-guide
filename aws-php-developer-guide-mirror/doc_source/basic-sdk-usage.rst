.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

##########################
Basic SDK Usage |sdk-PHP|
##########################

This guide focuses on basic usage patterns of the **|sdk-PHP|** in your project. This guide assumes
that you have already `downloaded and installed the SDK <setup-install>`_ and retrieved
your `AWS access keys <http://aws.amazon.com/developers/access-keys/>`_.

Including the SDK
==================

No matter which technique you have used to to install the SDK, you can include the SDK into
your code with just a single ``require`` statement. Please refer to the following table for the
PHP code that best fits your installation technique. Please replace any instances of
``/path/to/`` with the actual path on your system.

======================= =======================================
Installation Technique  Require Statement
======================= =======================================
Using Composer          ``require '/path/to/vendor/autoload.php';``
Using the Phar          ``require '/path/to/aws.phar';``
Using the Zip           ``require '/path/to/aws-autoloader.php';``
======================= =======================================

For the remainder of this guide, we will show examples that assume the Composer installation method.
If you are using a different installation method, then you can refer back to this section to
substitute in the proper require code.

.. _include-sdk:

Usage Summary
==============

The basic usage pattern of the SDK is that you instantiate a **Client** object for the AWS service
you want to interact with. Client objects have methods that correspond one-to-one with operations in
the service's API. To execute a particular operation, you call its corresponding method, which
either returns an array-like **Result** object on success, or throws an **Exception** on failure.

Downloading and extracting the SDK
==================================

Creating a Client
=================
You can create a client by passing an associative array of options to a client's constructor.

::
    <?php

    // Include the SDK using the Composer autoloader
    require 'vendor/autoload.php';

    $s3 = new Aws\S3\S3Client([
        'version' => 'latest',
        'region'  => 'us-east-1'
    ]);


Notice that we did **not** explicitly provide credentials to the client. That's because the
credentials should be detected by the SDK from either `environment variables <credentials>`_ (via
AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY), an `AWS credentials INI file <credential>`_ in your
HOME directory, AWS Identity and Access Management (IAM) instance `profile credentials
<credentials>`_, or `credential providers <credentials>`_.

All of the general client configuration options are described in detail in the `configuration guide
<configuration>`_. The array of options provided to a client may vary based on which client you are
creating. These custom client configuration options are described in the `API documentation
<http://docs.aws.amazon.com/aws-sdk-php/latest/>`_ of each client.

Using the Sdk class
===================
