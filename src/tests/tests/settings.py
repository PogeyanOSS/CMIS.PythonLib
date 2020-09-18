#
#      Licensed to the Apache Software Foundation (ASF) under one
#      or more contributor license agreements.  See the NOTICE file
#      distributed with this work for additional information
#      regarding copyright ownership.  The ASF licenses this file
#      to you under the Apache License, Version 2.0 (the
#      "License"); you may not use this file except in compliance
#      with the License.  You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#      Unless required by applicable law or agreed to in writing,
#      software distributed under the License is distributed on an
#      "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
#      KIND, either express or implied.  See the License for the
#      specific language governing permissions and limitations
#      under the License.
#
from cmislib.atompub.binding import AtomPubBinding
from cmislib.browser.binding import BrowserBinding

#
# Override these settings with values to match your environment.
#
# CMIS repository's service URL
# REPOSITORY_URL = 'http://cmis.alfresco.com/s/cmis' # Alfresco demo
REPOSITORY_URL = 'http://dapps-02.chainin.io:9080/sapp-cms/amrutha072000_gmail_com-default' # Apache Chemistry AtomPub
#REPOSITORY_URL = 'http://localhost:8081/chemistry/browser' # Apache Chemistry Browser
# REPOSITORY_URL = 'http://localhost:8080/alfresco/cmisatom'  # Alfresco 4.0 AtomPub
# REPOSITORY_URL = 'http://localhost:8080/alfresco/s/api/cmis'  # Alfresco
# REPOSITORY_URL = 'http://localhost:8080/alfresco/api/-default-/cmis/versions/1.0/atom' # Alfresco 4.2 CMIS 1.0 Atom
# REPOSITORY_URL = 'https://docs.dstech.info/alfresco/api/-default-/cmis/versions/1.1/atom' # Alfresco 4.2 CMIS 1.1 Atom
#REPOSITORY_URL = 'http://cmis.demo.nuxeo.org/nuxeo/atom/cmis' # Nuxeo demo
#REPOSITORY_URL = 'http://localhost:8080/nuxeo/atom/cmis' # Nuxeo local

# Choose a binding. The AtomPubBinding is the only one you should really be using right now
#BINDING = AtomPubBinding()
BINDING = BrowserBinding()

