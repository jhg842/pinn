from sympy import Symbol, Function, Number
import torch
from physicsnemo.sym.eq.pde import PDE

class WaveEquation1D(PDE):
    name = 'WaveEquation1D'
        
    def __init__(self, c=1.0):
        super().__init__()
        
        x = Symbol("x")
        t = Symbol("t")
        u = Function("u")(x, t)
        
        if isinstance(c, str):
            c = Function('c')(x, t)
        elif isinstance(c, (float, int)):
            c = Number(c)
        
        # 부모 클래스의 기대 속성명 맞추기
        self.equations = {
            'wave_equation': u.diff(t, 2) - (c**2 * u.diff(x)).diff(x)
        }
        

        