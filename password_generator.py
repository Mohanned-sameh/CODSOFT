import random
import string


def gen_pass(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(chars) for _ in range(length))
    return password


def main():
    try:
        length = int(input("Enter the length of the password: "))
        if length < 1:
            raise ValueError
        else:
            password = gen_pass(length)
            print(password)
    except ValueError:
        print("Invalid input. Please use a digit that isgreater than 0")


if __name__ == "__main__":
    main()
