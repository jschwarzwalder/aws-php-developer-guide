.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

====================================
Creating and Using |S3| Buckets
====================================

.. meta::
   :description:
   :keywords: |S3|, |sdk-php| examples

The examples below show how to:

* Return a list of buckets owned by the authenticated sender of the request using :aws-php-class:`ListBuckets </api-s3-2006-03-01.html#listbuckets>`_.
* Create a new bucket using :aws-php-class:`CreateBucket </api-s3-2006-03-01.html#createbucket>`_.
* Add an object to a bucket using :aws-php-class:`PutObject </api-s3-2006-03-01.html#putobject>`_.

All the example code for the |sdk-php| is available `here on GitHub <https://github.com/awsdocs/aws-doc-sdk-examples/tree/master/php/example_code>`_.

Credentials
-----------

Before running the example code, configure your AWS credentials, as described in :doc:`guide_credentials`.

List Buckets
------------

**Imports**

.. literalinclude::  example_code/s3/ListBuckets.php
   :lines: 16-19
   :language: PHP

**Code**

.. literalinclude:: example_code/s3/ListBuckets.php
   :lines: 28-38
   :language: php


Create a Bucket
---------------

**Imports**

.. literalinclude::  example_code/s3/CreateBucket.php
   :lines: 16-19
   :language: PHP

**Code**

.. literalinclude:: example_code/s3/CreateBucket.php
   :lines: 28-45
   :language: php

Put an Object in a Bucket
-------------------------
**Imports**

.. literalinclude::  example_code/s3/ListBuckets.php
   :lines: 16-19
   :language: PHP

**Code**

.. literalinclude:: example_code/s3/ListBuckets.php
   :lines: 28-56
   :language: php
