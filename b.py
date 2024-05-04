from imageai.Detection import ObjectDetection
restaurant=["bottle","cup","fork","knife","spoon","bowl","hot_dog","pizza","donut","cake","chair","diningtable","person"]
yol=["bicycle","car","motorbike","bus","traffic_light","stop_sign","parking_meter","person"]
ev=["chair","sofa","pottedplant","toilet","tvmonitor","laptop","mouse","remote","keyboard","cell_phone","microwawe","oven","toaster","sink","refrigerator","book","clock","vase","scissors","teddy_bear","hair_drier","tootbrush","person"]
manav=["banana","apple","orange","broccoli","carrot","person"]
havalanı=["aeroplane","person"]
magaza=["backpack","umbrella","handbag","tie","suitcase","frisbee","skis","snowboard","sports_ball","kite","baseball_bat","baseball_glove","skateboard","surfboard","tennis_racket","bottle","person"]
deniz=["boat","person"]
itfaye=["fire_hydrant","truck","person"]
hayvanat_bahcesi=["bench","bird","cat","dog","horse","sheep","cow","elephant","bear","zebra","giraffe","person"]
istasyon=["train","person"]

def f_n(f):
    detector = ObjectDetection()
    model_path = "yolov3.pt"
    detector.setModelTypeAsYOLOv3()
    detector.setModelPath(model_path)
    detector.loadModel()
    detections = detector.detectObjectsFromImage(
        input_image=f,
        output_image_path="output_image.jpg",
        minimum_percentage_probability=30)
    return detections

def t_f(f):
  res=0
  ev2=0
  man=0
  hava=0
  mag=0
  den=0
  itfa=0
  h_b=0
  ist=0
  y=0
  d={}
  detector = ObjectDetection()
  model_path = "yolov3.pt"
  detector.setModelTypeAsYOLOv3()
  detector.setModelPath(model_path)
  detector.loadModel()
  detections = detector.detectObjectsFromImage(
  input_image=f,
  output_image_path="output_image.jpg",
  minimum_percentage_probability=30)
  for i in detections:
    if i["name"] not in d:
      d[i["name"]]=1
    else:
      d[i["name"]]+=1

  for i,j in d.items():   
    print(f"{j} tane {i} vardır.")
    if i in restaurant:
       res+=j
    if i in ev:
       ev2+=j
    if i in itfaye:
       itfa+=j
    if i in manav:
       man+=j
    if i in yol:
       y+=j
    if i in magaza:
       mag+=j
    if i in istasyon:
       ist+=j
    if i in havalanı:
       hava+=j
    if i in hayvanat_bahcesi:
       h_b+=j
    if i in deniz:
       den+=j

    e_b= max(res,y,itfa,man,mag,ev2,hava,ist,h_b,den)
    if e_b==res:
       return "restaurant"
    elif e_b==y:
       return "yol"
    elif e_b==den:
       return "deniz"
    elif e_b==man:
       return "manav"
    elif e_b==mag:
       return "mağaza"
    elif e_b==itfa:
       return "itfaiye"
    elif e_b==h_b:
       return "hayvanat bahçesi"
    elif e_b==ist:
       return "istasyon"
    elif e_b==ev2:
       return "ev"
    elif e_b==hava:
       return "havaalanı"



if __name__=="__main__":
    print(t_f("fnewsgcv.png"))