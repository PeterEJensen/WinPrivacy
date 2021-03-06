# WinPrivacy
> Easily disable windows 10 tracking features with a single click


This small tool will disable tracking features from within regedit.

![](https://imgur.com/jcW3w9Z)
![Running from console](https://i.imgur.com/jcW3w9Z.png)
## Installation
Running from .py file:

```sh
in cmd/powershell type:
pip install requirements.txt
python WinPrivacy.py

Make sure the cmd is opened in the same directory as the files are locate
```

Running as .exe on windows:
```sh
Run the .exe file *as admin* and follow instructions on screen.
```

## Usage example

The tool is mostly focused towards anyone who do not feel comfortable editing the regedit. 


## Dev comments

* Telemetry - Sends usage and performance data to Microsoft.
* DiagTrack - Same as Telemetry, but for diagnose.
* GameDVR - Unused Xbox software that is both annoying and takes up system resources.
* dmwappushservice - Windows mobile data collector.



<!-- Markdown link & img dfn's -->
[npm-image]: https://img.shields.io/npm/v/datadog-metrics.svg?style=flat-square
[npm-url]: https://npmjs.org/package/datadog-metrics
[npm-downloads]: https://img.shields.io/npm/dm/datadog-metrics.svg?style=flat-square
[travis-image]: https://img.shields.io/travis/dbader/node-datadog-metrics/master.svg?style=flat-square
[travis-url]: https://travis-ci.org/dbader/node-datadog-metrics
[wiki]: https://github.com/yourname/yourproject/wiki
