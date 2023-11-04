import re


# region bailam
def get_name_in_email(email_list):
    regex = r"([\w-]+\.)*[\w-]+@[\w-]+\.[\w-]+"
    arr = []
    if not email_list:
        return arr
    else:
        for email in email_list:
            if email is None:
                arr.append("ERROR invaid email")
            elif not re.match(regex, email):
                arr.append("ERROR invaid email")

            # Tách tên tài khoản và miền email
            else:
                name, domain = email.split("@")
                arr.append(name)
        return arr


if __name__ == '__main__':
    pass