# CMIS repository credentials
USERNAME = '7cad5de9-de6c-409f-bbe8-e066623db650'  # Alfresco
PASSWORD = 'eyJraWQiOiJYSVwvSktRYUJYZ3UwK3MwZ0s3akZTd2FzZk9OZmR5dmRzQVwvUVJYUmFJeXc9IiwiYWxnIjoiUlMyNTYifQ.eyJjdXN0b206emlwQ29kZSI6IjAwMDEyMyIsImN1c3RvbTpjb3VudHJ5IjoiSW5kaWEiLCJzdWIiOiI3Y2FkNWRlOS1kZTZjLTQwOWYtYmJlOC1lMDY2NjIzZGI2NTAiLCJjb2duaXRvOmdyb3VwcyI6WyJhbXJ1dGhhMDcyMDAwX2dtYWlsX2NvbV9Db21wYW55X1N5c3RlbUFkbWluIiwiYW1ydXRoYTA3MjAwMF9nbWFpbF9jb21fQ29tcGFueSIsIlRlbmFudEdyb3VwIl0sImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJjdXN0b206YWRkcmVzcyI6IlBFU0lUIiwiY3VzdG9tOmxhc3ROYW1lIjoiQUJDIiwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLmFwLXNvdXRoLTEuYW1hem9uYXdzLmNvbVwvYXAtc291dGgtMV8zNHk1U0c1bDYiLCJjb2duaXRvOnVzZXJuYW1lIjoiN2NhZDVkZTktZGU2Yy00MDlmLWJiZTgtZTA2NjYyM2RiNjUwIiwiY3VzdG9tOnN0YXRlIjoia2FybmF0a2EiLCJjdXN0b206Y29udGFjdFBlcnNvbiI6IkZhaGFkIiwiY3VzdG9tOnRlbmFudElkIjoiOTE1NmMwMTAtYmI1NC0xMWVhLWE4MDctNTMyY2VlNDI5MjU3IiwiY29nbml0bzpyb2xlcyI6WyJhcm46YXdzOmlhbTo6NTI2ODIxNTM3NDY2OnJvbGVcL0RTLUNvZ25pdG8tVGVuYW50R3JvdXBSb2xlLTE5RERGSlVKOFdWVzMiXSwiYXVkIjoiNW1sMTN2OHNtb2hmbGNhZzRodnBxZTdpaGQiLCJldmVudF9pZCI6ImE2YjNjZjQyLTk0MmUtNGZiMC1iZTNiLWQyMzBhZWZhMTkyMSIsImN1c3RvbTpmaXJzdE5hbWUiOiJBbXJ1dGhhIiwidG9rZW5fdXNlIjoiaWQiLCJjdXN0b206cGhvbmVOdW1iZXIiOiIrOTE4MTQ3MTkwMDYwIiwiYXV0aF90aW1lIjoxNTk0ODcwMDc4LCJjdXN0b206Y29tcGFueU5hbWUiOiJhbXJ1dGhhMDcyMDAwX2dtYWlsX2NvbSIsImV4cCI6MTU5NDg3MzY3OCwiaWF0IjoxNTk0ODcwMDc4LCJlbWFpbCI6ImFtcnV0aGEwNzIwMDBAZ21haWwuY29tIn0.mJ7M2ZKB1mhaYuTwvYFZVC5UeGjZ1XU9lPHifFJu4LjybVNCILdXq3rDDYOO5kWEY4KiRje1vpYYrE1H8nSDdd5A0F2cyoDHUnW3VMy6NGCcCb2bl3SS359r1jMFZjWCE7z41quRZOAjkHC7bF1Cr-so2lmT-dSzN7sJU58fVGR31HZxy6gD8ja0gKAYFJ7PZT1IiwxV22wDPtt7dFgUlwgLx0SdP77A6bVmWMaGut69kIQg-ZWjfn9BKkwlW3owBytYNi2L3AU-cTzjYWPvWSNdAtj-RbL5I0GqiPq38JnjNsXwX7M6W6wQFDE5WzuLQApM3IkZrtpR0_Hr938nyw'  # Alfresco
#USERNAME = ''
#PASSWORD = ''
#USERNAME = 'Administrator'  # Nuxeo
#PASSWORD = 'Administrator'  # Nuxeo
EXT_ARGS = {}
#EXT_ARGS = {'alf_ticket': 'TICKET_cef29079d8d5341338bf372b08278bc30ec89380'}
# Absolute path to a directory where test folders can be created, including
# the trailing slash.
#TEST_ROOT_PATH = '/default-domain/workspaces/cmislib'  # No trailing slash
#TEST_ROOT_PATH = '/cmislib'  # No trailing slash
TEST_ROOT_PATH = '/'
# Binary test files. Assumed to exist in the same dir as this python script
TEST_BINARY_1 = 'sample_text'
TEST_BINARY_2 = 'hello'
# For repositories that support setting an ACL, the name of an existing
# principal ID to add to the ACL of a test object. Some repositories care
# if this ID doesn't exist. Some repositories don't.
#TEST_PRINCIPAL_ID = 'anyone'
TEST_PRINCIPAL_ID = 'admin'
# For repositories that may index test content asynchronously, the number of
# times a query is retried before giving up.
MAX_FULL_TEXT_TRIES = 10
# The number of seconds the test should sleep between tries.
FULL_TEXT_WAIT = 10
# Specify the type ID of a versionable type. If all types are versionable,
# specify cmis:document
VERSIONABLE_TYPE_ID = 'cmis:document'
#VERSIONABLE_TYPE_ID = 'cmisbook:pdf'
#VERSIONABLE_TYPE_ID = 'VersionableType'