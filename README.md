# REDHAT_ASSIGNMENT

1. Explore openstack API reference guide of cinder and glance and construct curl commands for crud operations 
   ref-api-doc: https://docs.openstack.org/api-ref/image/

2. Write one python program which will accept endpoint,http method (GET or DELETE), API, token etc. and communicate with any OpenStack service to get particular information.
   You can use requests library for the same, https://www.w3schools.com/python/module_requests.asp <br/>
   E.g. If i want to get information related to particular image then I should run the program like
   ```
   python communicate_openstack.py <endpoint> <method> <API> <token>
   Python communicate_openstack.py http://10.0.78.195/image GET /v2/image/c38ca326-1b6f-4370-bac4-3734c3485081 xyzzzzzzzzzzzz  
   ```
