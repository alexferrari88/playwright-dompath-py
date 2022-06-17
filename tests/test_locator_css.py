import re

from playwright.sync_api import Page
from playwright_dompath.dompath_sync import css_path


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
    path = css_path(div)
    assert path == "#test"


def test_should_return_correct_path_for_single_class(page: Page):
    page.goto(pageFromTemplate('<div class="test">test</div><div>test2</div>'))
    div = page.locator(".test")
    path = css_path(div)
    assert path == "body > div.test"


def test_should_return_the_correct_path_for_multiple_classes(page: Page):
    page.goto(pageFromTemplate('<div class="tst test">test</div><div>test2</div>'))
    div = page.locator(".test")
    path = css_path(div)
    assert path == "body > div.tst.test"


def test_should_return_the_correct_path_for_nested_classes(page: Page):
    page.goto(
        pageFromTemplate(
            '<div class="main">main<div class="child">child</div><div></div></div>'
        )
    )
    div = page.locator(".main .child")
    path = css_path(div)
    assert path == "body > div > div.child"


def test_should_return_the_correct_path_for_multiple_elements(page: Page):
    page.goto(pageFromTemplate("<div>test1</div><div>test2</div><div>test3</div>"))
    divs = page.locator("div")
    for i in range(divs.count()):
        path = css_path(divs.nth(i))
        assert path == f"body > div:nth-child({i + 1})"


def test_should_return_the_correct_path_for_nested_element(page: Page):
    page.goto(pageFromTemplate("<div><div>test</div></div>"))
    div = page.locator("div > div")
    path = css_path(div)
    assert path == "body > div > div"
