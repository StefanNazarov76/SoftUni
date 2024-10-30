class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


VALID_DOMAINS = ['com', 'bg', 'org', 'net']
MINIMUM_NAME_LENGTH = 4

email = input()
while email != 'End':
    if len(email.split('@')[0]) <= MINIMUM_NAME_LENGTH:
        raise NameTooShortError('Name must be more than 4 characters')

    if '@' not in email:
        raise MustContainAtSymbolError('Email must contain @')

    if email.split('.')[1] not in VALID_DOMAINS:
        raise InvalidDomainError(f'Domain must be one of the following: {', '.join('.' + d for d in VALID_DOMAINS)}')

    email = input()
