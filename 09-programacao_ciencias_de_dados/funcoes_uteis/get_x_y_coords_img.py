'''
Apresenta no terminal coordenadas x e y de uma imagem a partir de clique do cursor: permite vários cliques.
Fonte: https://www.geeksforgeeks.org/displaying-the-coordinates-of-the-points-clicked-on-the-image-using-python-opencv/
'''

import cv2

def click_event(event, x, y, flags, params): 
  
    
    if event == cv2.EVENT_LBUTTONDOWN: 
      print(x, ' ', y) 
      font = cv2.FONT_HERSHEY_SIMPLEX 
      cv2.putText(img, str(x) + ',' +
                    str(y), (x,y), font, 
                    1, (255, 0, 0), 2) 
      cv2.imshow('image', img) 
  
    
    if event==cv2.EVENT_RBUTTONDOWN: 
      print(x, ' ', y) 
      font = cv2.FONT_HERSHEY_SIMPLEX 
      b = img[y, x, 0] 
      g = img[y, x, 1] 
      r = img[y, x, 2] 
      cv2.putText(img, str(b) + ',' +
                  str(g) + ',' + str(r), 
                  (x,y), font, 1, 
                  (255, 255, 0), 2) 
      cv2.imshow('image', img) 
      
if __name__=="__main__": 
  
    #alterar conforme imagem desejada
    img = cv2.imread('mapa_brasil_regioes.jpeg', 1) 
    #padronizando tamanho da figura a ser aberta
    img = cv2.resize(img, (600,600))
    cv2.imshow('image', img)     
    cv2.setMouseCallback('image', click_event) 
    cv2.waitKey(0) 
    cv2.destroyAllWindows() 