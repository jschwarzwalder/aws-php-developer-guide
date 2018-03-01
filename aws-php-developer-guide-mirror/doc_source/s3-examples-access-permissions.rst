.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

============================================
Managing |S3| Bucket Access Permissions
============================================

.. meta::
   :description: Get ACLs and set permissions for |S3| buckets.
   :keywords: |S3|, |sdk-php| examples

Access control lists (ACLs) are one of the resource-based access policy options you can use to manage access to your buckets and objects. You can use ACLs to grant basic read/write permissions to other AWS accounts. To learn more, see `Managing Access with ACLs <http://docs.aws.amazon.com/AmazonS3/latest/dev/S3_ACLs_UsingACLs.html>`_.

The example below shows how to:

* Get the access control policy for a bucket using `GetBucketAcl <http://docs.aws.amazon.com/aws-sdk-php/v3/api/api-s3-2006-03-01.html#getbucketacl>`_.
* Set the permissions on a bucket using access control lists, using `PutBucketAcl <http://docs.aws.amazon.com/aws-sdk-php/v3/api/api-s3-2006-03-01.html#putbucketacl>`_.

All the example code for the |sdk-php| is available `here on GitHub <https://github.com/awsdocs/aws-doc-sdk-examples/tree/master/php/example_code>`_.

Credentials
-----------

Before running the example code, configure your AWS credentials, as described in :doc:`guide_credentials`.

Get and Set an Access Control List Policy
-----------------------------------------

**Imports**

.. literalinclude::  example_code/s3/s3BucketAcl.php
   :lines: 16-19
   :language: PHP

**Code**

.. literalinclude:: example_code/s3/s3BucketAcl.php
   :lines: 21-74
   :language: php
