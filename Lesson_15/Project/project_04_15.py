"""
SUMMARY: Write a program that creates a ten-megabyte data file in two
different ways, and time each method. The first technique should create a
memory-mapped file and write the data by setting one chunk at a time using s
successively higher indexes. The second technique should create an empty binary
file and repeatedly use the write() method to write a chunk of data.
Show how the timings vary with the size of the chunk.

NOTE: mmap_io() create empty file first since otherwise exception is raised
since empty file cannot be created/extended automatically using UNIX version
of mmap module.

NOTE: standart_io() create empty file first in order to reflect mmap_io().
For the same reason both methods are using "r+b" as file mode.
"""

from timeit import Timer
import mmap
import os


def chunks_generator():
    i = 0
    while True:
        yield 2**i
        i += 1


def create_empty_file(fn, fs):
    with open(fn, "wb") as f:
        f.write(b"\0" * fs)


def mmap_io(fn, fs, chunk, last_chunk):
    create_empty_file(fn, fs)
    with open(fn, "r+b") as f:
        m = mmap.mmap(f.fileno(), fs, access=mmap.ACCESS_WRITE)
        if chunk > fs:
            chunk = fs
        data = (chunk - last_chunk) * b'*'
        m[last_chunk:chunk] = data
        m.close()
    os.unlink(fn)


def standart_io(fn, fs, chunk, last_chunk):
    create_empty_file(fn, fs)
    with open(fn, "r+b") as f:
        if chunk > fs:
            chunk = fs
        data = (chunk - last_chunk) * b'*'
        f.write(data)
    os.unlink(fn)

if __name__ == '__main__':
    FN_1 = 'test_io_1.txt'
    FN_2 = 'test_io_2.txt'
    FS = 2**20*10  # 10485760 BYTES == 10 MB
    TRY = 1

    _chunk = 0
    _last_chunk = 0
    chunks = chunks_generator()
    print('-' * 50)
    print("{:>14s}{:>14s}{:>17s}".format('-Chunk size-',
                                         '-mmap I/O-',
                                         '-Regular I/O-'))
    print('-' * 50)
    while True:
        _chunk = next(chunks)
        mmap_io_timer = Timer("mmap_io(FN_1, FS, _chunk, _last_chunk)",
                              "from __main__ import mmap_io, FN_1, FS,"
                              "_chunk, _last_chunk, chunks_generator")
        standart_io_timer = Timer("standart_io(FN_2, FS, _chunk, _last_chunk)",
                                  "from __main__ import standart_io, FN_2, FS,"
                                  "_chunk, _last_chunk, chunks_generator")
        mmap_io_time = mmap_io_timer.timeit(number=TRY)
        standart_io_time = standart_io_timer.timeit(number=TRY)
        if _chunk > FS:
            _chunk = FS - _last_chunk
            print("{:>10d}{:>17f}{:>17f}".format(_chunk,
                                                 mmap_io_time,
                                                 standart_io_time))
            break
        print("{:>10d}{:>17f}{:>17f}".format(_chunk,
                                             mmap_io_time,
                                             standart_io_time))
        _last_chunk = _chunk
    print('-' * 50)
