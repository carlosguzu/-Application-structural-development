class Person(object):
    """
    Class used to represent a Person
    """

    def __init__(self, id_person: int = 0, name: str = 'Name', last_name: str = "LastName"):
        """ Person constructor object.

        :param id_person: id of person.
        :type id_person: int
        :param name: name of person.
        :type name: str
        :param last_name: last name of person.
        :type last_name: str
        :returns: Person object
        :rtype: object
        """
        self._id_person = id_person
        self._name = name
        self._last_name = last_name

    @property #hace que el método actue como atributo y se pueda acceder al él sin paréntesis, se pueda definir un setter y deleter.
    def id_person(self) -> int:
        """ Returns id person of the person.
          :returns: id of person.
          :rtype: int
        """
        return self._id_person #atributo privado o protegido de la clase.

    @id_person.setter
    def id_person(self, id_person: int):
        """ The id of the person.
        :param id_person: id of person.
        :type: int
        """
        self._id_person = id_person

    @property
    def name(self) -> str:
        """ Returns the name of the person.
          :returns: name of person.
          :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """ The name of the person.
        :param name: name of person.
        :type: str
        """
        self._name = name

    @property
    def last_name(self) -> str:
        """ Returns the last name of the person.
          :returns: last name of person.
          :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name: str):
        """ The last name of the person.
        : param last_name: last name of person.
        :type: str
        """
        self._last_name = last_name

    def __str__(self):
        """ Returns str of person.
          :returns: sting person
          :rtype: str
        """
        return '({0}, {1}, {2})'.format(self.id_person, self.name, self.last_name)


#se ejecuta solo si el archivo que contiene la definición de la clase Person se ejecuta como el programa principal.
if __name__ == '__main__':

    cliente1 = Person(id_person=65185, name="Carlos", last_name="Zuniga")
    print("Cliente 1: ",cliente1)
    cliente1.last_name = "Guzman" #Accede al atributo name para update it.
    print("Cliente 1: ",cliente1)

    cliente2 = Person() #Objeto vacío
    print(cliente2)
