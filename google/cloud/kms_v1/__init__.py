# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from google.cloud.kms_v1 import gapic_version as package_version

__version__ = package_version.__version__


from .services.ekm_service import EkmServiceAsyncClient, EkmServiceClient
from .services.key_management_service import (
    KeyManagementServiceAsyncClient,
    KeyManagementServiceClient,
)
from .types.ekm_service import (
    Certificate,
    CreateEkmConnectionRequest,
    EkmConnection,
    GetEkmConnectionRequest,
    ListEkmConnectionsRequest,
    ListEkmConnectionsResponse,
    UpdateEkmConnectionRequest,
)
from .types.resources import (
    CryptoKey,
    CryptoKeyVersion,
    CryptoKeyVersionTemplate,
    ExternalProtectionLevelOptions,
    ImportJob,
    KeyOperationAttestation,
    KeyRing,
    ProtectionLevel,
    PublicKey,
)
from .types.service import (
    AsymmetricDecryptRequest,
    AsymmetricDecryptResponse,
    AsymmetricSignRequest,
    AsymmetricSignResponse,
    CreateCryptoKeyRequest,
    CreateCryptoKeyVersionRequest,
    CreateImportJobRequest,
    CreateKeyRingRequest,
    DecryptRequest,
    DecryptResponse,
    DestroyCryptoKeyVersionRequest,
    Digest,
    EncryptRequest,
    EncryptResponse,
    GenerateRandomBytesRequest,
    GenerateRandomBytesResponse,
    GetCryptoKeyRequest,
    GetCryptoKeyVersionRequest,
    GetImportJobRequest,
    GetKeyRingRequest,
    GetPublicKeyRequest,
    ImportCryptoKeyVersionRequest,
    ListCryptoKeysRequest,
    ListCryptoKeysResponse,
    ListCryptoKeyVersionsRequest,
    ListCryptoKeyVersionsResponse,
    ListImportJobsRequest,
    ListImportJobsResponse,
    ListKeyRingsRequest,
    ListKeyRingsResponse,
    LocationMetadata,
    MacSignRequest,
    MacSignResponse,
    MacVerifyRequest,
    MacVerifyResponse,
    RestoreCryptoKeyVersionRequest,
    UpdateCryptoKeyPrimaryVersionRequest,
    UpdateCryptoKeyRequest,
    UpdateCryptoKeyVersionRequest,
)

__all__ = (
    "EkmServiceAsyncClient",
    "KeyManagementServiceAsyncClient",
    "AsymmetricDecryptRequest",
    "AsymmetricDecryptResponse",
    "AsymmetricSignRequest",
    "AsymmetricSignResponse",
    "Certificate",
    "CreateCryptoKeyRequest",
    "CreateCryptoKeyVersionRequest",
    "CreateEkmConnectionRequest",
    "CreateImportJobRequest",
    "CreateKeyRingRequest",
    "CryptoKey",
    "CryptoKeyVersion",
    "CryptoKeyVersionTemplate",
    "DecryptRequest",
    "DecryptResponse",
    "DestroyCryptoKeyVersionRequest",
    "Digest",
    "EkmConnection",
    "EkmServiceClient",
    "EncryptRequest",
    "EncryptResponse",
    "ExternalProtectionLevelOptions",
    "GenerateRandomBytesRequest",
    "GenerateRandomBytesResponse",
    "GetCryptoKeyRequest",
    "GetCryptoKeyVersionRequest",
    "GetEkmConnectionRequest",
    "GetImportJobRequest",
    "GetKeyRingRequest",
    "GetPublicKeyRequest",
    "ImportCryptoKeyVersionRequest",
    "ImportJob",
    "KeyManagementServiceClient",
    "KeyOperationAttestation",
    "KeyRing",
    "ListCryptoKeyVersionsRequest",
    "ListCryptoKeyVersionsResponse",
    "ListCryptoKeysRequest",
    "ListCryptoKeysResponse",
    "ListEkmConnectionsRequest",
    "ListEkmConnectionsResponse",
    "ListImportJobsRequest",
    "ListImportJobsResponse",
    "ListKeyRingsRequest",
    "ListKeyRingsResponse",
    "LocationMetadata",
    "MacSignRequest",
    "MacSignResponse",
    "MacVerifyRequest",
    "MacVerifyResponse",
    "ProtectionLevel",
    "PublicKey",
    "RestoreCryptoKeyVersionRequest",
    "UpdateCryptoKeyPrimaryVersionRequest",
    "UpdateCryptoKeyRequest",
    "UpdateCryptoKeyVersionRequest",
    "UpdateEkmConnectionRequest",
)
