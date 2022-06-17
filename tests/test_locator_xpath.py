import re

from playwright.sync_api import Page
from playwright_dompath.dompath_sync import xpath_path


def pageFromTemplate(template: str) -> str:
    return re.sub(
        r"[\s\n]+/s",
        " ",
        f"""data:text/html;charset=utf-8,<!DOCTYPE html>
            <html>
                <body>
                    {template}
                </body>
            </html>""",
    )


def test_should_return_correct_path_for_id(page: Page):
    page.goto(pageFromTemplate("<div id='test'></div>"))
    div = page.locator("#test")
    path = xpath_path(div)
    assert path == '//*[@id="test"]'


def test_should_return_correct_path_for_single_class(page: Page):
    page.goto(pageFromTemplate('<div class="test">test</div><div>test2</div>'))
    div = page.locator(".test")
    path = xpath_path(div)
    assert path == "/html/body/div[1]"


def test_should_return_the_correct_path_for_nested_classes(page: Page):
    page.goto(
        pageFromTemplate(
            '<div class="main">main<div class="child">child</div><div></div></div>'
        )
    )
    div = page.locator(".main .child")
    path = xpath_path(div)
    assert path == "/html/body/div/div[1]"


def test_should_return_the_correct_path_for_multiple_elements(page: Page):
    page.goto(pageFromTemplate("<div>test1</div><div>test2</div><div>test3</div>"))
    divs = page.locator("div")
    for i in range(divs.count()):
        path = xpath_path(divs.nth(i))
        assert path == f"/html/body/div[{i + 1}]"
