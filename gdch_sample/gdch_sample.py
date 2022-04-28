from google.cloud import kms_v1
from google.api_core.client_options import ClientOptions

options = ClientOptions(api_endpoint="<gdch_endpoint>")
project = "<project name>"

client = kms_v1.KeyManagementServiceClient(client_options=options)
parent = f"projects/{project}/locations/global"
res = client.list_key_rings(request={"parent": parent})
print(res)