def test_project_structure():
    import pathlib
    assert pathlib.Path('README.md').exists()
    assert pathlib.Path('requirements.txt').exists()
