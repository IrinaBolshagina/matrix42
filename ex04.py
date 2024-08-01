from vector import Vector
from vector import norm_1, norm, norm_inf


if __name__ == '__main__':

    print("\nTypes of norms for vectors: \n")
    
    v1 = Vector([0,0,0])
    print("for vector = ")
    print(v1)
    print(f"norm_1 = {norm_1(v1)}, norm = {norm(v1)}, norm_inf = {norm_inf(v1)}\n") # 0, 0.0, 0

    v2 = Vector([1,2,3])   
    print("for vector = ")
    print(v2)
    print(f"norm_1 = {norm_1(v2)}, norm = {norm(v2)}, norm_inf = {norm_inf(v2)}\n") # 6, 3.74165738, 3

    v3 = Vector([-1,-2])
    print("for vector = ")
    print(v3)
    print(f"norm_1 = {norm_1(v3)}, norm = {norm(v3)}, norm_inf = {norm_inf(v3)}\n") # 3, 2.236067977, 2
    
    v4 = Vector([1,1,1,1,1,1,1,1,1,1])
    print("for vector = ")
    print(v4)
    print(f"norm_1 = {norm_1(v4)}, norm = {norm(v4)}, norm_inf = {norm_inf(v4)}\n") # 10, 3.162277660, 1

    print("------------- bonus -------------\n")
    v5 = Vector([1.0 + 2.2j, 2.0 + 3.9j, 3.0 + 4.0j])
    print("for vector of complex numbers ")
    print(v5)
    print(f"norm_1 = {norm_1(v5)}, norm = {norm(v5)}, norm_inf = {norm_inf(v5)}\n") # 10.1, 6.0, 3.0