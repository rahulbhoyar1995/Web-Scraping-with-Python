### Scrapy Commands

```
scrapy <command> [options] [args]
```
You can run Scrapy with a specific command, optional options, and arguments to perform various tasks, such as creating a project, fetching data from a URL, or running a spider (the scraping logic).

Available Commands:
bench:

```
scrapy bench
```
Runs a quick benchmark test for Scrapy. This helps assess the performance of your Scrapy installation or system environment by running a test spider and measuring performance metrics.

fetch:

mathematica
```
scrapy fetch <URL>
```
Fetches the content of the specified URL using Scrapy’s downloader and prints it to the console. It simulates what Scrapy would see if it scraped the given URL.

genspider:


```
scrapy genspider <name> <domain>
```
Generates a new spider using pre-defined templates. You provide the spider name and the domain it will scrape, and Scrapy creates the initial files for the spider logic.

runspider:


```
scrapy runspider <script.py>
```
Runs a self-contained spider without creating a full Scrapy project. You point it to a script file where the spider logic is defined.

settings:

css
```
scrapy settings [options]
```
Retrieves and prints Scrapy's settings. You can use this to check and verify your Scrapy configuration.

shell:

```
scrapy shell <URL>
```
Launches an interactive scraping shell (like a Python REPL). This is useful for testing XPath/CSS selectors and interacting with web pages to see how Scrapy fetches and parses data.

startproject:


```
scrapy startproject <project_name>
```
Creates a new Scrapy project with the specified name. This generates the project directory and essential files (such as settings, items, spiders) for you to start building your web scraper.

version:

```
scrapy version
```
Prints the current version of Scrapy installed on your system.

view:

```
scrapy view <URL>
```
Opens the specified URL in a browser and shows how Scrapy "sees" the page. This can be useful for troubleshooting rendering issues or checking if Scrapy can access a specific URL.

Additional Commands:
The [ more ] section indicates that more commands will become available when you are within a Scrapy project directory. This includes commands specific to managing and interacting with the project’s spiders, pipelines, and settings.
These commands help in different stages of web scraping, from project setup to testing and executing spiders.