from google.cloud import kms_v1

project = "sijunliu-nondca-test"

client = kms_v1.KeyManagementServiceClient()
parent = f"projects/{project}/locations/global"
res = client.list_key_rings(request={"parent": parent})
print(res)

# Run GRPC_VERBOSITY=info RPC_TRACE=api python sample.py