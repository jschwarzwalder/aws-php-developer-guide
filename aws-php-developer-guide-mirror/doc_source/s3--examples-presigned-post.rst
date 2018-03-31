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
   :description: Create write access to private |S3| data using the |sdk-php|.
   :keywords: |S3|, |sdk-php| examples, |S3| for PHP code examples

Much like pre-signed URLs, pre-signed POSTs enable you to give write access to a
user without giving them AWS credentials. Pre-signed POST forms can be created
with the help of an instance of :aws-php-class:`Aws\S3\PostObjectV4 </class-Aws.S3.PostObjectV4.html>`.

To create an instance of ``PostObjectV4``, you must provide the following: 

- instance of ``Aws\S3\S3Client``
- bucket
- associative array of form input fields
- array of policy conditions (see :s3-dg:`Policy Construction <HTTPPOSTForms>` in the |S3-dg|)
- expiration time string for the policy (optional, one hour by default).

**Sample Code**

.. literalinclude:: example_code/s3/PresignedPost.php
   :lines: 25-58
   :language: php