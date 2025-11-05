from math import isclose
from calculator import Calculator
from pytest import raises


def is_almost_equal(a, b):
    return isclose(a, b, rel_tol=1e-9, abs_tol=0.0)

def test_adunare_simpla():
    assert is_almost_equal(Calculator.adunare(29, 5), 34)

def test_adunare_complexa():
    assert is_almost_equal(Calculator.adunare(-13, 4), -9)

def test_scadere_simpla():
    assert is_almost_equal(Calculator.scadere(15, 9), 6)

def test_scadere_complexa():
    assert is_almost_equal(Calculator.scadere(-20, -100), 80)

def test_inmultire_simpla():
    assert is_almost_equal(Calculator.inmultire(5, 7), 35)

def test_inmultire_complexa():
    assert is_almost_equal(Calculator.inmultire(-4.5, 3.7), -16.65)

def test_impartire_simpla():
    assert is_almost_equal(Calculator.impartire(20, 4), 5)

def test_impartire_cu_virgula():
    assert is_almost_equal(Calculator.impartire(-100, 125), -0.8)

def test_impartire_la_zero():
    with raises(ZeroDivisionError):
        Calculator.impartire(10, 0)
