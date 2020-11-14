import hashlib


def main():
    plain_str = "hello james"
    encoded_str = hashlib.sha1(plain_str.encode("utf-8")).hexdigest()
    print(encoded_str)


if __name__ == '__main__':
    main()
