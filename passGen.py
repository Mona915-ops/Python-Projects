import random
import string

def gen_pass(length):
    if length < 8 :
        print("Password must contain atleast 8 characters!")
        return None
    char_set = string.ascii_letters + string.digits + string.punctuation
    password = ' '.join(random.choice(char_set) for _ in range(length))
    return password
def main():
    try:
        length = int(input("Enter the desired length of the password:"))
        password = gen_pass(length)

        if password:
            print(f"Generated Password: {password}")
    except ValueError:
        print("Invalid input! ")
if __name__ == "__main__":
    main()
