__kernel void multiply(__global float* a, __global float* b, __global float* c)
{
    unsigned int i = get_global_id(0);

    c[i] = a[i] + b[i];
}
