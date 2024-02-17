import simd
from simd import A

# shape for testing:
s = (4, 4, 5)  # 4 bits for padding, 4 bits for values, 5 items

a = A(0x_05_04_03_02_01, *s)
b = A(0x_02_04_02_04_02, *s)

def test_str() -> None:
    assert str(a) == '[0000_0001, 0000_0010, 0000_0011, 0000_0100, 0000_0101]'
    assert str(b) == '[0000_0010, 0000_0100, 0000_0010, 0000_0100, 0000_0010]'

def test_repr() -> None:
    assert repr(a) == 'A(0x0504030201, *(4, 4, 5))'
    assert repr(b) == 'A(0x0204020402, *(4, 4, 5))'

# fmt: off

def test_eq() -> None:
    assert (
        A(0x_02_04_02_04_02, *s) ==
        A(0x_02_04_02_04_02, *s)
    )
    assert (
        A(0x_02_04_02_04_02, *s) !=
        A(0x_02_04_02_04_03, *s)
    )
    assert (
        A(0x_02_04_02_04_02, *s) !=
        A(0x_02_04_02_04_02, *(3, 4, 5))
    )

def test_sub() -> None:
    assert (
        A(0x_05_04_03_02_01, *s) -
        A(0x_02_04_02_04_02, *s) ==
        A(0x_03_00_01_0e_0f, *s)
    )
    assert (
        A(0x_05_04_03_02_01, *s) -
        3 ==
        A(0x_02_01_00_0f_0e, *s)
    )


def test_mul() -> None:
    assert (
        A(0x_05_04_03_02_01, *s) *
        4 ==
        A(0x_04_00_0c_08_04, *s)
    )
    assert (
        A(0x_05_04_03_02_01, *s) *
        A(0x_04_02_04_02_04, *s) ==
        A(0x_04_08_0c_04_04, *s)
    )

def test_neg() -> None:
    assert (
       -A(0x_05_04_03_02_01, *s) ==
        A(0x_0b_0c_0d_0e_0f, *s)
    )

def test_invert() -> None:
    assert (
       ~A(0x_05_04_03_02_01, *s) ==
        A(0x_0a_0b_0c_0d_0e, *s)
    )

def test_bit_and() -> None:
    s = (2, 2, 4)
    assert (
        A(0b_0000_0001_0010_0011, *s) &
        A(0b_0011_0001_0010_0000, *s) ==
        A(0b_0000_0001_0010_0000, *s)
    )
    assert (
        A(0b_0000_0001_0010_0011, *s) &
        0b_10 ==
        A(0b_0000_0000_0010_0010, *s)
    )

def test_bit_or() -> None:
    s = (2, 2, 4)
    assert (
        A(0b_0000_0001_0010_0011, *s) |
        A(0b_0011_0001_0010_0000, *s) ==
        A(0b_0011_0001_0010_0011, *s)
    )
    assert (
        A(0b_0000_0001_0010_0011, *s) |
        0b_10 ==
        A(0b_0010_0011_0010_0011, *s)
    )

def test_bit_xor() -> None:
    s = (2, 2, 4)
    assert (
        A(0b_0000_0001_0010_0011, *s) ^
        A(0b_0011_0001_0010_0000, *s) ==
        A(0b_0011_0000_0000_0011, *s)
    )
    assert (
        A(0b_0000_0001_0010_0011, *s) ^
        0b_10 ==
        A(0b_0010_0011_0000_0001, *s)
    )

def test_bit_shift() -> None:
    s = (2, 2, 4)
    assert (
        A(0b_0000_0001_0010_0011, *s) >>
        1 ==
        A(0b_0000_0000_0001_0001, *s)
    )
    assert (
        A(0b_0000_0001_0010_0011, *s) <<
        1 ==
        A(0b_0000_0010_0000_0010, *s)
    )

def test_to_bool() -> None:
    assert (
        A(0x_05_00_03_02_01, *s).is_true() ==
        A(0x_01_00_01_01_01, *s)
    )
    assert (
        A(0x_05_00_03_02_01, *s).is_false() ==
        A(0x_00_01_00_00_00, *s)
    )

def test_cmp() -> None:
    assert (
        A(0x_05_04_03_02_01, *s).eq(
        A(0x_02_04_02_04_02, *s)) ==
        A(0x_00_01_00_00_00, *s)
    )
    assert (
        A(0x_05_04_03_02_01, *s).ne(
        A(0x_02_04_02_04_02, *s)) ==
        A(0x_01_00_01_01_01, *s)
    )
    assert (
        A(0x_05_04_03_02_01, *s).gt(
        A(0x_02_04_02_04_02, *s)) ==
        A(0x_01_00_01_00_00, *s)
    )
    assert (
        A(0x_05_04_03_02_01, *s).lt(
        A(0x_02_04_02_04_02, *s)) ==
        A(0x_00_00_00_01_01, *s)
    )
    assert (
        A(0x_05_04_03_02_01, *s).ge(
        A(0x_02_04_02_04_02, *s)) ==
        A(0x_01_01_01_00_00, *s)
    )
    assert (
        A(0x_05_04_03_02_01, *s).le(
        A(0x_02_04_02_04_02, *s)) ==
        A(0x_00_01_00_01_01, *s)
    )

# fmt: on
