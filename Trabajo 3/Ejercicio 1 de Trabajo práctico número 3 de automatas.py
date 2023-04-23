import re

def check_email_internet_domain(email):
    string1 = r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$'
    internet_domain = ['gmail.com', 'info.com', 'org.com', 'net.com', 'biz.com']
    countries = ['ar', 'col', 'mex', 'us', 'uk']
    return re.match(string1, email)
    return re.match(internet_domain,email)
    return re.match(countries,email)

print(check_email_internet_domain('juan24@gmail.com.ar'))
