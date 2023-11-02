records = {}

def user_error(func):
    def inner(*args):
        try:
            return func(*args)
        except IndexError:
            return 'Not enough params ! Use help.'
        except  KeyError:
            return 'Unknown name ! Try another.'
    return inner

@user_error
def add_record(*args):
    name = args[0]
    number = args[1]
    records[name] = number
    return f'Add record {name = }, {number = }'

@user_error
def change_record(*args):
    name = args[0]
    new_number = args[1]
    rec = records[name]
    if rec:
        records[name] = new_number
        return f'Changed record {name = }, {new_number = }'

@user_error
def show_phone(name):
    return records[name]

def show_all():
    return records

def unknown(*args):
    return 'Unknown command ! Try again.'

COMMANDS = {add_record: 'add', change_record: 'change', show_phone: 'phone', show_all: 'show all'}

def parser(text: str) -> tuple:
    for func, kw in COMMANDS.items():
        if text.startswith(kw):
            return func, text[len(kw):].strip().split()
    return unknown, []

def main():
    while True:
        user_input = input('>>>')
        if user_input.lower() == 'hello':
            print('How can I help You ?')
            continue
        if user_input.lower() in ['exit', 'close', 'good bye']:
            print('Good bye !')
            break
        func, data = parser(user_input.lower())
        print (func(*data))
        


if __name__ == '__main__':
    main()