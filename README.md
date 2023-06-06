# One2One

## Database design

### User

| Field | Type | Description |
| --- | --- | --- |
| id | int | Primary key |
| first_name | varchar(255) | First name |
| last_name | varchar(255) | Last name |
| username | varchar(255) | Username |
| age | int | Age |
| created_at | datetime | Created at |
| updated_at | datetime | Updated at |

### Contact

| Field | Type | Description |
| --- | --- | --- |
| id | int | Primary key |
| user_id | int | Foreign key to User |
| phone | varchar(255) | Phone number |
| address | varchar(255) | Address |
| city | varchar(255) | City |

### Group

| Field | Type | Description |
| --- | --- | --- |
| id | int | Primary key |
| name | varchar(20) | group name |
| students | list[int] | students |

## API

### Endpoints

#### User

| Method | Endpoint | Description |
| --- | --- | --- |
| GET | /users | Get all users |
| GET | /users/:id | Get user by id |
| POST | /users | Create user |
| PUT | /users/:id | Update user |
| DELETE | /users/:id | Delete user |

#### Contact

| Method | Endpoint | Description |
| --- | --- | --- |
| GET | /users/:user_id/contact | Get user contact |
| POST | /users/:user_id/contact | Create contact |
| PUT | /users/:user_id/contact | Update contact |
| DELETE | /users/:user_id/contact | Delete contact |

#### Group

| Method | Endpoint | Description |
| --- | --- | --- |
| GET | /groups | Get groups |
| GET | /groups/:group_id | Get group |
| POST | /groups | Create group |
| PUT | /groups/:group_id | Update group |
| DELETE | /groups/:group_id | Delete group |
| GET | /groups/:gruop_id/students | Get students by group id |
| POST | /group/:groups_id/add/:student_id | Add student to group |
| DELETE | /group/:groups_id/remove/:student_id | Remove student from froup |

### Request & Response

#### User

##### GET /users

Request:

```
curl -X GET http://localhost:8000/users
```

Response:

```
[
    {
        "id": 1,
        "first_name": "John",
        "last_name": "Doe",
        "username": "johndoe",
        "age": 20,
        "created_at": "2020-01-01 00:00:00",
        "updated_at": "2020-01-01 00:00:00"
    },
    {
        "id": 2,
        "first_name": "Jane",
        "last_name": "Doe",
        "username": "janedoe",
        "age": 20,
        "created_at": "2020-01-01 00:00:00",
        "updated_at": "2020-01-01 00:00:00"
    }
]
```

##### GET /users/:id

Request:

```
curl -X GET http://localhost:8000/users/1
```

Response:

```json
{
    "id": 1,
    "first_name": "John",
    "last_name": "Doe",
    "username": "johndoe",
    "age": 20,
    "created_at": "2020-01-01 00:00:00",
    "updated_at": "2020-01-01 00:00:00"
}
```

##### POST /users

Request:

```
curl -X POST \
    -H "Content-Type: application/json" \
    -d '{"first_name": "John", "last_name": "Doe", "username": "johndoe", "age": 20}' \
    http://localhost:8000/users
```

Response:

```json
{
    "id": 1,
    "first_name": "John",
    "last_name": "Doe",
    "username": "johndoe",
    "age": 20,
    "created_at": "2020-01-01 00:00:00",
    "updated_at": "2020-01-01 00:00:00"
}
```

##### PUT /users/:id

Request:

```
curl -X PUT \
    -H "Content-Type: application/json" \
    -d '{"first_name": "John", "last_name": "Doe", "username": "johndoe", "age": 20}' \
    http://localhost:8000/users/1
```

Response:

```json
{
    "id": 1,
    "first_name": "John",
    "last_name": "Doe",
    "username": "johndoe",
    "age": 20,
    "created_at": "2020-01-01 00:00:00",
    "updated_at": "2020-01-01 00:00:00"
}
```

##### DELETE /users/:id

Request:

```
curl -X DELETE http://localhost:8000/users/1
```

Response:

```
{
    "message": "User deleted"
}
```

#### Contact

##### GET /users/:user_id/contact

Request:

```
curl -X GET http://localhost:8000/users/1/contact
```

Response:

```json
{
    "id": 1,
    "user_id": 1,
    "phone": "08123456789",
    "address": "Jl. Jalan",
    "city": "Jakarta"
}
```

##### POST /users/:user_id/contact

Request:

```
curl -X POST \
    -H "Content-Type: application/json" \
    -d '{"phone": "08123456789", "address": "Jl. Jalan", "city": "Jakarta"}' \
    http://localhost:8000/users/1/contact
```

Response:

```json
{
    "id": 1,
    "user_id": 1,
    "phone": "08123456789",
    "address": "Jl. Jalan",
    "city": "Jakarta"
}
```

##### PUT /users/:user_id/contact

Request:

```
curl -X PUT \
    -H "Content-Type: application/json" \
    -d '{"phone": "08123456789", "address": "Jl. Jalan", "city": "Jakarta"}' \
    http://localhost:8000/users/1/contact
```

Response:

```json
{
    "id": 1,
    "user_id": 1,
    "phone": "08123456789",
    "address": "Jl. Jalan",
    "city": "Jakarta"
}
```

##### DELETE /users/:user_id/contact

Request:

```
curl -X DELETE http://localhost:8000/users/1/contact
```

Response:

```
{
    "message": "Contact deleted"
}
```
