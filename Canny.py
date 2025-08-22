import cv2

# Leer la imagen 'cartas.jpg' en escala de grises
img = cv2.imread('cartas.jpg', 0)
bordeCanny = cv2.Canny(img, 100, 200)

# Mostrar la imagen original
cv2.imshow('Oringinal', img)

# Mostrar la imagen con bordes detectados
cv2.imshow('blur', bordeCanny)

cv2.waitKey(0)
cv2.destroyAllWindows()
