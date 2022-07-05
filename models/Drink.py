

from select import select


drinks = [
  {"id" : 0, 
  "name" : "Boulevardier", 
  "description" : "Bourbon, campari e vermouth. Variação do clássico negroni.",
  "image" : ""},
  {"id" : 1, 
  "name" : "Old Fashioned", 
  "description" : "Bourbon, pequeno toque de açúcar e bitter angostura.",
  "image" : ""},
  {"id" : 2,
  "name" : "Dry Martini",
  "description" : "Gin e vermouth seco, levemente diluído",
  "image" : ""},
  {"id" : 3,
  "name" : "Negroni",
  "description" : "Gin, campari e vermouth.",
  "image" : ""}
]

class Drink():

  def getMaxID():
    return max(drink["id"] for drink in drinks) +1

  def selectAll():
    return drinks

  def select(id):
    drink = [drink for drink in drinks if drink["id"] == id]
    return drink[0]

  def insert(drink):
    drinks.append(drink)
    return drink

  def update(id, drink):
    drink_db = [drink for drink in drinks if drink["id"] == id]

    if len(drink_db) > 0:
      drink_db[0].update(drink)
      return drink
    
    return None

  def delete(id):
    drink_db = [drink for drink in drinks if drink["id"] == id]

    if len(drink_db) > 0:
      drinks.remove(drink_db)
      return True

    return False