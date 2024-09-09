---
title: Edge Delivery Services for AEM Forms commonly used regex expressions for validating form fields
description: Edge Delivery Services for AEM Forms commonly used regex expressions for validating form fields
feature: Edge Delivery Services
role: User
hide: yes
hidefromtoc: yes
exl-id: 5cfe23bb-155f-4639-b7b7-5edc172ba92a
---
# Commonly used regex expressions for validations

Here are some regular expressions you can use to enhance form validation beyond what modern browsers offer:

## Strong Password

```regex 

^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$

```

Ensures at least 8 characters with:

* Lowercase letter (a-z)
* Uppercase letter (A-Z)
* Digit (0-9)
* Special character (@$!%*?&)


## Email Address


```regex 

^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$

```

Allows letters, numbers, and special characters in the username and domain name.


## Phone Number (US format)

```regex 

^\(?([0-9]{3})\)?[-. ]([0-9]{3})[-. ]([0-9]{4})$

```

Validates phone numbers in the format (XXX) XXX-XXXX.



## URL

```regex 

^(http|https)://.*$

```

Ensures a valid URL starting with http or https.



## Date (YYYY-MM-DD)

```regex 

^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$

```

Validates dates in the format YYYY-MM-DD.


## Time (HH:MM)

```regex 

^([01][0-9]|2[0-3]):[0-5][0-9]$

```

Validates times in the format HH:MM (24-hour format).


## Zip Code (US format)

```regex 

^\d{5}(?:[-\ ]\d{4})?$

```

Validates 5-digit US zip codes with optional hyphen and 4-digit extension.


## Username (alphanumeric and underscore)

```regex 

^[a-zA-Z0-9_]+$

```

Allows letters, numbers, and underscores.


## Color Hex Code

```regex 

^#[0-9a-fA-F]{6}$

```

Validates 6-digit hex color codes. For example, #FFFFFF.


## IP Address

```regex 

^(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[0-9]{2,3})\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[0-9]{2,3})\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[0-9]{2,3})\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[0-9]{2,3})$

```

Validates IPv4 addresses.



## Social Security Number (US format)

```regex 

^\d{3}-\d{2}-\d{4}$

```



## Credit Card Number

```regex 

^(?:4[0-9]{12}(?:[0-9]{3})?|[25][1-7][0-9]{14}$

```

Validates phone numbers in the format (XXX) XXX-XXXX.



## Phone Number (US format):

```regex 

^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$


```

Validates phone numbers in the format (XXX) XXX-XXXX.
