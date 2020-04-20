class Animals:
  
  animal_count = 0
  weight_count = 0
  max_weight = {}


  def __init__(self, name, weight):
    self.name = name
    self.weight = weight
    Animals.animal_count += 1
    Animals.weight_count += weight
    Animals.max_weight[self.name] = self.weight


  # def max_weight_animals(self, max_weight):
  #   self.max_weight = {name: weight}
    

    


class Goose(Animals):   #Гуси

  def egg(self):
    return ('несет яйца')

  def feed(self):
    return (self.name + ' это животное нужно покормить')
  
  def vote(self):
    return (self.name + ' гогочет га-га-га')

  

class Cow(Animals):   #Корова

  def milk(self):
    return ('Корова дает молоко')
  
  def feed(self):
    return (self.name + ' это животное нужно покормить')
  
  def vote(self):
    return (self.name + ' мычит муу')
    



class Sheep(Animals):   #Овцы

  def cut(self):
    return ('Овцы дают шерсть')

  def feed(self):
    return (self.name + ' это животное нужно покормить')
  
  def vote(self):
    return (self.name + ' блеет') 



class Chicken(Animals):   #Курочки

  def egg(self):
    return ('Курочка несет яйца')

  def feed(self):
    return (self.name + ' это животное нужно покормить')
  
  def vote(self):
    return (self.name + ' кричит ко-ко-ко')
  


class Goat(Animals):   #Коза

  def milk(self):
    return ('Коза дает молоко')
  
  def feed(self):
    return (self.name + ' это животное нужно покормить')
  
  def vote(self):
    return (self.name + ' блеет')



class Duck(Animals): #Утка

  def egg(self):
    return ('Утка несет яйца')

  def feed(self):
    return (self.name + ' это животное нужно покормить')
  
  def vote(self):
    return (self.name + ' крякает кря-кря')


my_goose1 = Goose('Гусь Серый', 3.67)

my_goose2 = Goose('Гусь Белый', 3.84)

my_cow = Cow('Корова Манька', 284)  

my_sheep1 = Sheep('Овца Барашек', 92)

my_sheep2 = Sheep('Овца Кудрявый', 81)

my_chicken1 = Chicken('Курочка Ко-Ко', 3.14)

my_chicken2 = Chicken('Курочка Кукареку', 2.81)

my_goat1 = Goat('Коза Рога', 41)

my_goat2 = Goat('Коза Копыта', 46)

my_duck = Duck('Кряква', 4.76)


# max_weight_animals = (Animals.max_weight)
# print(max_weight_animals)


# print(f'Общее количество животных: 

max_weight_animals = max(Animals.max_weight.items())



print('Всего животных:', Animals.animal_count)
print('Общий вес всех животных:', Animals.weight_count)
# print('Вес самого тяжелого животного:', Animals.max_weight)

print(f'Название животного с максимальным весом: {max_weight_animals[0]}')
