class Planta(object):

 def __init__(self = "", nombre = "", especie = "", temporada = ""):
  self._nombre = nombre
  self._especie = especie
  self._temporada = temporada
  pass

 def __del__(self):
  print("Eliminado")

  #GET 
 def getnombre(self):
  return(self._nombre)
 def getespecie(self):
  return(self._especie)
 def gettemporada(self):
  return(self._temporada)

 def settemporada(self):
  return(self._temporada)

class Jardin(object):
 def __init__(self, lugar = ""):
  self.emplazamiento = lugar
  numplantas = 0
  for i in 100:
   i = None

  def __del__(self):
   for i in numplantas:
   	i = None
   	numplantas = 0

  def jardin(self):
   emplazamiento = j.emplazamiento
   self.numplantas = j.numplantas
   for i in 100:
   	if j.p[i] != None:
   	 p[i] = Planta(j.p[i].getnombre(),j.p[i].getespecie(),j.p[i].gettemporada())
   	else:
   	 p[i] = None


  def Plantar(self, n = "", esp = "", tiempo = ""):
   if numplantas >= 100:
    print("No caben más plantas en el jardín")
   else:
    Planta =[]
    lp =Planta(n,esp)
    lp = settemporada(tiempo)
    for i in 100:
     if p[i] == lp:
      break
     numplantas += 1

   def Arrancar(self,nombre = "", esp = ""):
    if numplantas == 0:
     print("No quedan plantas en el jardín")
    else:
     for i in 100:
      if nombre == p[i].getnombre() and esp == p[i].getespecie():
#INICIO
c=Jardin()
c.jardin()