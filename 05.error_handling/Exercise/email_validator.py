import re


class MustContainAtSymbolError(Exception):
    pass


class MustContainOnlyOneAtSymbol(Exception):
    pass


class NameTooShortError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class ContainsOnlyWordsAndNumbers(Exception):
    pass


MIN_LENGHT = 4
VALID_DOMAINS = ['.com', '.bg', '.net', '.org']

pattern_name = r'[A-Za-z0-9]+'
pattern_domain = r'\.[a-z]+'

while True:
    emails = input()

    if emails == 'End':
        break

    if '@' not in emails:
        raise MustContainAtSymbolError('Email must contain @')

    if emails.count('@') > 1:
        raise MustContainOnlyOneAtSymbol('Email should contain only one @ symbol')

    if len(emails.split('@')[0]) < MIN_LENGHT:
        raise NameTooShortError('Name must be more than 4 characters')

    if re.findall(pattern_domain, emails)[-1] not in VALID_DOMAINS:
        raise InvalidDomainError('Domain must be one of the following: .com, .bg, .org, .net')

    if re.findall(pattern_name, emails)[0] != emails.split('@')[0]:
        raise ContainsOnlyWordsAndNumbers('Email should contain only numbers and letters')
    print('Email is valid')
