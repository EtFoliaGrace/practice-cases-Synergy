ALPHA = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
KEY = "КАЗАХСТАН"


def encrypt(text, key):
    text = text.upper()
    key = key.upper()
    result = []
    key_index = 0

    for ch in text:
        if ch in ALPHA:
            text_index = ALPHA.index(ch)
            key_char = key[key_index % len(key)]
            key_value = ALPHA.index(key_char)

            result.append(
                ALPHA[(text_index + key_value) % len(ALPHA)]
            )
            key_index += 1
        else:
            result.append(ch)

    return "".join(result)


def decrypt(text, key):
    text = text.upper()
    key = key.upper()
    result = []
    key_index = 0

    for ch in text:
        if ch in ALPHA:
            text_index = ALPHA.index(ch)
            key_char = key[key_index % len(key)]
            key_value = ALPHA.index(key_char)

            result.append(
                ALPHA[(text_index - key_value) % len(ALPHA)]
            )
            key_index += 1
        else:
            result.append(ch)

    return "".join(result)


mode = input("Выберите режим (1 — шифрование, 2 — расшифровка): ")
message = input("Введите текст: ")

if mode == "1":
    print("Шифртекст:", encrypt(message, KEY))
elif mode == "2":
    print("Расшифрованный текст:", decrypt(message, KEY))
else:
    print("Ошибка: выберите 1 или 2.")
