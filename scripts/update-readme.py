#!/usr/bin/env python

import re

README_FILE = 'README.md'

PACKAGES_PATTERN = r"<!\-\-\s*PACKAGES:(.*?)\s*\-\->(.*?)<!\-\-\s*END PACKAGES\s*\-\->\s*\n"
PACKAGES_BADGES_PATTERN = r"<!\-\-\s*PACKAGE BADGES:\s*(\S+)\s+(\S+)\s*\-\->.*"

BASEURL = "https://git.icinga.com/packaging"

def build_badge(name, variant):
    project = variant + "-" + name
    return "[![%s](%s/%s/badges/master/pipeline.svg?style=flat-square)](%s/%s)" % (
        variant, BASEURL, project, BASEURL, project)

def render_badges(name, variants):
    text = "<!-- PACKAGE BADGES: %s %s --> " % (name, ",".join(variants))

    for variant in variants:
        text += build_badge(name, variant) + " | "

    return text

def render_packages(config,
                    pkgs=[],
                    prefix='',
                    upstream='https://github.com/Icinga/%s',
                    sorted=True):
    text = "<!-- PACKAGES:%s -->\n" % (config)

    text += "Package | RPM | Debian/Ubuntu\n"
    text += "--------|-----|--------------\n"

    if sorted:
        pkgs.sort()

    for package in pkgs:
        if prefix:
            package = prefix + package

        text += ("[%s](" + upstream + ") | ") % (package, package)
        text += build_badge(package, "rpm")
        text += " | "
        text += build_badge(package, "deb")
        text += "\n"

    text += "<!-- END PACKAGES -->\n\n"

    return text

def parse_config(text):
    config = {}
    (pkgs, options) = re.split(r"\s*\|\s*", text.strip(), 1, re.DOTALL)
    config['pkgs'] = re.split(r"[\s\r\n]*", pkgs.strip())
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
        config_line = match.group(1)
        config = parse_config(config_line)
        config['config'] = config_line
        result = render_packages(**config)

        content = re.sub(re.escape(match.group(0)), result, content, re.DOTALL)

    for match in re.finditer(PACKAGES_BADGES_PATTERN, content):
        name = match.group(1)
        variants = match.group(2).split(",")
        result = render_badges(name, variants)

        content = re.sub(re.escape(match.group(0)), result, content)

    with open(README_FILE, 'w') as _f:
        _f.write(content)

main()
