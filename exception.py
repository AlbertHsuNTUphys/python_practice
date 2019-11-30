def get_password(name, passwdtble):
    if len(name) < 5:
        raise Exception('Illegal Name')
    try:
        return passwdtble[name]
    except Exception as e:
        return 'Name not exist'

if __name__ == "__main__":
    print(get_password('abcde',{'abcde':'password','orzzzz':'666666','whoami':'777777'})) 
    print(get_password('abcdef',{'abcde':'password','orzzzz':'666666','whoami':'777777'})) 
