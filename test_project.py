from project import wordstate, man, check


def test_wordstate():
    assert wordstate("TEST") == "_ _ _ _ "
    assert wordstate("HELLO WORLD") == "_ _ _ _ _  _ _ _ _ _ "


def test_man():
    assert man(0) == ""
    assert man(1) == "========="
    assert man(2) == "       \n       \n       \n       \n      |\n      |\n========="
    assert man(3) == "       \n       \n      |\n      |\n      |\n      |\n========="
    assert man(4) == "      +\n      |\n      |\n      |\n      |\n      |\n========="
    assert man(5) == "  +---+\n      |\n      |\n      |\n      |\n      |\n========="
    assert man(6) == "  +---+\n  |   |\n      |\n      |\n      |\n      |\n========="
    assert man(7) == "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n========="
    assert man(8) == "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n========="
    assert man(9) == "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n========="
    assert man(10) == "  +---+\n  |   |\n  O   |\n /|\  |\n      |\n      |\n========="
    assert man(11) == "  +---+\n  |   |\n  O   |\n /|\  |\n /    |\n      |\n========="
    assert man(12) == "  +---+\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n========="


def test_check():
    assert check("A", "FLAT")
    assert not check("E", "TRUTH")