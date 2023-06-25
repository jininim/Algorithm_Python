def solution(phone_book):
    hash_map = {}
    
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        prefix = ""
        for digit in phone_number:
            prefix += digit
            if prefix != phone_number and prefix in hash_map:
                return False
    return True