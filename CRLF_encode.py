import urllib.parse

def url_encode_string(input_string):
    return urllib.parse.quote(input_string)

def main():
    print("Program URL Encoder untuk injeksi CRLF")
    print("===================")

    # Menerima input dari pengguna sebagai string literal
    user_input = input("Masukkan string yang ingin di-encode (gunakan \\r\\n untuk literal CRLF): ")

    # Encode sebagai karakter carriage return dan line feed (CRLF)
    actual_input = user_input.encode().decode('unicode_escape')
    encoded_crlf = url_encode_string(actual_input)
    print(f"Encoded string (karakter CRLF): {encoded_crlf}")

    # Encode string literal dengan escape sequences
    escaped_input = user_input.replace('\\', '%5C').replace('r', '%72').replace('n', '%6E')
    print(f"Encoded string (literal escape sequences): {escaped_input}")

if __name__ == "__main__":
    main()
