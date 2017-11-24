Check_MK Plugins
================

This is a collection of plugins for the [Check_MK Monitoring system](http://mathias-kettner.com/check_mk.html)
that I wrote.


Building
--------

To build all the plugins, clone this repository and run:

    make all

(Make sure to have Python3 installed.)

You can also build a single plugin, e.g.:

    make check_hls

The files (*.mkp) will be written into the `build/` directory.


Installing
----------

SSH into your Check_MK machine, change to the user of the site you want to install the plugin,
then run:

    mkp install /path/to/plugin.mkp

