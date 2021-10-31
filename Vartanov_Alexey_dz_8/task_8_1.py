import re

re_email = re.compile(r'^[^@][a-zA-Z0-9#$%&-]+@[^@.]+\.[^@][a-z]+$')


def email_parse(verified_email):
    res_re = re.match(re_email, verified_email)
    if not res_re:
        msg = f"wrong email: {verified_email}"
        raise ValueError(msg)
    res_list = re.match(re_email, verified_email).group().split('@')
    res_dict = dict(zip(['username', 'domain'], res_list))
    return res_dict


if __name__ == '__main__':
    while True:
        email = input('Введите email:\n')
        try:
            if email_parse(email):
                print(email_parse(email))
        except ValueError as err:
            print(err)
