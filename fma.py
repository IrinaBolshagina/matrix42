import decimal
import pyfma

out1 = pyfma.fma(3.0, 2.0, 1.0)  # 3.0*2.0 + 1.0 = 7.0

out2 = decimal.Decimal(3).fma(2,1)
print(out1, out2)