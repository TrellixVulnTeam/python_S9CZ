
clients = 'pablo, ricardo, '


def create_client(client_name):
    global clients             #global permite que la funcion haga manejo de la variable clients

    if client_name not in clients:
        clients += client_name
        _add_comma()
    else:
        print('Client already is in the client\'s list')


def list_clients():
    global clients

    print(clients)


def update_client(client_name, update_client_name):
    global clients

    if client_name in clients:
        clients = clients.replace(client_name + ',', update_client_name + ',')
    else:
        print('Client is nor in clients list')


def _add_comma():
    global clients

    clients +=', '

def _print_welcome():
    print('Welcome to platzi ventas')
    print('*'*50)
    print('What would you like to do today?')
    print('[C]reate client')
    print('[U]pdate client')
    print('[D]elete client')

def _get_client_name():
    return input('What is the client name? ')


if __name__ == '__main__':       #punto de partida (la condicion if para que se ejecute el programa)
    _print_welcome()

    command = input()
    command = command.upper()

    if command == 'C':
        client_name = _get_client_name()
        create_client(client_name)
        list_clients()
    elif command == 'D':
        pass
    elif command == 'U':
        client_name = _get_client_name()
        update_client_name = input('What is de updated client name? ')
        update_client(client_name,update_client_name)
        list_clients()                          #placeolder
    else:
        print('Invalid Command')