import pytest

from multipipe import Multipipe


# FIXTURES =====================================================================
@pytest.fixture
def lowercase():
    return str.lower


@pytest.fixture
def tokenize():
    return str.split


@pytest.fixture
def inputs():
    return ["Black Sabbath", "Ozzy Osbourne"]


# TESTS ========================================================================
def test_multipipe_generator(inputs, lowercase, tokenize):
    pipeline = Multipipe([lowercase, tokenize])
    out = list(pipeline(inputs))

    assert out[0] == ["black", "sabbath"]
    assert out[1] == ["ozzy", "osbourne"]


def test_multipipe_list(inputs, lowercase, tokenize):
    pipeline = Multipipe([lowercase, tokenize])
    out = pipeline(inputs, generator=False)

    print(out)
    print(list(out))

    assert out[0] == ["black", "sabbath"]
    assert out[1] == ["ozzy", "osbourne"]
