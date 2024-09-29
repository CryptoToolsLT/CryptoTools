import validators
import re
import typing

validate_ascii_not_empty = re.compile(r'^[\x20-\x7e]+$')
validate_unicode_not_empty = re.compile(r'^(\w|[\x20-\x7e])+$')

def email_error(email: str, field_name: str = 'email') -> str|None:
    if validators.email(email) is True:
        return None
    return f"invalid {field_name}"

def name_error(name: str, field_name: str = 'name') -> str|None:
    if validate_unicode_not_empty.match(name) is not None:
        return None
    return f"{field_name} contains invalid characters"

def password_error(password: str, field_name: str = 'password') -> str|None:
    if len(password) < 8:
        return f"{field_name} is too short - minimum 8 characters"
    if len(password) > 24:
        return f"{field_name} is too long - maximum 24 characters"
    if validate_ascii_not_empty.match(password) is not None:
        return None
    return f"{field_name} contains invalid characters"

ValidationType = typing.Literal['email', 'password', 'name']

class BaseValidation:
    def __init__(
        self,
        validation_type: ValidationType,
        field_name: str,
        field_value: str|int|None,
        required: bool,
        
        missing: bool,
        semantic_error: str|None,
    ):
        self.validation_type = validation_type
        self.field_name = field_name
        self.field_value = field_value
        self.required = required

        self.missing = missing
        self.semantic_error = semantic_error

class StrValidation(BaseValidation):
    def __init__(self,
        validation_type: ValidationType,
        field_name: str,
        field_value: str|None,
        required: bool = True,
    ):
        missing = False
        semantic_error = None

        if required and not field_value:
            missing = True
        
        if not missing:
            if field_value:
                if validation_type == 'email':
                    semantic_error = email_error(field_value, field_name)
                elif validation_type == 'password':
                    semantic_error = password_error(field_value, field_name)
                elif validation_type == 'name':
                    semantic_error = name_error(field_value, field_name)
                else:
                    raise RuntimeError(f"Invalid validation type: {validation_type}")
        
        super().__init__(
            validation_type,
            field_name,
            field_value,
            required,

            missing,
            semantic_error,
        )

def validation_error(validations: list[BaseValidation]) -> str|None:
    missing_fields: list[str] = []

    for v in validations:
        if v.missing:
            missing_fields.append(v.field_name)
    
    if len(missing_fields) > 0:
        return "Missing " + ', '.join(missing_fields)
    
    semantically_invalid_fields_errors: list[str] = list(
        filter(
            lambda x: x is not None,
            (v.semantic_error for v in validations),
        )
    ) # type: ignore

    if len(semantically_invalid_fields_errors) > 0:
        return "Error: " + ', '.join(semantically_invalid_fields_errors)

    return None
