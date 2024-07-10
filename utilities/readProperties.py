import configparser


config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

# We create a static method in which we can access these method without having to create an instance of those class

class ReadConfig():
    @staticmethod
    def getApplicationUrl():
        url= config.get('common info','baseURL')
        return url

    @staticmethod
    def getUserEmail():
        username = config.get('common info','username')
        return username

    @staticmethod
    def getUserPassword():
        password = config.get('common info', 'password')
        return password
