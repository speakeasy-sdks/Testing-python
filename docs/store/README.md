# store

## Overview

Access to Petstore orders

Find out more about our store
<http://swagger.io>
### Available Operations

* [delete_order](#delete_order) - Delete purchase order by ID
* [get_inventory](#get_inventory) - Returns pet inventories by status
* [get_order_by_id](#get_order_by_id) - Find purchase order by ID
* [place_order_form](#place_order_form) - Place an order for a pet
* [place_order_json](#place_order_json) - Place an order for a pet
* [place_order_raw](#place_order_raw) - Place an order for a pet

## delete_order

For valid response try integer IDs with value < 1000. Anything above 1000 or nonintegers will generate API errors

### Example Usage

```python
import petstore
from petstore.models import operations

s = petstore.Petstore()

req = operations.DeleteOrderRequest(
    order_id=662527,
)

res = s.store.delete_order(req)

if res.status_code == 200:
    # handle response
```

## get_inventory

Returns a map of status codes to quantities

### Example Usage

```python
import petstore
from petstore.models import operations

s = petstore.Petstore()


res = s.store.get_inventory(operations.GetInventorySecurity(
    api_key="",
))

if res.get_inventory_200_application_json_object is not None:
    # handle response
```

## get_order_by_id

For valid response try integer IDs with value <= 5 or > 10. Other values will generate exceptions.

### Example Usage

```python
import petstore
from petstore.models import operations

s = petstore.Petstore()

req = operations.GetOrderByIDRequest(
    order_id=820994,
)

res = s.store.get_order_by_id(req)

if res.order is not None:
    # handle response
```

## place_order_form

Place a new order in the store

### Example Usage

```python
import petstore
import dateutil.parser
from petstore.models import shared

s = petstore.Petstore()

req = shared.Order(
    complete=False,
    id=10,
    pet_id=198772,
    quantity=7,
    ship_date=dateutil.parser.isoparse('2022-11-26T13:23:33.410Z'),
    status=shared.OrderStatus.APPROVED,
)

res = s.store.place_order_form(req)

if res.order is not None:
    # handle response
```

## place_order_json

Place a new order in the store

### Example Usage

```python
import petstore
import dateutil.parser
from petstore.models import shared

s = petstore.Petstore()

req = shared.Order(
    complete=False,
    id=10,
    pet_id=198772,
    quantity=7,
    ship_date=dateutil.parser.isoparse('2021-04-29T07:12:18.684Z'),
    status=shared.OrderStatus.APPROVED,
)

res = s.store.place_order_json(req)

if res.order is not None:
    # handle response
```

## place_order_raw

Place a new order in the store

### Example Usage

```python
import petstore
import dateutil.parser
from petstore.models import shared

s = petstore.Petstore()

req = 'laborum'.encode()

res = s.store.place_order_raw(req)

if res.order is not None:
    # handle response
```
