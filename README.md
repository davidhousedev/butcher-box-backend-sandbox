# ButcherBox Backend Sandbox

In this project, we take the same data model and implement it in
multiple different web frameworks to prototype which implementation
should be the next iteration of the ButcherBox backend.

# Implementations

For each implementation, if you plan to work on it, assign it to
yourself in the checkbox below. Once complete, update the next
checkbox. Then, create a Google Document, share it with
contributors, and link it below. Once the retrospective is
complete, check off the final checkbox.

Feel free to add more implementation ideas below!

- [Django Rest Framework](https://www.django-rest-framework.org/)
  - [x] Assigned: David House
  - [ ] Completed
  - [ ] Retrospective
- [Hasura](https://hasura.io/)
  - [ ] Assigned
  - [ ] Completed
  - [ ] Retrospective
- [Django Graphene](https://graphene-python.org/)
  - [ ] Assigned
  - [ ] Completed
  - [ ] Retrospective
- [Serverless JavaScript](https://github.com/serverless/serverless)
  - [ ] Assigned
  - [ ] Completed
  - [ ] Retrospective
- [Lumen REST](https://auth0.com/blog/developing-restful-apis-with-lumen/)
  - [ ] Assigned
  - [ ] Completed
  - [ ] Retrospective
- [GraphQL with Node and Pirsma](https://www.prisma.io/tutorials/bootstrap-a-graphql-server-for-nodejs-ct10)
  - [ ] Assigned
  - [ ] Completed
  - [ ] Retrospective

# Schema

For this project, use the same schema to create your POCs.

**Note**: Apply this schema using the best patterns available to the
tool that you're using. For example, for attributes `array of...`,
you may choose to implement this as a Foreign Key relationship from
the related model, rather than an array type in the declared model.
_Use your best judgement to write maintainble patterns_.

## Models

```
Legend:
! : Required
(...) : Default Value

Box
  id:        !int PRIMARY_KEY
  uid:       !str UUID4
  shipped:   datetime (null)
  delivered: datetime (null)
  box_items: array of BoxItem ([])
  type:      !relation->BoxType

BoxType:
  id:          !int PRIMARY_KEY
  uid:         !str UUID4
  name:        !str MAX_LENGTH=63
  description: !text MAX_LENGTH=511
  type:        !str ENUM[custom, static, assorted]

BoxItem
  id:      !int PRIMARY_KEY
  uid:     !str UUID4
  box:     !relation->Box
  product: !relation->Product
  type:    str ENUM[subscription, promotion, offer, addon] (subscription)

Product
  id:            !int PRIMARY_KEY
  uid:           !str UUID4
  name:          !str MAX_LENGTH=63
  description:   !text MAX_LENGTH=511
  weight_g:      !int
  size_cubic_cm: !int

Subscription
  id:                  !int PRIMARY_KEY
  uid:                 !str UUID4
  bill_date:           datetime (null)  # null if inactive subscription
  bill_frequency:      !int
  bill_interval:       !str ENUM[days, weeks, months]
  customer:            !relation->Customer
  box_type_preference: !relation->BoxType
  next_box:            relation->Box (null)

Customer
  id:    !int PRIMARY_KEY
  uid:   !str UUID4
  user:  !relation->User
  boxes: array of Box ([])

# Note: If a framework provides a default User model which loosely conforms
#       to this spec, use the one provided by the framework, rather than
#       re-implementing the User model yourself.
User
  id:            !int PRIMARY_KEY
  uid:           !str UUID4
  username:      !str
  password:      !str
  password_salt: !str
```

## API

```
Format:
route
METHOD: REQUEST_BODY -> RESPONSE_BODY

Legend:
! : Admin required
~ : User or Admin required

**Note**: for PATCH, we assume that the Request Body will be a subset
of attributes.


/subscriptions
~GET: EMPTY -> Subscription
~POST: Subscription -> Subscription

/subscriptions/{uid}
~PATCH: Subscription -> Subscription
~DELETE: EMPTY -> NO_CONTENT


/customers
!GET: EMPTY -> [Customer]
!POST: Customer -> Customer

/customers/{uid}
!GET: EMPTY -> Customer
~PATCH: Customer -> Customer
~DELETE: EMPTY -> NO_CONTENT


/boxes
~GET: EMPTY -> [Box]
~POST: Box -> Box

/boxes/{uid}
~GET: EMPTY -> [Box]
~PATCH: Box -> Box

/boxes/{uid}/items
~GET: EMPTY -> [BoxItem]
~POST: BoxItem -> BoxItem

/boxes/{uid}/items/{uid}
~GET: EMPTY -> BoxItem
~PATCH: BoxItem -> BoxItem
~DELETE: EMPTY -> NO_CONTENT


/box-types
GET: EMPTY -> [BoxType]
!POST: BoxType -> BoxType

/box-types/{uid}
GET: EMPTY -> [BoxType]
!PATCH: BoxItem -> BoxItem
!DELETE: EMPTY -> NO_CONTENT


/products
GET: EMPTY -> [Product]
!POST: Product -> Product

/products/{uid}
GET: EMPTY -> [Product]
!PATCH: BoxItem -> BoxItem
!DELETE: EMPTY -> NO_CONTENT

# TODO: API design for customer/user profile
```
