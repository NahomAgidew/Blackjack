class Player:

  def __init__(self, name: str):
    self.hand = []
    self.name = name
  
  def __str__(self):
    return self.name