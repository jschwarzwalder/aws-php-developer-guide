.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

=====================
|S3| Pre-Signed POSTs
=====================

.. meta::
   :description: Create write access to private Amazon S3 data using the AWS SDK for PHP.
   :keywords: Amazon S3 code examples for PHP

Much like pre-signed URLs, pre-signed POSTs enable you to give write access to a
user without giving them AWS credentials.

The following examples show how to:

* Create a presigned POST form that is an instance of :aws-php-class:`Aws\S3\PostObjectV4 </class-Aws.S3.PostObjectV4.html>`.


All the example code for the |sdk-php| is available `here on GitHub <https://github.com/awsdocs/aws-doc-sdk-examples/tree/master/php/example_code>`_.

Credentials
-----------

Before running the example code, configure your AWS credentials. See :doc:`guide_credentials` and import the |sdk-php|.

**Sample Code**

.. literalinclude:: example_code/s3/PresignedPost.php
   :lines: 25-58
   :language: php
