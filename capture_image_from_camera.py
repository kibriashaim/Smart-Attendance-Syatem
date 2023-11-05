import cv2

cam_port = 0  # Change the camera port as needed
cam = cv2.VideoCapture(cam_port)

if not cam.isOpened():
    print("Cannot open camera")
    exit()

inp = input('Enter person name: ')

while True:
    ret, frame = cam.read()

    if not ret:
        print("Failed to capture image")
        break

    cv2.imshow(inp, frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord('s'):  # Press 's' to save the image
        cv2.imwrite(inp + ".png", frame)
        print("Image saved as " + inp + ".png")
        break
    elif key == 27:  # Press 'Esc' key to exit
        break

cam.release()
cv2.destroyAllWindows()
