class Deliver(object):      
  """
  Class used to represent a deliver
  """
  
  W_GR_100 = 1.0

  def __init__(self, date: str = "99/99/9999", time: str = "23:59", sender: str = "Person", recive: str = "Person", sender_add: str = "Address", recive_add: str = "Address", contac: str = "+999999999999", items: str = "Package"):
    """ Deliver constructor object.

    :param date: date of Deliver.
    :type date: str
    
    :param time: time of Deliver.
    :type time: str
    
    :param sender: sender of Deliver.
    :type sender: str

    :param recive: recive of Deliver.
    :type recive: str

    :param sender_add: sender_add of Deliver.
    :type sender_add: str

    :param recive_add: recive_add of Deliver.
    :type recive_add: str

    :param contac: contac of Deliver.
    :type contac: str
    
    :param items: items of Deliver.
    :type items: Deliver
    
    :returns: Deliver object.
    :rtype: object
    """
    self._date = date 
    self._time = time
    self._sender = sender
    self._recive = recive
    self._sender_add = sender_add
    self._recive_add = recive_add
    self._contac = contac
    self._items = items

  @property
  def date(self) -> str:
   """ Returns date of the delivery.
    :returns: date of delivery.
    :type: str
   """
   return self._date
  
  @date.setter
  def date(self, date: str):
    """ The date of the Deliver.
    :param date: date of Deliver.
    :type: str
    """
    self._date = date

  @property
  def time(self) -> str:
   """ Returns time of the delivery.
    :returns: time of delivery.
    :type: str
   """
   return self._time
    
  @time.setter
  def time(self, time: str):
    """ The time of the Deliver.
    :param time: time of Deliver.
    :type: str
    """
    self._time = time

  @property
  def sender(self) -> str:
   """ Returns sender of the delivery.
    :returns: sender of delivery.
    :type: str
   """
   return self._sender

  @sender.setter
  def sender(self, sender: str):
    """ The sender of the Deliver.
    :param sender: sender of Deliver.
    :type: str
    """
    self._sender = sender

  @property
  def recive(self) -> str:
   """ Returns recive of the delivery.
    :returns: recive of delivery.
    :type: str
   """
   return self._recive

  @recive.setter
  def recive(self, recive: str):
    """ The recive of the Deliver.
    :param recive: recive of Deliver.
    :type: str
    """
    self._recive = recive

  @property
  def sender_add(self) -> str:
   """ Returns sender_add of the delivery.
    :returns: sender_add of delivery.
    :type: str
   """
   return self._sender_add

  @sender_add.setter
  def sender_add(self, sender_add: str):
    """ The sender_add of the Deliver.
    :param sender_add: sender_add of Deliver.
    :type: sender_add
    """
    self._sender_add = sender_add

  @property
  def recive_add(self) -> str:
   """ Returns recive_add of the delivery.
    :returns:  recive_add of delivery.
    :type: str
   """
   return self._recive_add

  @recive_add.setter
  def recive_add(self, recive_add: str):
    """ The recive_add of the Deliver.
    :param recive_add: recive_add of Deliver.
    :type: str
    """
    self._recive_add = recive_add

  @property
  def contac(self) -> str:
   """ Returns contac of the delivery.
    :returns: contac of delivery.
    :type: str
   """
   return self._contac

  @contac.setter
  def contac(self, contac: str):
    """ The contac of the Deliver.
    :param contac: contac of Deliver.
    :type: str
    """
    self._contac = contac

  @property
  def items(self) -> str:
    """ Returns items of the delivery.
    :returns: items of delivery.
    :type: str
   """
    return self._items

  @items.setter
  def items(self, items: str):
    """ The items of the Deliver.
    :param items: items of Deliver.
    :type: str
    """
    self._items = items


  def __str__(self):   
    """
    Returns str of Deliver.
    :returns: sting Deliver
    :rtype: str
    """
    return '({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7})'.format(self._date, self._time, self._sender, self._recive, self._sender_add, self._recive_add, self._contac, self._items)

#se ejecuta solo si el archivo que contiene la definición de la clase Person se ejecuta como el programa principal.
if __name__ == '__main__':

    deliver1 = Deliver(date = "1/5/23", time = "20:58", sender = "Mario Zuniga", recive = "Carlos Guzman", sender_add = "Bogotá, Calle 38", recive_add = "Cartagena Crra 104", contac = +573046356749, items = "Airpods")
    print("Deliver 1: ",deliver1)

    deliver2 = Deliver() #Objeto vacío
    print("Deliver 2 ",deliver2)
