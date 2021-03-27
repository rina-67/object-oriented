#オブジェクト
"""
クラス(設計図)によって生成されるもの
同じクラスから別々の個性を持ったオブジェクトを生成可能
"""
#今回はオブジェクト を犬として考える
class Dog():
  
  #1.コンストラクタ
  """
  classをインスタンス化するときに、プロパティの値を初期化すること
  インスタンス化した後にプロパティの値を変更する必要がなくなる(lesson1-1.py参照)
  __init__はコンストラクタの定義の方法
  """
  def __init__(self,name,breed,weight):
    #2.プロパティ
    #selfが付くとメンバ変数
    self.name = name
    self.breed = breed
    self.weight = weight
    
    #4.プライベート変数
    """
    class内部のみから使うことが目的
    外部から使わせたくないとき
    """
    self._eaten = False
    
    #プライベートメソッドを記入
    """
    classをインスタンス化するときに実行される
    最初にアンダーバーをつける
    """
    self._output_data()

  
  
  #3.振る舞い＝メソッド
  
  #self
  """
  インスタンスそのもの
  自分自身のオブジェクトを指すキーワード
  """
  
  def sit(self):
    print(self.name, "座る")
    
  def sleep(self):
    print(self.name, "寝る")
  
  def eat(self):
    print(self.name, "食べる")
    #プライベート変数を使う
    self._eaten = True
    
  #5.プライベートメソッド
  def _output_data(self):
    print(f'私は{self.name},{self.breed}で体重は{self.weight}kg')

#インスタンス&初期化
"""
クラスを実体化したもの
"""
dog1 = Dog("kuro","chihuahua",15)

"""
dog2 = Dog()
dog2.name="choco"
dog2.breed="toy poodle"
dog2.weight = 10
"""

print(dog1.name, dog1.breed, dog1.weight)

#メソッドを使う

dog1.sleep()

print(dog1.name)

    