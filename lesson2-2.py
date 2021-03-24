#ゲッター、セッター
"""
プロパティの役割
  その属性の値を取得、設定する
  その値を利用する

lesson1-1から2-1では、
プロパティは変数で扱っていた(取得、設定可能)
この作業を関数で実現
"""


class Dog():
  def __init__(self,name):
    #プライベート変数で宣言
    self._name = name

  #ゲッター
  """
  プロパティをを取得する関数
  """
  @property
  def name(self):
    return self._name
    
  #セッター
  """
  プロパティを設定する関数
  """
  @name.setter
  def name(self,value):
    self._name=value
    
    
dog1=Dog('Leo')

#セッターがコードにない場合エラーが出る
"""
ゲッターによって読み込みのみに制限されているため
"""
dog1.name='Choco'


print(dog1.name)