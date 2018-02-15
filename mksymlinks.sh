#!/bin/bash

# create symlinks for working locally with GitHub repos
# rmsymlinks.sh removes these.

# PHP developer guide (GitHub)
ln -s $HOME/src/awsdocs/aws-php-developer-guide .
cd aws-php-developer-guide/doc_source

# SDK examples (GitHub), PHP
ln -s $HOME/src/awsdocs/aws-doc-sdk-examples/php/example_code .
cd ../..

# Shared content (GitHub)
ln -s $HOME/src/awsdocs/aws-doc-shared-content .

# Shared content (internal)
ln -s ../AwsSphinxSharedContent/ .
