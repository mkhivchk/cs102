def get_greeting(name: str) -> str:
    return ('Hello, ' + name + '!')
    pass


if __name__ == "__main__":
    message = get_greeting("World")
    print(message)
