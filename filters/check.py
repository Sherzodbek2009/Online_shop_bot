import re

def is_valid_name(name: str) -> bool:
    
    name = name.strip()

    # Bo‘sh yoki juda qisqa/uzun bo‘lsa
    if not (2 <= len(name) <= 50):
        return False

    pattern = r"^[A-Za-zА-Яа-яЁё\s\-]+$"
    return bool(re.match(pattern, name))
