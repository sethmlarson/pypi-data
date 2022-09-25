import pytest

import main


@pytest.mark.parametrize(
    "test_info,expected",
    [
        # https://pypi.org/pypi/arclet-alconna-graia/json
        (
            # input:
            {
                "bugtrack_url": "None",
                "docs_url": "None",
                "download_url": "",
                "home_page": "",
                "project_url": "https://pypi.org/project/arclet-alconna-graia/",
                "project_urls": {
                    "Bug Reports": "https://github.com/ArcletProject/Alconna/issues",
                    "Documentation": "https://arcletproject.github.io/docs/alconna/tutorial",
                    "Homepage": "https://github.com/ArcletProject/Alconna-Graia",
                    "Source": "https://github.com/ArcletProject/Alconna",
                },
            },
            # expected:
            [
                (
                    "Bug Reports",
                    "https://github.com/ArcletProject/Alconna/issues",
                    "github.com",
                ),
                (
                    "Documentation",
                    "https://arcletproject.github.io/docs/alconna/tutorial",
                    "arcletproject.github.io",
                ),
                (
                    "Homepage",
                    "https://github.com/ArcletProject/Alconna-Graia",
                    "github.com",
                ),
                (
                    "Source",
                    "https://github.com/ArcletProject/Alconna",
                    "github.com",
                ),
            ],
        ),
        # https://pypi.org/pypi/0x2nac0nda/json
        (
            # input:
            {
                "bugtrack_url": None,
                "docs_url": None,
                "download_url": "",
                "home_page": "",
                "project_url": "https://pypi.org/project/0x2nac0nda/",
                "project_urls": None,
            },
            # expected:
            [],
        ),
    ],
)
def test_get_project_urls(test_info, expected) -> None:
    result = main.get_project_urls(test_info)
    assert result == expected
