.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

=============================
Configuring |S3| Buckets
=============================

.. meta::
   :description: Get or set CORS configuration for an |S3| bucket.
   :keywords: |S3|, |sdk-php| examples

Cross-origin resource sharing (CORS) defines a way for client web applications that are loaded in one domain to interact with resources in a different domain. With CORS support in |S3|, you can build rich client-side web applications with |S3| and selectively allow cross-origin access to your |S3| resources.

For more information about using CORS configuration with an |S3| bucket, see `Cross-Origin Resource Sharing (CORS) <http://docs.aws.amazon.com/AmazonS3/latest/dev/cors.html>`_.

The examples below show how to:

* Get the CORS configuration for a bucket using :aws-php-class:`GetBucketCors <api-s3-2006-03-01.html#getbucketcors>`.
* Set the CORS configuration for a bucket using :aws-php-class:`PutBucketCors <api-s3-2006-03-01.html#putbucketcors>`.

All the example code for the |sdk-php| is available `here on GitHub <https://github.com/awsdocs/aws-doc-sdk-examples/tree/master/php/example_code>`_.

Credentials
-----------

Before running the example code, configure your AWS credentials, as described in :doc:`guide_credentials`.

Get the CORS Configuration
--------------------------


**Imports**

.. literalinclude::  example_code/s3/GetBucketCors.php
   :lines: 16-19
   :language: PHP

**Code**

.. literalinclude:: example_code/s3/GetBucketCors.php
   :lines: 27-42
   :language: php

Set the CORS Configuration
--------------------------

**Imports**

.. literalinclude::  example_code/s3/PutBucketCors.php
   :lines: 16-19
   :language: PHP

**Code**

.. literalinclude:: example_code/s3/PutBucketCors.php
   :lines: 27-53
   :language: php
