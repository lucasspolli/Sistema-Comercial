class UserMapper:
    def __init__(self, dataMapper):
        self.id = dataMapper[0]
        self.username = dataMapper[1]
        self.email = dataMapper[2]
        self.password = dataMapper[3]

def userMapper(dataMapper):
    return UserMapper(dataMapper) if dataMapper else None