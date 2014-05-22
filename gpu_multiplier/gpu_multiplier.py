__author__ = 'Sherlock'
import pyopencl as cl
import numpy


class GPUMultiplier:
    def __init__(self):
        self.context = cl.create_some_context()
        self.queue = cl.CommandQueue(self.context)
        self.program = None

        self.a, self.b = \
            numpy.array(range(10), dtype=numpy.float32),\
            numpy.array(range(10), dtype=numpy.float32)

        mf = cl.mem_flags
        self.a_buf, self.b_buf, self.res_buf = \
            cl.Buffer(self.context, mf.READ_ONLY | mf.COPY_HOST_PTR, host_buf=self.a),\
            cl.Buffer(self.context, mf.READ_ONLY | mf.COPY_HOST_PTR, host_buf=self.b),\
            cl.Buffer(self.context, mf.WRITE_ONLY, self.b.nbytes)

    def load_program(self, filename):
        f = open(filename, 'r')
        f_str = "".join(f.readlines())
        self.program = cl.Program(self.context, f_str).build()

    def multiply(self):
        self.program.multiply(self.queue, self.a.shape, None, self.a_)