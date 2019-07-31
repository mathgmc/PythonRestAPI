#Simple Employee Registry API

This is a simple REST API build in Python using Flask, and wrapped in a docker container. The API only register, list and delete employees, as specified in the following sections.

## Usage

All the API responses will have the following form:

```json
{
    "message": "Descriptive message of what happened on the API",
    "data": "Mixed type that holds the content of the response"
}
```

The following responses definitions will detail only the expected value of the `data` field;

### List all employee

**Definition**

`GET /employee`

**Response**

- `200 OK` - on success

```json
[
    {
        "identifier": "1001",
        "name": "Jorge Campos",
        "age": "33",
        "role": "Developer",
        "tel-number": "55 11 98989-8989"
    },
    {
        "identifier": "1002",
        "name": "Julia Costa",
        "age": "35",
        "role": "Head of Marketing",
        "tel_number": "55 13 90909-0909"
    }
]
```

### Registering a new employee

**Definition**

`POST /employee`

**Arguments**

- `"identifier":integer` a globally unique identifier for this employee
- `"name":string` the name of the employee
- `"age":integer` the age of the employee
- `"role":string` the role of the employee on the company
- `"tel_number":string` the telephone number of the employee

**Response**

- `403 Forbidden - Employee already exists` if the employee already exists

- `201 Created` on success

```json
{
    "identifier": "1001",
    "name": "Jorge Campos",
    "age": "33",
    "role": "Developer",
    "tel_number": "55 11 98989-8989"
}
```

### Lookup employee details

`GET /employee/<identifier>`

**Response**

- `404 Not Found` if the employee does not exist

- `200 OK` on success
```json
{
    "identifier": "1001",
    "name": "Jorge Campos",
    "age": "33",
    "role": "Developer",
    "tel-number": "55 11 98989-8989"
}
```

### Update a employee

**Definition**

`PUT /employee/<identifier>`

**Response**

- `404 Not Found` if the employee does not exist

- `201 Employee updated` on success
```json
{
    "identifier": "1001",
    "name": "Jorge Campos",
    "age": "33",
    "role": "Developer",
    "tel-number": "55 11 98989-8989"
}
```
### Delete a employee

**Definition**

`DELETE /employee/<identifier>`

**Response**

- `404 Not Found` if the employee does not exist
- `204 No Content` on success
