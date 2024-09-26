import sys
from OBR import SegmentationEngine,BrailleClassifier,BrailleImage,BrailleClassifierENG
if len(sys.argv) == 1:
    print("./digestENG.py [PATH TO SCANNED BRAILLE IMAGE(S)]")
    sys.exit(0)

classifier = BrailleClassifierENG()

for path in sys.argv[1:]:
    img = BrailleImage(path)
    for letter in SegmentationEngine(image=img):
        classifier.push(letter)
    print("Digest[{}]: {}\n".format(path, classifier.digest()))
    classifier.clear()



