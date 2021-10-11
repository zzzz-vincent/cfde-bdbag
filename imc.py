#!/usr/bin/env python
# coding: utf-8

import hubmapbags

data_provider = 'University of Florida'
metadata_file = 'hubmap-imc-20210823.csv'

hubmapbags.magic.do_it( data_provider, metadata_file )
