from package import Package

class OverWeigthPackage(Package):
  """
  Class used to represent a Package
  """

  def __init__(self, id_package: int = 0, weight: float = 0.1 , description: str = "DescriptionOfProduct" , cost: float = 1.0, over_weigth: float = 0.1):
    """ OverWeigthPackage constructor object.

    :param over_weigth: over_weigth of OverWeigthPackage Package.
    :type over_weigth: float
    :returns: OverWeigthPackage Package.
    :rtype: Package
    """
    
    def calculate(self):
      
      print(f"The shipping cost by adding the fixed fee at the cost based on the weight of the package is  ${(self._over_weigth + self._weight ) * self._cost}")

    super().__init__(id_package, weight, description, cost)
    self.over_weigth = over_weigth

    @property
    def over_weigth(self) -> float:
     """ Returns over_weigth of the overweightpackage.
      :returns: over_weigth of overweightpackage.
      :type: str
     """
     return self._over_weigth
    
    @over_weigth.setter
    def over_weigth(self, over_weigth: float):
        """ The over_weigth of the OverWeigthPackage package.
        :param over_weigth: over_weigth of OverWeigthPackage package.
        :type: float
        """
        self._over_weigth = over_weigth

    def __str__(self):
      """ Returns str of package.
      :returns: sting package
      :rtype: str
      """
      return '({0}'.format(self._over_weigth)