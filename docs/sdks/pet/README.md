# pet

## Overview

Everything about your Pets

Find out more
<http://swagger.io>
### Available Operations

* [add_pet_form](#add_pet_form) - Add a new pet to the store
* [add_pet_json](#add_pet_json) - Add a new pet to the store
* [add_pet_raw](#add_pet_raw) - Add a new pet to the store
* [delete_pet](#delete_pet) - Deletes a pet
* [find_pets_by_status](#find_pets_by_status) - Finds Pets by status
* [find_pets_by_tags](#find_pets_by_tags) - Finds Pets by tags
* [get_pet_by_id](#get_pet_by_id) - Find pet by ID
* [update_pet_with_form](#update_pet_with_form) - Updates a pet in the store with form data
* [update_pet_form](#update_pet_form) - Update an existing pet
* [update_pet_json](#update_pet_json) - Update an existing pet
* [update_pet_raw](#update_pet_raw) - Update an existing pet
* [upload_file](#upload_file) - uploads an image

## add_pet_form

Add a new pet to the store

### Example Usage

```python
import petstore
from petstore.models import operations, shared

s = petstore.Petstore()

req = shared.Pet(
    category=shared.Category(
        id=1,
        name='Dogs',
    ),
    id=10,
    name='doggie',
    photo_urls=[
        'ipsam',
    ],
    status=shared.PetStatus.SOLD,
    tags=[
        shared.Tag(
            id=778157,
            name='Teri Strosin',
        ),
        shared.Tag(
            id=799159,
            name='Erik Lebsack',
        ),
        shared.Tag(
            id=118274,
            name='Luke McCullough',
        ),
        shared.Tag(
            id=944669,
            name='Everett Breitenberg',
        ),
    ],
)

res = s.pet.add_pet_form(req, operations.AddPetFormSecurity(
    petstore_auth="",
))

if res.pet is not None:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [shared.Pet](../../models/shared/pet.md)                                       | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `security`                                                                     | [operations.AddPetFormSecurity](../../models/operations/addpetformsecurity.md) | :heavy_check_mark:                                                             | The security requirements to use for the request.                              |


### Response

**[operations.AddPetFormResponse](../../models/operations/addpetformresponse.md)**


## add_pet_json

Add a new pet to the store

### Example Usage

```python
import petstore
from petstore.models import operations, shared

s = petstore.Petstore()

req = shared.Pet(
    category=shared.Category(
        id=1,
        name='Dogs',
    ),
    id=10,
    name='doggie',
    photo_urls=[
        'qui',
        'impedit',
    ],
    status=shared.PetStatus.SOLD,
    tags=[
        shared.Tag(
            id=216550,
            name='Brandon Auer',
        ),
        shared.Tag(
            id=149675,
            name='Curtis Morissette',
        ),
    ],
)

res = s.pet.add_pet_json(req, operations.AddPetJSONSecurity(
    petstore_auth="",
))

if res.pet is not None:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [shared.Pet](../../models/shared/pet.md)                                       | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `security`                                                                     | [operations.AddPetJSONSecurity](../../models/operations/addpetjsonsecurity.md) | :heavy_check_mark:                                                             | The security requirements to use for the request.                              |


### Response

**[operations.AddPetJSONResponse](../../models/operations/addpetjsonresponse.md)**


## add_pet_raw

Add a new pet to the store

### Example Usage

```python
import petstore
from petstore.models import operations, shared

s = petstore.Petstore()

req = 'saepe'.encode()

res = s.pet.add_pet_raw(req, operations.AddPetRawSecurity(
    petstore_auth="",
))

if res.pet is not None:
    # handle response
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [bytes](../../models//.md)                                                   | :heavy_check_mark:                                                           | The request object to use for the request.                                   |
| `security`                                                                   | [operations.AddPetRawSecurity](../../models/operations/addpetrawsecurity.md) | :heavy_check_mark:                                                           | The security requirements to use for the request.                            |


### Response

**[operations.AddPetRawResponse](../../models/operations/addpetrawresponse.md)**


## delete_pet

Deletes a pet

### Example Usage

```python
import petstore
from petstore.models import operations

s = petstore.Petstore()

req = operations.DeletePetRequest(
    api_key='fuga',
    pet_id=449950,
)

res = s.pet.delete_pet(req, operations.DeletePetSecurity(
    petstore_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.DeletePetRequest](../../models/operations/deletepetrequest.md)   | :heavy_check_mark:                                                           | The request object to use for the request.                                   |
| `security`                                                                   | [operations.DeletePetSecurity](../../models/operations/deletepetsecurity.md) | :heavy_check_mark:                                                           | The security requirements to use for the request.                            |


### Response

**[operations.DeletePetResponse](../../models/operations/deletepetresponse.md)**


## find_pets_by_status

Multiple status values can be provided with comma separated strings

### Example Usage

```python
import petstore
from petstore.models import operations

s = petstore.Petstore()

req = operations.FindPetsByStatusRequest(
    status=operations.FindPetsByStatusStatus.PENDING,
)

res = s.pet.find_pets_by_status(req, operations.FindPetsByStatusSecurity(
    petstore_auth="",
))

if res.pets is not None:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.FindPetsByStatusRequest](../../models/operations/findpetsbystatusrequest.md)   | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `security`                                                                                 | [operations.FindPetsByStatusSecurity](../../models/operations/findpetsbystatussecurity.md) | :heavy_check_mark:                                                                         | The security requirements to use for the request.                                          |


### Response

**[operations.FindPetsByStatusResponse](../../models/operations/findpetsbystatusresponse.md)**


## find_pets_by_tags

Multiple tags can be provided with comma separated strings. Use tag1, tag2, tag3 for testing.

### Example Usage

```python
import petstore
from petstore.models import operations

s = petstore.Petstore()

req = operations.FindPetsByTagsRequest(
    tags=[
        'iure',
        'saepe',
        'quidem',
    ],
)

res = s.pet.find_pets_by_tags(req, operations.FindPetsByTagsSecurity(
    petstore_auth="",
))

if res.pets is not None:
    # handle response
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.FindPetsByTagsRequest](../../models/operations/findpetsbytagsrequest.md)   | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `security`                                                                             | [operations.FindPetsByTagsSecurity](../../models/operations/findpetsbytagssecurity.md) | :heavy_check_mark:                                                                     | The security requirements to use for the request.                                      |


### Response

**[operations.FindPetsByTagsResponse](../../models/operations/findpetsbytagsresponse.md)**


## get_pet_by_id

Returns a single pet

### Example Usage

```python
import petstore
from petstore.models import operations

s = petstore.Petstore()

req = operations.GetPetByIDRequest(
    pet_id=99280,
)

res = s.pet.get_pet_by_id(req, operations.GetPetByIDSecurity(
    api_key="",
))

if res.pet is not None:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.GetPetByIDRequest](../../models/operations/getpetbyidrequest.md)   | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `security`                                                                     | [operations.GetPetByIDSecurity](../../models/operations/getpetbyidsecurity.md) | :heavy_check_mark:                                                             | The security requirements to use for the request.                              |


### Response

**[operations.GetPetByIDResponse](../../models/operations/getpetbyidresponse.md)**


## update_pet_with_form

Updates a pet in the store with form data

### Example Usage

```python
import petstore
from petstore.models import operations

s = petstore.Petstore()

req = operations.UpdatePetWithFormRequest(
    name='Lela Orn',
    pet_id=170909,
    status='dolorem',
)

res = s.pet.update_pet_with_form(req, operations.UpdatePetWithFormSecurity(
    petstore_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.UpdatePetWithFormRequest](../../models/operations/updatepetwithformrequest.md)   | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `security`                                                                                   | [operations.UpdatePetWithFormSecurity](../../models/operations/updatepetwithformsecurity.md) | :heavy_check_mark:                                                                           | The security requirements to use for the request.                                            |


### Response

**[operations.UpdatePetWithFormResponse](../../models/operations/updatepetwithformresponse.md)**


## update_pet_form

Update an existing pet by Id

### Example Usage

```python
import petstore
from petstore.models import operations, shared

s = petstore.Petstore()

req = shared.Pet(
    category=shared.Category(
        id=1,
        name='Dogs',
    ),
    id=10,
    name='doggie',
    photo_urls=[
        'explicabo',
        'nobis',
    ],
    status=shared.PetStatus.AVAILABLE,
    tags=[
        shared.Tag(
            id=363711,
            name='Velma Batz',
        ),
        shared.Tag(
            id=988374,
            name='Juan O'Hara',
        ),
        shared.Tag(
            id=161309,
            name='Shaun McCullough',
        ),
    ],
)

res = s.pet.update_pet_form(req, operations.UpdatePetFormSecurity(
    petstore_auth="",
))

if res.pet is not None:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [shared.Pet](../../models/shared/pet.md)                                             | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `security`                                                                           | [operations.UpdatePetFormSecurity](../../models/operations/updatepetformsecurity.md) | :heavy_check_mark:                                                                   | The security requirements to use for the request.                                    |


### Response

**[operations.UpdatePetFormResponse](../../models/operations/updatepetformresponse.md)**


## update_pet_json

Update an existing pet by Id

### Example Usage

```python
import petstore
from petstore.models import operations, shared

s = petstore.Petstore()

req = shared.Pet(
    category=shared.Category(
        id=1,
        name='Dogs',
    ),
    id=10,
    name='doggie',
    photo_urls=[
        'molestiae',
        'velit',
    ],
    status=shared.PetStatus.PENDING,
    tags=[
        shared.Tag(
            id=338007,
            name='Kayla O'Kon',
        ),
    ],
)

res = s.pet.update_pet_json(req, operations.UpdatePetJSONSecurity(
    petstore_auth="",
))

if res.pet is not None:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [shared.Pet](../../models/shared/pet.md)                                             | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `security`                                                                           | [operations.UpdatePetJSONSecurity](../../models/operations/updatepetjsonsecurity.md) | :heavy_check_mark:                                                                   | The security requirements to use for the request.                                    |


### Response

**[operations.UpdatePetJSONResponse](../../models/operations/updatepetjsonresponse.md)**


## update_pet_raw

Update an existing pet by Id

### Example Usage

```python
import petstore
from petstore.models import operations, shared

s = petstore.Petstore()

req = 'quo'.encode()

res = s.pet.update_pet_raw(req, operations.UpdatePetRawSecurity(
    petstore_auth="",
))

if res.pet is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [bytes](../../models//.md)                                                         | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `security`                                                                         | [operations.UpdatePetRawSecurity](../../models/operations/updatepetrawsecurity.md) | :heavy_check_mark:                                                                 | The security requirements to use for the request.                                  |


### Response

**[operations.UpdatePetRawResponse](../../models/operations/updatepetrawresponse.md)**


## upload_file

uploads an image

### Example Usage

```python
import petstore
from petstore.models import operations

s = petstore.Petstore()

req = operations.UploadFileRequest(
    request_body='sequi'.encode(),
    additional_metadata='tenetur',
    pet_id=368725,
)

res = s.pet.upload_file(req, operations.UploadFileSecurity(
    petstore_auth="",
))

if res.api_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.UploadFileRequest](../../models/operations/uploadfilerequest.md)   | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `security`                                                                     | [operations.UploadFileSecurity](../../models/operations/uploadfilesecurity.md) | :heavy_check_mark:                                                             | The security requirements to use for the request.                              |


### Response

**[operations.UploadFileResponse](../../models/operations/uploadfileresponse.md)**

