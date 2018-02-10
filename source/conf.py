# -*- coding: utf-8 -*-
#
# AWS Sphinx configuration file.
#
# For more information about how to configure this file, see:
#
# https://w.amazon.com/bin/view/AWSDocs/SphinxToZonbook/
#

#
# General information about the project.
#

# Optional service/SDK name, typically the three letter acronym (TLA) that
# represents the service, such as 'SWF'. If this is an SDK, you can use 'SDK'
# here.
service_name = 'SDK'

# The long version of the service or SDK name, such as "Amazon Simple Workflow
# Service", "AWS Flow Framework for Ruby" or "AWS SDK for Java"
service_name_long = 'AWS SDK for PHP'

# The landing page for the service documentation.
service_docs_home = 'https://aws.amazon.com/documentation/sdk-for-php/'

# The project type, such as "Developer Guide", "API Reference", "User Guide",
# or whatever.
project = 'Developer Guide'

# A short description of the project.
project_desc = ' '.join([service_name_long, project])

# the output will be generated in <project_basename> and will appear on
# the web using the same basename in its URL.
project_basename = 'developer-guide'

# This name is used as the manual / PDF name. Don't include the extension
# (.pdf) here.
man_name = 'aws-sdk-php-v3-developer-guide'

# The language for this version of the docs. Typically 'en'. For a full list of
# values, see: http://sphinx-doc.org/config.html#confval-language
language = 'en'

# Whether or not to show the PDF link. If you generate a PDF for your
# documentation, set this to True.
show_pdf_link = True

# Whether or not to show the language selector
show_lang_selector = True

#
# Version Information
#

# The version info for the project you're documenting, acts as replacement for
# |version| and |release| substitutions in the documentation, and is also used
# in various other places throughout the built documents.
#
# The short X.Y version.

# version = '1.0'

# The full version, including alpha/beta/rc tags.

# release = '1.0'

#
# Forum Information
#

# Optional forum ID. If there's a relevant forum at forums.aws.amazon.com, then
# set the ID here. If not set, then no forum ID link will be generated.
#

forum_id = '80'

# The link to the top of the doc source tree on GitHub. This allows generation
# of per-page "Edit on GitHub" links.
#github_doc_url = 'https://github.com/<insert URL path here>/doc_source'

# This allows the "Feedback" button to create a new issue on GitHub.
#doc_feedback_url = 'https://github.com/<insert URL path here>/issues/new'

#
# Extra Navlinks
#

# Extra navlinks. You can specify additional links to appear in the top bar here
# as navlink name–url pairs. If extra_navlinks is not set, then no extra
# navlinks will be generated.
#
# Note: The following extra_navlinks were a guess, and never seemed to actually
# do anything to the built HTML docs.
extra_navlinks = [
#    ('SDK Home', 'https://aws.amazon.com/sdk-for-php/'),
#    ('GitHub', 'https://github.com/aws/aws-sdk-php'),
]

build_html = True
build_pdf = True
build_mobi = False # Or the Kindle ASIN if you need a Kindle build

feedback_folder_id = '4556e6d1-d4de-4ae1-ab9e-22a40dc5ad49'

# For the URL, e.g. http://docs.aws.amazon.com/docset/version/guide
docset_path_slug = 'sdk-for-php'
version_path_slug = 'v3'
guide_path_slug = 'developer-guide'

#
# EXTRA_CONF_CONTENT -- don't change, move or remove this line!
#

# Any settings *below* this act as overrides for the default config content.
# Declare extlinks <http://www.sphinx-doc.org/en/stable/ext/extlinks.html> and
# additional configuration details specific to this documentation set here.
#

# default code language for syntax highlighting
highlight_language = 'php'

if 'extlinks' not in vars():
    extlinks = {}

#
# The following example is one way to declare extlinks; for others, see:
# https://code.amazon.com/packages/AWSSdkDocsGo/blobs/mainline/--/source/conf.py
# https://code.amazon.com/packages/AWSSDKDocsJavav2/blobs/mainline/--/source/conf.py
# https://code.amazon.com/packages/AWSSdkDocsNET/blobs/mainline/--/source/conf.py
# https://code.amazon.com/packages/AWSSdkDocsRuby/blobs/mainline/--/source/conf.py
# https://github.com/awsdocs/aws-doc-shared-content/blob/master/sphinx_shared/_conf/default_extlinks.py
#
#extlinks.update({
#    'aws-cpp-class': ('https://sdk.amazonaws.com/cpp/api/LATEST/class_%s.html', ''),
#    'aws-cpp-namespace': ('https://sdk.amazonaws.com/cpp/api/LATEST/namespace_%s.html', ''),
#    'aws-cpp-struct': ('https://sdk.amazonaws.com/cpp/api/LATEST/struct_%s.html', ''),
#    'sdk-examples-cpp': ('https://github.com/awsdocs/aws-doc-sdk-examples/tree/master/cpp/example_code/%s', ''),
#    'sdk-source': ('https://github.com/aws/aws-sdk-cpp/tree/master/%s', ''),
#})
