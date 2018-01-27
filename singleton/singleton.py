class Singleton(object):
    """
    Simple Singleton class
    """
    def __new__(cls):
        #Check if instance has initialized
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


class LazySingleton:
    """
    Simple Singleton Lazy class
    """
    __instance = None
    def __init__(self):
        if not LazySingleton.__instance:
            print("__init__ method called")
        else:
            print("Instance already Created:", self.getInstance())

    @classmethod
    def getInstance(cls):
        """
        Create a Object Instance
        :return: The object instance =)
        """
        if not cls.__instance:
            cls.__instance = LazySingleton()
        return cls.__instance