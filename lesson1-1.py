
#オブジェクト
"""
クラス(設計図)によって生成されるもの
同じクラスから別々の個性を持ったオブジェクトを生成可能
"""
#今回はオブジェクト を犬として考える
class Dog():
  
  #属性＝プロパティ
  
  name=""
  breed=""
  weight=0
  
  
  #振る舞い＝メソッド
  
  #self
  """
  インスタンスそのもの
  """
  
  def sit(self):
    print(self.name, "座る")
    
  def sleep(self):
    print(self.name, "寝る")
  
  def eat(self):
    print(self.name, "食べる")


#インスタンス
"""
クラスを実体化したもの
"""
dog1 = Dog()

#プロパティの値を変更
dog1.name="kuro"
dog1.breed="chihuahua"
dog1.weight=15

dog2 = Dog()
dog2.name="choco"
dog2.breed="toy poodle"
dog2.weight = 10

print(dog1.name, dog1.breed, dog1.weight)

#メソッドを使う

dog1.sleep()
dog2.sit()

print(dog1.name)

    