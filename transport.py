class Transport():
   def __init__(self,driver,kms):
      
      self.driver = driver
      self.kms = kms
      
   def __str__(self):
      
      return f'{self.driver}'


class Cab(Transport):
   noofcabs=0
   def __init__(self,driver,kms,place,pay,passengers):
      super().__init__(driver,kms)
      self.place=place
      self.bill = pay
      self.passengers=passengers

   def __str__(self):
      
      return super().__str__()+ f' has travelled {str(self.kms)} kms so far and his '\
             f'current Emirate is {self.place},'\
             f' amount earned: AED {self.bill}. '\
             
         
class Tram(Transport):
   
   
   def __init__(self,driver,kms,place,passengers):
      super().__init__(driver,kms)
      self.place=place
      self.passengers=passengers
      
   def __str__(self):
      return super().__str__()+ f' has travelled {str(self.kms)} kms right now and the ' \
             f'current platform is {self.place}.'\


class RTAbus(Transport):
   
   def __init__(self,driver,kms,place,passengers):
      super().__init__(driver,kms)
      self.place=place
      self.passengers=passengers
      
   def __str__(self):
      return super().__str__()+ f' carried {str(self.passengers)} passengers , travelled {str(self.kms)} km and' \
             f' it is currently at {self.place}.'\


class EXPO(RTAbus):
   
   def __init__(self,driver,kms,place,passengers):
      self.driver=driver
      self.kms=kms
      self.place=place
      self.passengers=passengers
      
   

      
   

