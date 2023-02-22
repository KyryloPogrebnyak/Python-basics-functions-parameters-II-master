### Task 1

settings = {'title': 'Regal is Still Raving', 'pages': []}

def change_site_title(str):
    settings['title'] = str
    return settings

print(settings)
change_site_title("A new fancy title")
print(settings)

### Task 2

default_settings = {'title': 'My original title', 'pages': []}

def get_title(settings = default_settings):
    return settings.get('title')

print('########################################################################')
print(get_title(default_settings))
print(get_title())
change_site_title("A new fancy title")
print(get_title(settings))
print(get_title())

### Task 3: Default and non default arguments combined

def get_pages(settings = default_settings):
    return settings['pages']

def add_page(page, settings=default_settings):
    settings["pages"].append(page)
    return settings

print('########################################################################')
home = {"title": "Home", "page": "/"}
add_page(home)
print(get_pages())
print(get_pages(settings))
about = {"title": "About", "page": "/about/"}
add_page(about, settings)
print(get_pages())
print(get_pages(settings))

### Task 4

def print_user_profile(gender = 'female', first = '', last = 'Doe', pictures = []):
    common_header = "common header.png"
    if gender is 'male' and not first:
        first = 'John'
    elif gender is 'female' and not first:
        first = 'Jane'
    print(f"The user {first} {last} has the following pictures:")
    if not pictures:
        print(common_header)
    elif pictures:
        print(common_header)
    for picture in pictures:
        print(picture)

test_data1 = {
    "gender": "male",
    "last": "Brown",
    "pictures": ["holidays1.png", "easter_grandma.png"]
}
test_data2 = {
    "first": "Alicia",
    "last": "Schmidt"
}
test_data3 = {
    "last": "Korkov",
    "pictures": ["sunset.png"]
}

print('########################################################################')
print_user_profile(**test_data1)
print('########################################################################')
print_user_profile(**test_data2)
print('########################################################################')
print_user_profile(**test_data3)
print('########################################################################')
print_user_profile(**test_data2)

