#!/usr/bin/env python
# coding: utf-8

import hubmapbags

data_provider = 'University of Florida'
metadata_file = 'hubmap-scrnaseq-20210609.csv'

hubmapbags.magic.do_it( data_provider, metadata_file )