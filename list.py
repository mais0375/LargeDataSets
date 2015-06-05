#!/usr/bin/env python
import os
import sys
import pysam
import subprocess
import stat
import swiftclient

#Lists all .bam files in Gemomdata swift object store.
if __name__ == '__main__':
    username = os.environ['OS_USERNAME']
    password = os.environ['OS_PASSWORD']
    tenant_name = os.environ['OS_TENANT_NAME']
    auth_url = os.environ['OS_AUTH_URL']
    conn = swiftclient.client.Connection(auth_version='2',user=username,key=password,tenant_name=tenant_name,authurl=auth_url)
    (response, obj_list) = conn.get_container('GenomeData')
    for obj in obj_list:
        if obj['name'].endswith('.bam'):
            print  obj['name']
