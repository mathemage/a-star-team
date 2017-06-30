from send_invoice import get_negatives, get_positives

positives = get_positives()
negatives = get_negatives()
print(positives)
print(len(positives["positives"]))
print(negatives)
print(len(negatives["negatives"]))