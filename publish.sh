python3 -m build && python3 -m twine upload --repository testpypi dist/* && rm -rf dist