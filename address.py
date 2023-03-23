from deliver import Deliver

class Address(Deliver):
  """
  Class used to represent a Address
  """
  def __init__(self, date: str = "99/99/9999", time: str = "23:59", sender: str = "Person", recive: str = "Person", sender_add: str = "Address", recive_add: str = "Address", contac: str = "+999999999999", items: str = "Package", neighborhood: str = "Neighborhood", street: str = "Street", city: str = "City", avenue: str = "Avenue", postal_code: str = "999999"):
    """ Address constructor Deliver.
    
    :param neighborhood: neighborhood of Address.
    :type neighborhood: str
    :param street: street of Address.
    :type street: str
    :param city: city of Address.
    :type city: str
    :param avenue: avenue of Address.
    :type avenue: str
    :param postal_code: postal_code of Address.
    :type postal_code: str
    :returns: address object.
    :rtype: object
    """
    
    super().__init__(date, time, sender, recive, sender_add, recive_add, contac, items)
    self._neighborhood = neighborhood
    self._street = street
    self._city = city
    self._avenue = avenue
    self._postal_code = postal_code
  
  @property
  def neighborhood(self) -> str:
   """ Returns neighborhood of the address.
    :returns: neighborhood of address.
    :type: str
   """
   return self._neighborhood
  
  @neighborhood.setter
  def neighborhood(self, neighborhood: str):
    """ The neighborhood of the Address.
    :param neighborhood: neighborhood of Address.
    :type: str
    """
    self._neighborhood = neighborhood

  @property
  def street(self) -> str:
   """ Returns street of the address.
    :returns: street of address.
    :type: str
   """
   return self._street
  
  @street.setter
  def street(self, street: str):
    """ The street of the Address.
    :param street: street of Address.
    :type: str
    """
    self._street = street

  @property
  def city(self) -> str:
   """ Returns city of the address.
    :returns: city of address.
    :type: str
   """
   return self._city
  
  @city.setter
  def city(self, city: str):
    """ The city of the Address.
    :param city: city of Address.
    :type: str
    """
    self._city = city

  @property
  def avenue(self) -> str:
   """ Returns avenue of the address.
    :returns: avenue of address.
    :type: str
   """
   return self._avenue
  
  @avenue.setter
  def avenue(self, avenue: str):
    """ The avenue of the Address.
    :param avenue: avenue of Address.
    :type: str
    """
    self._avenue = avenue

  @property
  def postal_code(self) -> str:
   """ Returns postal_code of the address.
    :returns: postal_code of address.
    :type: str
   """
   return self._postal_code
  
  @postal_code.setter
  def postal_code(self, postal_code: str):
    """ The postal_code of the Address.
    :param postal_code: postal_code of Address.
    :type: str
    """
    self._postal_code = postal_code
    
  
  def __str__(self):
    """ Returns str of address.
    :returns: sting of address
    :rtype: str
    """
    return '({0}, {1}, {2}, {3}, {4}'.format(self._neighborhood, self._street, self._city,self._avenue, self._postal_code)
  
#se ejecuta solo si el archivo que contiene la definición de la clase Person se ejecuta como el programa principal.
if __name__ == '__main__':

    address = Address(neighborhood = "Los Calamares", street = "65", city = "Cartagena", avenue = "Av. 3", postal_code = "130010")
    print("Address 1: ", address)

    address = Address() #Objeto vacío
    print("Address 2: ", address)
