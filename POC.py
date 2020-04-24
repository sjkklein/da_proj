import aifc
import sys

rec = aifc.open(sys.argv[1])
rate = rec.getframerate()
width = rec.getsamplewidth()
n_samples = rec.getnframes()

print('rate:', rate)
print('width:', width)
print('n_samples:', n_samples)

samples = rec.readframes(n_samples)

print('first sample:', samples[0])
