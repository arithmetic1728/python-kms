from google.cloud import kms_v1

import logging
from http.client import HTTPConnection

def debug_requests_on():
    '''Switches on logging of the requests module.'''
    HTTPConnection.debuglevel = 1

    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)
    requests_log = logging.getLogger("requests.packages.urllib3")
    requests_log.setLevel(logging.DEBUG)
    requests_log.propagate = True

debug_requests_on()

project = "sijunliu-nondca-test"

client = kms_v1.KeyManagementServiceClient()
parent = f"projects/{project}/locations/global"
res = client.list_key_rings(request={"parent": parent})
print(res)

# Run GRPC_VERBOSITY=info RPC_TRACE=api python sample.py