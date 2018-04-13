.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except inS compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

===================
|S3| Pre-Signed URL
===================

.. meta::
   :description: Create direct browser access to private Amazon S3 data using the AWS SDK for PHP.
   :keywords: Amazon S3 code examples for PHP

You can authenticate certain types of requests by passing the required
information as query-string parameters instead of using the Authorization HTTP
header. This is useful for enabling direct third-party browser access to your
private |S3| data, without proxying the request.


The following examples show how to:

* Get a "pre-signed" request and encode it as a URL using :aws-php-class:`CreatePresignedRequest <class-Aws.S3.S3Client.html#_createPresignedRequest>`.
* Encode a URL for an |S3| object from a "pre-signed" request so an end-user's browser can retrieve it.
* Limit access to a URL by specifying an expiration time when you use :aws-php-class:`CreatePresignedRequest <class-Aws.S3.S3Client.html#_createPresignedRequest>`.
* Retrieve the public URL for an |S3| object using :aws-php-class:`GetObjectUrl <class-Aws.S3.S3Client.html#_getObjectUrl>`.

All the example code for the |sdk-php| is available `here on GitHub <https://github.com/awsdocs/aws-doc-sdk-examples/tree/master/php/example_code>`_.

Credentials
-----------

Before running the example code, configure your AWS credentials. See :doc:`guide_credentials` and import the |sdk-php|.

Creating a Pre-Signed Request
-----------------------------

You can create pre-signed URLs for any |S3| operation using the
``getCommand`` method for creating a command object, and then calling the
``createPresignedRequest()`` method with the command. When you ultimately send
the request, be sure to use the same method and headers as the
returned request.

**Sample Code**

.. literalinclude:: example_code/s3/PresignedURL.php
   :lines: 25-36
   :language: php

Creating a Pre-Signed URL
-------------------------


The most common scenario to enable third-party browser access to your private |S3| object is to create a pre-signed URL to
GET an object. You can retrieve the pre-signed URL of the object using the ``getUri()`` method of the request.

**Sample Code**

.. literalinclude:: example_code/s3/PresignedURL.php
   :lines: 39-47
   :language: php

Getting the URL to an Object
----------------------------

If you only need the public URL to an object stored in an |S3| bucket,
you can use the ``Aws\S3\S3Client::getObjectUrl()`` method. This method
returns an unsigned URL to the given bucket and key.

**Sample Code**

.. literalinclude:: example_code/s3/PresignedURL.php
   :lines: 49-50
   :language: php

.. important::

    The URL returned by this method isn't validated to ensure that the bucket
    or key exists. Also this method doesn't ensure that the object allows
    unauthenticated access.
