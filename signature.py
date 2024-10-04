import cv2

def compare_signatures(signature_path, reference_path):
    signature = cv2.imread(signature_path, cv2.IMREAD_GRAYSCALE)
    reference = cv2.imread(reference_path, cv2.IMREAD_GRAYSCALE)

    signature = cv2.resize(signature, (300, 300))
    reference = cv2.resize(reference, (300, 300))

    score = cv2.matchTemplate(signature, reference, cv2.TM_CCOEFF_NORMED)
    return score[0][0]
