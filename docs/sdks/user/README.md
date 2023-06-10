# user

## Overview

Operations about user

### Available Operations

* [create_user_form](#create_user_form) - Create user
* [create_user_json](#create_user_json) - Create user
* [create_user_raw](#create_user_raw) - Create user
* [create_users_with_list_input](#create_users_with_list_input) - Creates list of users with given input array
* [delete_user](#delete_user) - Delete user
* [get_user_by_name](#get_user_by_name) - Get user by user name
* [login_user](#login_user) - Logs user into the system
* [logout_user](#logout_user) - Logs out current logged in user session
* [update_user_form](#update_user_form) - Update user
* [update_user_json](#update_user_json) - Update user
* [update_user_raw](#update_user_raw) - Update user

## create_user_form

This can only be done by the logged in user.

### Example Usage

```python
import petstore
from petstore.models import shared

s = petstore.Petstore()

req = shared.User(
    email='john@email.com',
    first_name='John',
    id=10,
    last_name='James',
    password='12345',
    phone='12345',
    user_status=1,
    username='theUser',
)

res = s.user.create_user_form(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                  | Type                                       | Required                                   | Description                                |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `request`                                  | [shared.User](../../models/shared/user.md) | :heavy_check_mark:                         | The request object to use for the request. |


### Response

**[operations.CreateUserFormResponse](../../models/operations/createuserformresponse.md)**


## create_user_json

This can only be done by the logged in user.

### Example Usage

```python
import petstore
from petstore.models import shared

s = petstore.Petstore()

req = shared.User(
    email='john@email.com',
    first_name='John',
    id=10,
    last_name='James',
    password='12345',
    phone='12345',
    user_status=1,
    username='theUser',
)

res = s.user.create_user_json(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                  | Type                                       | Required                                   | Description                                |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `request`                                  | [shared.User](../../models/shared/user.md) | :heavy_check_mark:                         | The request object to use for the request. |


### Response

**[operations.CreateUserJSONResponse](../../models/operations/createuserjsonresponse.md)**


## create_user_raw

This can only be done by the logged in user.

### Example Usage

```python
import petstore
from petstore.models import shared

s = petstore.Petstore()

req = 'quasi'.encode()

res = s.user.create_user_raw(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                  | Type                                       | Required                                   | Description                                |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `request`                                  | [bytes](../../models//.md)                 | :heavy_check_mark:                         | The request object to use for the request. |


### Response

**[operations.CreateUserRawResponse](../../models/operations/createuserrawresponse.md)**


## create_users_with_list_input

Creates list of users with given input array

### Example Usage

```python
import petstore
from petstore.models import shared

s = petstore.Petstore()

req = [
    shared.User(
        email='john@email.com',
        first_name='John',
        id=10,
        last_name='James',
        password='12345',
        phone='12345',
        user_status=1,
        username='theUser',
    ),
    shared.User(
        email='john@email.com',
        first_name='John',
        id=10,
        last_name='James',
        password='12345',
        phone='12345',
        user_status=1,
        username='theUser',
    ),
    shared.User(
        email='john@email.com',
        first_name='John',
        id=10,
        last_name='James',
        password='12345',
        phone='12345',
        user_status=1,
        username='theUser',
    ),
    shared.User(
        email='john@email.com',
        first_name='John',
        id=10,
        last_name='James',
        password='12345',
        phone='12345',
        user_status=1,
        username='theUser',
    ),
]

res = s.user.create_users_with_list_input(req)

if res.user is not None:
    # handle response
```

### Parameters

| Parameter                                  | Type                                       | Required                                   | Description                                |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `request`                                  | [list[shared.User]](../../models//.md)     | :heavy_check_mark:                         | The request object to use for the request. |


### Response

**[operations.CreateUsersWithListInputResponse](../../models/operations/createuserswithlistinputresponse.md)**


## delete_user

This can only be done by the logged in user.

### Example Usage

```python
import petstore
from petstore.models import operations

s = petstore.Petstore()

req = operations.DeleteUserRequest(
    username='Weston_Thiel',
)

res = s.user.delete_user(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.DeleteUserRequest](../../models/operations/deleteuserrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.DeleteUserResponse](../../models/operations/deleteuserresponse.md)**


## get_user_by_name

Get user by user name

### Example Usage

```python
import petstore
from petstore.models import operations

s = petstore.Petstore()

req = operations.GetUserByNameRequest(
    username='Whitney.Bednar',
)

res = s.user.get_user_by_name(req)

if res.user is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.GetUserByNameRequest](../../models/operations/getuserbynamerequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.GetUserByNameResponse](../../models/operations/getuserbynameresponse.md)**


## login_user

Logs user into the system

### Example Usage

```python
import petstore
from petstore.models import operations

s = petstore.Petstore()

req = operations.LoginUserRequest(
    password='cum',
    username='Aiyana.Batz',
)

res = s.user.login_user(req)

if res.login_user_200_application_json_string is not None:
    # handle response
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.LoginUserRequest](../../models/operations/loginuserrequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.LoginUserResponse](../../models/operations/loginuserresponse.md)**


## logout_user

Logs out current logged in user session

### Example Usage

```python
import petstore


s = petstore.Petstore()


res = s.user.logout_user()

if res.status_code == 200:
    # handle response
```


### Response

**[operations.LogoutUserResponse](../../models/operations/logoutuserresponse.md)**


## update_user_form

This can only be done by the logged in user.

### Example Usage

```python
import petstore
from petstore.models import operations, shared

s = petstore.Petstore()

req = operations.UpdateUserFormRequest(
    user=shared.User(
        email='john@email.com',
        first_name='John',
        id=10,
        last_name='James',
        password='12345',
        phone='12345',
        user_status=1,
        username='theUser',
    ),
    username='Wilfrid.Carter',
)

res = s.user.update_user_form(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.UpdateUserFormRequest](../../models/operations/updateuserformrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.UpdateUserFormResponse](../../models/operations/updateuserformresponse.md)**


## update_user_json

This can only be done by the logged in user.

### Example Usage

```python
import petstore
from petstore.models import operations, shared

s = petstore.Petstore()

req = operations.UpdateUserJSONRequest(
    user=shared.User(
        email='john@email.com',
        first_name='John',
        id=10,
        last_name='James',
        password='12345',
        phone='12345',
        user_status=1,
        username='theUser',
    ),
    username='Jayden.Carter88',
)

res = s.user.update_user_json(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.UpdateUserJSONRequest](../../models/operations/updateuserjsonrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.UpdateUserJSONResponse](../../models/operations/updateuserjsonresponse.md)**


## update_user_raw

This can only be done by the logged in user.

### Example Usage

```python
import petstore
from petstore.models import operations, shared

s = petstore.Petstore()

req = operations.UpdateUserRawRequest(
    request_body='commodi'.encode(),
    username='Terrill69',
)

res = s.user.update_user_raw(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.UpdateUserRawRequest](../../models/operations/updateuserrawrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.UpdateUserRawResponse](../../models/operations/updateuserrawresponse.md)**

