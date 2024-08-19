def abs_path_from_project(relative_path: str):
    from wikipedia_project_tests import utils
    from pathlib import Path

    return (
        Path(utils.__file__)
        .parent.parent.joinpath(relative_path)
        .absolute()
        .__str__()
    )
