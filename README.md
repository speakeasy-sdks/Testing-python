# petstore

<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install git+https://github.com/speakeasy-sdks/Testing-python.git
```
<!-- End SDK Installation -->

## SDK Example Usage
<!-- Start SDK Example Usage -->
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
        'provident',
        'distinctio',
        'quibusdam',
    ],
    status=shared.PetStatus.PENDING,
    tags=[
        shared.Tag(
            id=544883,
            name='Ben Mueller',
        ),
        shared.Tag(
            id=437587,
            name='Raquel Bednar',
        ),
        shared.Tag(
            id=383441,
            name='Alexandra Schulist',
        ),
        shared.Tag(
            id=568045,
            name='Mrs. Sophie Smith MD',
        ),
    ],
)

res = s.pet.add_pet_form(req, operations.AddPetFormSecurity(
    petstore_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.pet is not None:
    # handle response
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## Available Resources and Operations


### [pet](docs/pet/README.md)

* [add_pet_form](docs/pet/README.md#add_pet_form) - Add a new pet to the store
* [add_pet_json](docs/pet/README.md#add_pet_json) - Add a new pet to the store
* [add_pet_raw](docs/pet/README.md#add_pet_raw) - Add a new pet to the store
* [delete_pet](docs/pet/README.md#delete_pet) - Deletes a pet
* [find_pets_by_status](docs/pet/README.md#find_pets_by_status) - Finds Pets by status
* [find_pets_by_tags](docs/pet/README.md#find_pets_by_tags) - Finds Pets by tags
* [get_pet_by_id](docs/pet/README.md#get_pet_by_id) - Find pet by ID
* [update_pet_with_form](docs/pet/README.md#update_pet_with_form) - Updates a pet in the store with form data
* [update_pet_form](docs/pet/README.md#update_pet_form) - Update an existing pet
* [update_pet_json](docs/pet/README.md#update_pet_json) - Update an existing pet
* [update_pet_raw](docs/pet/README.md#update_pet_raw) - Update an existing pet
* [upload_file](docs/pet/README.md#upload_file) - uploads an image

### [store](docs/store/README.md)

* [delete_order](docs/store/README.md#delete_order) - Delete purchase order by ID
* [get_inventory](docs/store/README.md#get_inventory) - Returns pet inventories by status
* [get_order_by_id](docs/store/README.md#get_order_by_id) - Find purchase order by ID
* [place_order_form](docs/store/README.md#place_order_form) - Place an order for a pet
* [place_order_json](docs/store/README.md#place_order_json) - Place an order for a pet
* [place_order_raw](docs/store/README.md#place_order_raw) - Place an order for a pet

### [user](docs/user/README.md)

* [create_user_form](docs/user/README.md#create_user_form) - Create user
* [create_user_json](docs/user/README.md#create_user_json) - Create user
* [create_user_raw](docs/user/README.md#create_user_raw) - Create user
* [create_users_with_list_input](docs/user/README.md#create_users_with_list_input) - Creates list of users with given input array
* [delete_user](docs/user/README.md#delete_user) - Delete user
* [get_user_by_name](docs/user/README.md#get_user_by_name) - Get user by user name
* [login_user](docs/user/README.md#login_user) - Logs user into the system
* [logout_user](docs/user/README.md#logout_user) - Logs out current logged in user session
* [update_user_form](docs/user/README.md#update_user_form) - Update user
* [update_user_json](docs/user/README.md#update_user_json) - Update user
* [update_user_raw](docs/user/README.md#update_user_raw) - Update user
<!-- End SDK Available Operations -->

### Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

### Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release !

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
