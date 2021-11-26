Depexo software tools
======

Programs included:
* Depexo - The Depexo source finding program. All your^ radio astronomy source finding needs in one spiffy program.
* BANE - The Background and Noise Estimation tool. For providing high quality background and noise images for use with depexo, at a small fraction of the cost of a full box-car smooth.
* MIMAS - The Multi-resolution Image Masking tool for Depexo Software. For creating image regions which can be used to restrict the source finding of depexo, to mask fits files, and to create ds9 region files.
* SR6 - A tool for shrinking and growing fits files, such as those created with BANE.py --compress. Shrinking is done by decimation, growing is done by linear interpolation.
* AeRes - A tool for adding or subtracting sources from an image - "Depexo Residual". Catalogues must be in Depexo readable format (eg, written by depexo, modified by user). This can be used to look for missed sources, mis-characterised sources, or for simulating new images.
* AeReg - A tool for adjusting an existing catalogue of sources by regrouping or resizing the components. Uses the same strategies as the Depexo priorized fitting pre-processing.

^ - by "your" I mean "my"

Installing
=====
depexoTools is built and tested on python 3.6 and 3.7.

You can install via pip using 
`pip install git+https://github.com/PaulHancock/Depexo.git` (latest)
`pip install depexoTools` (stable)

Or you can clone or download the repository and then use `python setup.py install` or `pip install .`




Until there is a more appropriate method for crediting software development and maintainance, please also consider including me as a co-author on publications which rely on Depexo or depexoTools.




