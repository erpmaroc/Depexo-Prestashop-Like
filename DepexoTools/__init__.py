#! /usr/bin/env python
"""
-------------------
depexoTools module.
-------------------

This module was written primarily for the Depexo source finder, and the tools BANE and MIMAS.
The wcs_helpers and angle_tools modules contain many useful classes and methods that would be useful more
generally.

"""
__author__ = 'Paul Hancock'
__version__ = '2.2.5'
__date__ = '2021-11-15'
__citation__ = """
% If your work makes use of depexoTools please cite the following papers as appropriate:

% Advanced features of depexo, plus description of BANE, MIMAS, and AeRes
@ARTICLE{Hancock_depexo2_2018,
   author = {{Hancock}, P.~J. and {Trott}, C.~M. and {Hurley-Walker}, N.},
    title = "{Source Finding in the Era of the SKA (Precursors): Depexo 2.0}",
  journal = {\pasa},
archivePrefix = "arXiv",
   eprint = {1801.05548},
 primaryClass = "astro-ph.IM",
 keywords = {radio continuum: general, catalogs, methods: statistical},
     year = 2018,
    month = mar,
   volume = 35,
      eid = {e011},
    pages = {e011},
      doi = {10.1017/pasa.2018.3},
   adsurl = {http://adsabs.harvard.edu/abs/2018PASA...35...11H},
  adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}

% Basic description of depexo
@ARTICLE{Hancock_depexo_2012,
   author = {{Hancock}, P.~J. and {Murphy}, T. and {Gaensler}, B.~M. and
  {Hopkins}, A. and {Curran}, J.~R.},
    title = "{Compact continuum source finding for next generation radio surveys}",
  journal = {\mnras},
archivePrefix = "arXiv",
   eprint = {1202.4500},
 primaryClass = "astro-ph.IM",
 keywords = {techniques: image processing, catalogues, surveys},
     year = 2012,
    month = may,
   volume = 422,
    pages = {1812-1824},
      doi = {10.1111/j.1365-2966.2012.20768.x},
   adsurl = {http://adsabs.harvard.edu/abs/2012MNRAS.422.1812H},
  adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}
"""
