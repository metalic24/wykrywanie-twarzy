
import cv2
import face_recognition



def camera():
    cap = cv2.VideoCapture(0)
    #jesli nie uda się otworzyć kamerki, to wypisze błąd
    if not cap.isOpened():
        print("Cannot open camera")
        exit()

    #wczytywanie obrazu z kamerki
    while True:
        #wczytanie obrazu
        ret, frame = cap.read()
        rgb_frame = frame[:, :, ::-1]

        #znalezienie twarzy na obrazie
        face_locations = face_recognition.face_locations(rgb_frame)
        #jesli nie uda się przechwycić obrazu, to wyświetla informację
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        #wczytanie twarzy myszki miki
        img = cv2.imread("myszka.png",-1)
        #zamiana bgr na rgba (z kanałem alfra)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGBA)
        #dla każdego rogu w lokacjach twarzy
        for top, right, bottom, left in face_locations:

            a=(right-left)
            b=(bottom-top)
            #zmiana wielkości obrazu na wielkość twarzy
            img =  cv2.resize(img, (a, b))

            #zamiana kanału alfa na obraz
            alpha_img = img[:, :, 3] / 255.0
            alpha_frame = 1.0 - alpha_img
            for c in range(0, 3):
                frame[top:bottom, left:right, c] = (alpha_img * img[:, :, c] +
                                                    alpha_frame * frame[top:bottom, left:right, c])

        cv2.imshow('Video', frame)


        # 'q' zamyka kamerę
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()
    cap.release()


def zdjecie(path):

    #wczytanie zdjęcia
    image = cv2.imread(path)
    #znalezienie twarzy na zdjęciu
    face_locations = face_recognition.face_locations(image)
    #wczytanie twarzy myszi miki
    img = cv2.imread("myszka.png",-1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGBA)

    #podmiana każdej twarzy na zdjęciu
    for top, right, bottom, left in face_locations:
        #zmiana rozmiarów nakładanego obrazu
        a = (right - left)
        b = (bottom - top)
        img = cv2.resize(img, (a, b))

        #usunięcie kanału alfa
        alpha_img = img[:, :, 3] / 255.0
        alpha_image = 1.0 - alpha_img

        for c in range(0, 3):
                    image[top:bottom, left:right, c] = (alpha_img * img[:, :, c] +
                                                   alpha_image * image[top:bottom, left:right, c])


    return image





