class Human():
  def __init__(self,name):
    self.name=name
    
  
class Patient(Human):
  def __init__(self,name,patient_id,symptom):
    super().__init__(name)
    self.symptom=symptom
    self.patient_id=patient_id
    
    
class Clinic():
  def __init__(self):
    
    '''
    patient_listは引数には指定しない
    '''
    self.patient_list=[]
  
  #診察待ち人数を表示
  def show_waiting_count(self):
    print(len(self.patient_list))
  
  #患者の予約処理
  def reserve(self,patient):
    if self._check_reserved(patient):
      print(f"{patient.name}様は既に予約済みです")
    else:
      self.patient_list.append(patient)
      """
      patientは一応オブジェクト
      リストじゃない
      """
      print(f"{patient.name}様、予約完了しました")
      
      
  
  #患者の診察処理
  def diagnosis(self,patient_id=None):
    
    #患者指定なしの場合、順番に
    patient =None
    if patient_id == None:
      #patient_listがからではない(診察患者がいる)場合
      if len(self.patient_list)>0:
        patient = self.patient_list[0]
    #患者指定ありの場合、
    #引数のidと一致するものをpatient_listから探す
    else:
      for p in self.patient_list:
        """
        オブジェクト名.idでそのオブジェクトのidをゲット
        
        pはPatientクラスから生成されたオブジェクトを収納したリストのうちの要素のひとつ
        つまり、pはオブジェクト
        
        この場合、patientには、diagnosis()の引数に指定されたidと一致するpatientオブジェクトが代入される
        """
        if p.patient_id == patient_id:
          patient=p
    
    #診察する患者がいない場合のコメント
    if patient == None:
      print('診察する患者がいません')
    #診察する患者がいた場合
    else:
      print(f"{patient.name}さん、{patient.symptom}ですね")
      print("診察終わりました。お大事に。")
      
      #patient_listからこの患者を除外
      self.patient_list.remove(patient)
    
    
    
    
  
  #患者の予約が既にされているか確認
  """
  このpatientはオブジェクト
  """
  def _check_reserved(self,patient):
    for p in self.patient_list:
      #idが一致するものがあるか確認
      if p.patient_id == patient.patient_id:
        #予約済み
        return True
    #予約されていない場合
    """
    for文の中にreturn Falseを入れない
    インデントに注意
    """
    return False
    
    

myclinic=Clinic()

#患者予約対象データ
#name, patient_id, symptomの順
patients = [['Sato','101','cough'],
['Tanaka','102','stomach_ache'],
['Suzuki','103','runny_nose'],
['Yamada','104','headache'],
['Takahashi','105','tiredness'],]

"""
for i in listみたいな感覚
"""
for p in patients:
  name, patient_id, symptom=p
  
  #loopで取得するname,age,symptomでPatientをインスタンス化
  patient=Patient(name,patient_id,symptom)
  
  #myclinicに予約
  myclinic.reserve(patient)

#現在の待ち人数
myclinic.show_waiting_count()

#重複した患者を予約する
mee = Patient('Takahashi','105','tiredness')
#予約する
myclinic.reserve(mee)

#現在の待ち人数
myclinic.show_waiting_count()

#診察
myclinic.diagnosis()
#現在の待ち人数
myclinic.show_waiting_count()

#急患の診察
myclinic.diagnosis('105')
myclinic.show_waiting_count()

  
"""
課題
重複の患者を入れようとしても、予約済みですって表示されずに新しい患者として追加されてしまう
patient_idは同じなのに、、
"""
    
