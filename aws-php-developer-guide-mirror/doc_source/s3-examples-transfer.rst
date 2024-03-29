.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

================================================
Upload a whole directory to |S3| using |sdk-php|
================================================

.. meta::
   :description: Upload, copy, or download files and directories to an Amazon S3 bucket using the AWS SDK for PHP.
   :keywords: Amazon S3 code examples for PHP


The |sdk-php| |S3| transfer manager is used to upload entire directories to
an |S3| bucket and download entire buckets to a local directory.

The examples below show how to:

* Upload directories and download buckets using :aws-php-class:`Transfer <class-Aws.S3.Transfer.html>`.
* Transfer asynchronously with :aws-php-class:`Promises <class-Aws.S3.Transfer.html#_promise>`.

All the example code for the |sdk-php| is available `here on GitHub <https://github.com/awsdocs/aws-doc-sdk-examples/tree/master/php/example_code>`_.

Credentials
-----------

Before running the example code, configure your AWS credentials, as described in :doc:`guide_credentials`.

Upload a Local Directory to |S3|
--------------------------------

The ``Aws\S3\Transfer`` object is used to perform transfers. The following
example shows how to recursively upload a local directory of files to an
|S3| bucket.


**Sample Code**

.. literalinclude:: example_code/s3/TransferManager.php
   :lines: 25-29
   :language: php

.. literalinclude:: example_code/s3/TransferManager.php
   :lines: 34-44
   :language: php



In this example, we created an |S3| client, created a ``Transfer`` object,
and performed a transfer synchronously. The example demonstrates how to use a 
minimal amount of code to perform a transfer. The transfer object
can also perform transfers of files asynchronously and has various configuration options you can
use to customize the transfers.

You can upload the local files to a "subfolder" of a an |S3| bucket by
providing a key prefix in the ``s3://`` URI. The following example uploads the
local files on disk to the ``bucket`` bucket and stores the files under the
``foo`` key prefix.


Download an |S3| Bucket
-----------------------

You can recursively download an |S3| bucket to a local directory on disk
by specifying the ``$source`` argument as an |S3| URI
(e.g., ``s3://bucket``) and the ``$dest`` argument as the path to a local
directory.

**Sample Code**

.. literalinclude:: example_code/s3/TransferManager.php
   :lines: 49-54
   :language: php

.. literalinclude:: example_code/s3/TransferManager.php
   :lines: 43-44
   :language: php


.. note::

    The |sdk-php| automatically creates any necessary directories when
    downloading the objects that are in the bucket.

You can include a key prefix in the |S3| URI after the bucket to download
only objects stored under a "pseudo-folder". The following example downloads
only files stored under the "/foo" key prefix of the given bucket.


Configuration
-------------

The ``Transfer`` object constructor accepts the following arguments.

``$client``
    The ``Aws\ClientInterface`` object to use to perform the transfers.

``$source`` (string|``\Iterator``)
    The source data being transferred. This can point
    to a local path on disk (e.g., ``/path/to/files``) or an |S3| bucket
    (e.g., ``s3://bucket``). The ``s3://`` URI may also contain a key prefix
    that can be used to transfer only objects under a common prefix.

    If the ``$source`` argument is an |S3| URI, the ``$dest``
    argument must be a local directory (and vice versa).

    In addition to providing a string value, you can also provide an
    ``\Iterator`` object that yields absolute file names. If you provide an
    iterator, you **must** provide a ``base_dir`` option in the
    ``$options`` associative array.

``$dest``
    The destination to which the files will be transferred. If the ``$source``
    argument is a local path on disk, ``$dest`` must be an |S3|
    bucket URI (e.g., ``s3://bucket``). If the ``$source`` argument is an
    |S3| bucket URI, the ``$dest`` argument must be a local path on
    disk.

``$options``
    An associative array of :ref:`transfer options <s3_transfer_options>`.

.. _s3_transfer_options:

Transfer Options
----------------

``base_dir`` (string)
    Base directory of the source, if ``$source`` is an iterator. If
    the ``$source`` option is not an array, this option is ignored.

``before`` (callable)
    A callback to invoke before each transfer. The callback should
    have a function signature like ``function (Aws\Command $command) {...}``.
    The provided command will be a ``GetObject``, ``PutObject``,
    ``CreateMultipartUpload``, ``UploadPart``, or ``CompleteMultipartUpload``
    command.

``mup_threshold`` (int)
    Size in bytes in which a multipart upload should be used instead of
    ``PutObject``. Defaults to ``16777216`` (16 MB).

``concurrency`` (int, default=5)
    Number of files to upload concurrently. The ideal
    concurrency value will vary based on the number of files being uploaded and
    the average size of each file. Generally, smaller files benefit
    from a higher concurrency while larger files don't.

``debug`` (bool)
    Set to ``true`` to print out debug information for transfers. Set to
    an ``fopen()`` resource to write to a specific stream instead of writing
    to STDOUT.

Transfer files Asynchronously
-----------------------------

The ``Transfer`` object is an instance of
``GuzzleHttp\Promise\PromisorInterface``. This means that the transfer can
occur asynchronously and is initiated by calling the ``promise`` function of the
object.


**Sample Code**

.. literalinclude:: example_code/s3/TransferManager.php
   :lines: 50-54
   :language: php

.. literalinclude:: example_code/s3/TransferManager.php
   :lines: 58-64
   :language: php
   :dedent: 4


If any of the files fail to transfer, the promise is rejected. You can
handle the failed transfer asynchronously using the ``otherwise`` function of the
promise. The ``otherwise`` function accepts a callback to invoke when an error
occurs. The callback accepts the ``$reason`` for the rejection, which is
typically an instance of ``Aws\Exception\AwsException`` (although a value of
**any** type can be delivered to the callback).

.. code-block:: php

    $promise->otherwise(function ($reason) {
        echo 'Transfer failed: ';
        var_dump($reason);
    });

Because the ``Transfer`` object returns a promise, these transfers can occur
concurrently with other asynchronous promises.

Customize the Transfer Manager's Commands
-----------------------------------------

You can set custom options on the operations executed by the transfer manager via
a callback passed to its constructor.

.. code-block:: php

    $uploader = new Transfer($s3Client, $source, $dest, [
        'before' => function (\Aws\Command $command) {
            // Commands can vary for multipart uploads, so check which command
            // is being processed
            if (in_array($command->getName(), ['PutObject', 'CreateMultipartUpload'])) {
                // Set custom cache-control metadata
                $command['CacheControl'] = 'max-age=3600';
                // Apply a canned ACL
                $command['ACL'] = strpos($command['Key'], 'CONFIDENTIAL') === false
                    ? 'public-read'
                    : 'private';
            }
        },
    ]);
