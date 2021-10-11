#!/usr/bin/env python
# coding: utf-8

import hubmapbags

data_provider = 'Vanderbilt University'
metadata_file = 'hubmap-maldi-ims-neg-20210820.csv'

hubmapbags.magic.do_it( data_provider, metadata_file )
