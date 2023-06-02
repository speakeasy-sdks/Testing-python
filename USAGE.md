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