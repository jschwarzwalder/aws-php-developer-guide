.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

==========================================
Using Elastic IP Addresses with |EC2|
==========================================

.. meta::
   :description: Describe |EC2| instances and acquire, associate, and release Elastic IP addresses.
   :keywords: |EC2|, |sdk-php| examples

An Elastic IP address is a static IP address designed for dynamic cloud computing. An Elastic IP address is associated with your AWS account. It is a public IP address, which is reachable from the Internet. If your instance does not have a public IP address, you can associate an Elastic IP address with your instance to enable communication with the Internet.

The examples below show how to:

* Describes one or more of your instances using `DescribeInstances <http://docs.aws.amazon.com/aws-sdk-php/v3/api/api-ec2-2016-11-15.html#describeinstances>`_.
* Acquires an Elastic IP address using `AllocateAddress <http://docs.aws.amazon.com/aws-sdk-php/v3/api/api-ec2-2016-11-15.html#allocateaddress>`_.
* Associate an Elastic IP address with an instance using `AssociateAddress <http://docs.aws.amazon.com/aws-sdk-php/v3/api/api-ec2-2016-11-15.html#associateaddress>`_.
* Release an Elastic IP address using `ReleaseAddress <http://docs.aws.amazon.com/aws-sdk-php/v3/api/api-ec2-2016-11-15.html#releaseaddress>`_.

All the example code for the |sdk-php| is available `here on GitHub <https://github.com/awsdocs/aws-doc-sdk-examples/tree/master/php/example_code>`_.

Credentials
-----------

Before running the example code, configure your AWS credentials, as described in :doc:`guide_credentials`.

Describe an Instance
--------------------

**Imports**

.. literalinclude::  example_code/ec2/DescribeInstances.php
   :lines: 15-17
   :language: PHP

**Code**

.. literalinclude:: example_code/ec2/DescribeInstances.php
   :lines: 26-34
   :language: php


Allocate and Associate an Address
---------------------------------

**Imports**

.. literalinclude::  example_code/ec2/AllocateAddresses.php
   :lines: 15-17
   :language: PHP

**Code**

.. literalinclude:: example_code/ec2/AllocateAddresses.php
   :lines: 26-45
   :language: php


Release an Address
------------------

**Imports**

.. literalinclude::  example_code/ec2/ReleaseAddress.php
   :lines: 15-17
   :language: PHP

**Code**

.. literalinclude:: example_code/ec2/ReleaseAddress.php
   :lines: 26-44
   :language: php

