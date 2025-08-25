from flexsim.mechanics import calculate_damage, encounter_occurs, save_game, load_game


def test_calculate_damage():
    assert calculate_damage(10, 3) == 7
    assert calculate_damage(3, 5) == 1


def test_encounter_occurs_true():
    rng = iter([0.05]).__next__
    assert encounter_occurs(0.1, rng) is True


def test_encounter_occurs_false():
    rng = iter([0.2]).__next__
    assert encounter_occurs(0.1, rng) is False


def test_save_and_load(tmp_path):
    state = {"hp": 10, "items": ["potion"]}
    filename = tmp_path / "save.json"
    save_game(state, filename)
    loaded_state = load_game(filename)
    assert loaded_state == state
