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

* Return a list of buckets owned by the authenticated sender of the request using :sdk-php-api-v3:`ListBuckets <api-s3-2006-03-01.html#listbuckets>`.
* Create a new bucket using :sdk-php-api-v3:`CreateBucket <api-s3-2006-03-01.html#createbucket>`.
* Add an object to a bucket using :sdk-php-api-v3:`PutObject <api-s3-2006-03-01.html#putobject>`.

All the example code for the |sdk-php| is available `here on GitHub <https://github.com/awsdocs/aws-doc-sdk-examples/tree/master/php/example_code>`_.

Credentials
-----------

Before running the example code, configure your AWS credentials, as described in :doc:`guide_credentials`.

List Buckets
------------

Create a php file with following code. First create an AWS.S3 client service specifying the region and version, then call the listBuckets method which will return all |s3| buckets owned by the sender of the request as an array of Bucket structures.   

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

Create a php file with following code. First create an AWS.S3 client service specifying the region and version, then call the createBucket method with an array as the parameter. The only required field is the key 'Bucket' with a string value for bucket name you want to create, but you can specify the region with the 'CreateBucketConfiguration' field.  If successful this method will return the 'Location' of the bucket.  

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

.. literalinclude::  example_code/s3//PutObject.php
   :lines: 16-19
   :language: PHP

**Code**

.. literalinclude:: example_code/s3//PutObject.php
   :lines: 28-56
   :language: php
