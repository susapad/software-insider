

# SusaPad Software Insider

> [[Português](./README.pt-br.md)] | [[Español](./README.es.md)]

![gpl-3.0](./susapad/media/gplv3-with-text-136x68.png)

*SusaPad Software Insider* is the software used to configure 
*SusaPad Insider Edition*/[*MiniPad*][minipad].

> **Note**: *SusaPad Software* refers to [SusaPad Software][software],
> but it's not the same as *SusaPad*, which is just a *keypad* (hardware).
> *SusaPad Software Insider* refers to this project itself.

> **Note**: It's not available to all *SusaPad*/*MiniPad*'s version.
>
> Please read [Compatibility Section](#compatibility) to more information.

[minipad]: https://github.com/minipadKB
[software]: https://github.com/susapad/software

## User Guide

### Compatibility

It's not available to all *SusaPad*'s version 
since it's for *Insider edition* only,
which uses *Arduino* instead of *Raspberry* 
and the [old MiniPad's firmware][old-firmware] instead of the latest.

If your *SusaPad*/*MiniPad* is at the latest firmware's version,
so use the [*SusaPad Software*][software].

[old-firmware]: https://github.com/minipadKB/minipad-firmware-old
[software]: https://github.com/susapad/software

### Installation

> **Warning**: In production...

### Issues

You can add issues: bugs, doubts, questions, feature requests,
via Issues.

Please, carefully read [our pinned Issue][issue-1]
and make sure that you know about
[Github's Community Guideline][gh-rules].

[issue-1]: https://github.com/susapad/software-insider/issues/1
[gh-rules]: https://docs.github.com/en/site-policy/github-terms/github-community-guidelines#maintaining-a-strong-community

---


## Licenses

### SusaPad Software Insider

*SusaPad Software Insider* is under *GPL-3.0*, and it follows the following
four degrees of freedom:

- Freedom to run the program for any purpose.
- Freedom to study how the program works & adapt it to specific needs.
- Freedom to redistribute copies so you can help your neighbor.
- Freedom to improve the program & release your improvements to the public,
    so that the whole community benefits.

For more details about our licence: [LICENSE](./LICENSE).

### GNU Logo

Official GPL, AGPL and LGPL logos
These images are in the public domain.

For more details about GNU's logo, [GNU License Logos][gnu-logos].

### Nuitka

The Apache License, Version 2.0,
© 2023, Kay Hayen and Nuitka Contributors. All rights reserved.

This product is compiled by software developed
by Kay Hayen and Nuitka Contributors.
https://nuitka.net/index.html

For more details about their license, [read Nuitka's License][nuitka-license].

### pySerial

BSD license,
© 2001-2020 Chris Liechti <cliechti@gmx.net>

This product includes libraries developed
by Chris Liechti and pySerial's Contributors.
https://github.com/pyserial

For more details about their license, [read pySerial's License][pyserial-license].

### PySide6

The Lesser General Public License (LGPL),
© Copyright 2023 The Qt Company Ltd. All rights reserved.

This product includes libraries developed by The Qt Company Ltd.
for use in GUI.
https://www.qt.io/

For more details about their license, [read Qt's License][qt-license].

[gnu-logos]: https://www.gnu.org/graphics/license-logos.html
[nuitka-license]: https://www.apache.org/licenses/LICENSE-2.0
[pyserial-license]: https://github.com/pyserial/pyserial/blob/master/LICENSE.txt
[qt-license]: https://www.qt.io/licensing/


## FAQ

### Is it compatible with *Minipad*?

Yes, it's compatible with the [old *minipad-firmware*'s
version (*commit `f62f827`*)][minipad-commit],
used by *SusaPad Insider Edition*.


### Why my application is so slow?

It's not the application itself,
but the way it comunicate via serial port.

Unfortunately, the commands can only be sent with
one second of interval between.
As a result, some configurations
may take up to six seconds to complete.


### Is this software translated?

No, it isn't. But we plan to translate it soon.
For now *SusaPad Software Insider* is just available to Portuguese,
the native language of this project.


### Does this project have any relationship with others?

No, it isn't. This project is independent
and has no relationship with other projects
such as *Minipad Project*, *Nuitka*, *pySerial* or *QT Company*,
but it has relationship with *SusaPad* itself.

Also, worth mentioning that *SusaPad Software Insider* is a fork
of *SusaPad Software* to work with the *Arduino* version of *SusaPad*,
the *SusaPad Insider Edition*.
So, it follows the same rules and licences given by *SusaPad Software*.


[minipad-commit]: https://github.com/minipadKB/minipad-firmware-old/commit/f62f827ce73f8c3a55bdd9106de2d631eb93e775


## Contributors

- Maintainer: [sousaone1][sousa]
- Developer: [rickbarretto][rick]
- Logo Designer: [Axiey][logo]
- Legacy application by: [Luiz Fernando][batatinho]

It's good to mention Luiz Fernando who was responsible for creating
the first functional version of *SusaPad Software* in *Kivy*.


[sousa]: https://github.com/sousaone1
[rick]: https://github.com/RickBarretto
[logo]: https://osu.ppy.sh/users/11711340
[batatinho]: https://github.com/batatinhoProGamer
