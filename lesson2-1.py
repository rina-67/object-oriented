#親クラス
class Animal():
  
  def __init__(self,name,weight):
    self.name=name
    self.weight=weight
    
  def sleep(self):
    print(self.name,"寝る")
  def eat(self):
    print(self.name,"食べる")
    
  #オーバーライド
  """
  子クラスで親クラスの宣言を上書きすること
  多様性を実現する方法
    同じメソッドを使い、オブジェクトによって異なる振る舞いをする
  """
  def make_sound(self):
    
    #子クラスでオーバーライドして欲しい場合
    """
    子クラスでオーバーライドされないと、エラーが発生する
    """
    raise NotImplementedError
    
#子クラス
#継承
"""
子クラスを宣言するときに()の中に親クラスを入れると、
親クラスを継承できる
"""
class Dog(Animal):
  """
  コンストラクタ時に親クラスの引数も取得する
  """
  def __init__(self, name,weight,breed):
    """
    super().__init__で親クラスの引数を割り当てる
    super()は親クラスのこと
    """
    super().__init__(name,weight)
    self.breed=breed
    
  
  #オーバーロード
  """
  引数、型などの違いで、同じメソッド名を複数作ること
  多様性の一種
  """
  
  def run(self,speed="usually"):
    if speed =='usually':
      print(self.name,"普通に走る")
    elif speed=='speedy':
      print(self.name,'速く走る')
    elif speed=='lately':
      print(self.name,'遅く走る')
    
  #オーバーライド
  def make_sound(self):
    print(self.name,"wanwan")
    
    
class Bird(Animal):
  def __init__(self,name,weight,types):
    super().__init__(name,weight)
    
    self.types=types
    
  def fly(self):
    print(self.name,"飛ぶ")
    
  def make_sound(self):
    print(self.name,"piiiii")
    
dog1=Dog("choco",10,"chihuahua")

#オーバーロード

#引数指定なし
"""
普通の速さで走るはず
"""
dog1.run()

#引数に'speedy'を指定
"""
速く走るはず
"""
dog1.run('speedy')

dog1.make_sound()


bird1=Bird("pipi",15,"inko")
bird1.fly()
  