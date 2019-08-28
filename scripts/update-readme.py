#!/usr/bin/env python

import re

README_FILE = 'README.md'

PACKAGES_PATTERN = r"<!\-\-\s*PACKAGES:\s*(.*?)\s*\-\->(.*?)<!\-\-\s*END PACKAGES\s*\-\->\s*\n"

def render_packages(config,
                    pkgs=[],
                    prefix='',
                    upstream='https://github.com/Icinga/%s',
                    rpm='https://git.icinga.com/packaging/rpm-%s',
                    deb='https://git.icinga.com/packaging/deb-%s',
                    sorted=True):
    text = "<!-- PACKAGES: %s -->\n" % (config)

    text += "Package | Repositories\n"
    text += "--------|-------------\n"

    if sorted:
        pkgs.sort()

    for package in pkgs:
        if prefix:
            package = prefix + package

        text += ("[%s](" + upstream + ") | ") % (package, package)
        text += ("[RPM](" + rpm + ")") % (package)
        text += (" - [Debian/Ubuntu](" + deb + ")") % (package)
        text += "\n"

    text += "<!-- END PACKAGES -->\n\n"

    return text

def parse_config(text):
    config = {}
    (pkgs, options) = re.split(r"\s*\|\s*", text, 1)
    config['pkgs'] = pkgs.strip().split(' ')
    for opt in re.split(r"\s+", options.strip()):
        match = re.match(r"^(\w+)=(.+)$", opt)
        if match and match.group(1) != 'pkgs':
            config[match.group(1)] = match.group(2)
        else:
            raise Exception("Option '%s' is invalid!" % opt)
    return config

def main():
    with open(README_FILE, 'r') as _f:
        content = _f.read()

    for match in re.finditer(PACKAGES_PATTERN, content, re.DOTALL):
        config_line = match.group(1).strip()
        config = parse_config(config_line)
        config['config'] = config_line
        result = render_packages(**config)

        content = re.sub(re.escape(match.group(0)), result, content, re.DOTALL)

    with open(README_FILE, 'w') as _f:
        _f.write(content)

main()
