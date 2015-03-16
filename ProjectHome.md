This project controls multimedia devices which support the [PTP](http://en.wikipedia.org/wiki/Picture_Transfer_Protocol) protocol. It currently supports USB devices, with an emphasis on Nikon digital camera control. It requires the [pyusb](http://pyusb.berlios.de/) library.

Nikon cameras support the PTP protocol, permitting much computer control and automation. They also implement a large number of extensions, many of which have not yet been decoded.

Several sample programs are available:
|Capture|Repeatedly capture images and save them to disk|
|:------|:----------------------------------------------|
|DumpDeviceDetails|Dump all available PTP information from a PTP device|
|HDRCapture|Perform multiple captures at different F-stops for combining into an HDR image|

The source is available [here](http://code.google.com/p/pyptp/source/browse/trunk)
