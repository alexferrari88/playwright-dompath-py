# Playwright DOMPath for Python 🎭

[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)
[![Python Version](https://img.shields.io/pypi/pyversions/playwright-dompath?style=flat-square)](https://pypi.org/project/playwright-dompath)
[![PyPi Version](https://img.shields.io/pypi/v/playwright-dompath?style=flat-square)](https://pypi.org/project/playwright-dompath)
[![GitHub Last Commit](https://img.shields.io/github/last-commit/alexferrari88/playwright-DOMPath?style=flat-square)](https://img.shields.io/github/last-commit/alexferrari88/playwright-DOMPath?style=flat-square)

This library implements the ChromeDevTools DOMPath functionality in Playwright.

This means that you can retrieve the CSS selector or the XPath of any element you select in your Playwright code as a Locator.

_Typescript version here: [https://github.com/alexferrari88/playwright-DOMPath](https://github.com/alexferrari88/playwright-DOMPath)_

## Installation 📦

Install with pip

```bash
  pip install playwright-dompath
```

## API Reference 📚

#### css_path

```python
css_path: (element: Playwright.Locator, optimized: bool = True) -> str
```

#### xpath_path

```python
xpath_path: (element: Playwright.Locator, optimized: bool = True) -> str
```

## Usage 🔧

Just import the `css_path` or `xpath_path` from this module.

At the moment the tested version is the dompath_sync one while there is dompath_async, it has not been tested yet.

```python
from playwright_dompath.dompath_sync import css_path, xpath_path
```

Then use either function by passing it the element you previously selected as a Locator:

```python
searchBar = page.locator('input[name="q"]')
print("CSS Path:", css_path(searchBar))
print("XPath:", xpath_path(searchBar))
```

## Full Example 🎁

```python
from playwright.sync_api import sync_playwright
from playwright_dompath.dompath_sync import css_path, xpath_path

with sync_playwright() as p:
  url = "https://google.com"
  browser = p.chromium.launch()
  page = browser.new_page()
  page.goto(url)
  searchBar = page.locator('input[name="q"]')
  print("CSS Path:", css_path(searchBar))
  print("XPath:", xpath_path(searchBar))
  browser.close()
```

Which will output (class names may vary for you):

```bash
CSS Path: body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input
XPath: /html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input
```

## TODO ✅

-   Increase tests coverage (include edge cases and async)
-   Add better error handling

## Contributing 🤝🏼

Feel free to fork this repo and create a PR. I will review them and merge if ok.

The above todos can be a very good place to start.

## Acknowledgements 🤗

-   This library reimplements the [Chrome DevTools DOMPath library](https://github.com/ChromeDevTools/devtools-frontend/blob/b6a3b2ae8a4c1d5847c2bb1535377e13ee3045be/front_end/panels/elements/DOMPath.ts) with modifications to allow the use of Playwright's ElementHandle and Locator
-   [CSS.escape polyfill](https://github.com/mathiasbynens/CSS.escape)

## License 📝

[MIT](https://choosealicense.com/licenses/mit/)
