"""
Warning: this is NOT a real OTP generator, it is purely for visual demo purposes!
"""
from PIL import Image
import itertools
import random
import sys

def _make_otp(size):
    otp = Image.new("1", size)
    width, height = size
    otp.putdata(list(itertools.islice(_random_bits(), width * height)))
    return otp


def _random_bits():
    """
    Produces an infinite stream of random choices from [0, 255].
    """
    while True:
        yield random.choice([0, 255])


if __name__ == "__main__":
    input_filename = sys.argv[1]
    in_file = Image.open(input_filename).convert("1")

    otp = _make_otp(in_file.size)
    otp.save(input_filename + "_otp.png")

    applied_data = []
    applied_highlighted_data = []

    for in_bit, pad_bit in itertools.izip(in_file.getdata(), otp.getdata()):
        applied_data.append(255 if pad_bit == in_bit else 0)
        if not in_bit:
            applied_highlighted_data.append((255, 0, 0))
        elif pad_bit:
            applied_highlighted_data.append((255, 255, 255))
        else:
            applied_highlighted_data.append((0, 0, 0))

    applied = Image.new("1", in_file.size)
    applied.putdata(applied_data)
    applied.save(input_filename + "_applied.png")

    applied_highlighted = Image.new("RGB", in_file.size)
    applied_highlighted.putdata(applied_highlighted_data)
    applied_highlighted.save(input_filename + "_applied+highlighted.png")
