import sympy as sp

def ErrProp(func, vars, errors):
    '''
        func: symbolic function
        vars: list of symbolic variables in func
        errors: list of ints or symbols with errors of vars
        
        returns: error formula
    '''
    assert(len(vars) == len(errors))
    err = []
    for v, e in zip(vars, errors):
        err.append(e**2 * func.diff(v)**2)
    return sp.sqrt(sum(err)).simplify()

def ShowErrorProp(func, vars, errors):
    err = ErrProp(func, vars, errors)
    print(func, '±', err)

def Evaluate(func, subs):
    '''
        func: symbolic function (expression)
        subs: dict with symbol key pointing to numerical value. for example
        {vv: 4.99, ri: 1.174, vf: 5, evv: 0.04, eri: 0.026, evf:0}
        
        returns: result of eval
    '''
    return func.subs(subs).evalf()

def ErrAnalisis(func, vars, errors, subs):
    err = ErrProp(func, vars, errors)
    return Evaluate(func, subs), Evaluate(err, subs)

def ShowErrAnalisis(func, vars, errors, subs):
    val, err = ErrAnalisis(func, vars, errors, subs)
    print(val, '±', err)

if __name__ == '__main__':
    vv, ri, vf = sp.symbols('V_V, R_i, V_f')
    evv, eri, evf = sp.symbols('delta_V_V, delta_R_i, delta_V_f')
    rv = vv*(ri/(vf-vv))

    a = ErrProp(rv, [vv, ri, vf], [evv, eri, evf])
    print(a)
    print('evaluate', Evaluate(rv, {vv: 4.99, ri: 1.174, vf: 5, evv: 0.04, eri: 0.026, evf:0}))