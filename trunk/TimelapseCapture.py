#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import traceback
import time
from ptp.PtpUsbTransport import PtpUsbTransport
from ptp.PtpSession import PtpSession, PtpException
from ptp import PtpValues

if len(sys.argv) != 2:
    print >>sys.stderr, "Syntax: TimelapseCapture <interval in seconds>"
    sys.exit(1)
delay = int(sys.argv[1])

ptpTransport = PtpUsbTransport(PtpUsbTransport.findptps()[0])
ptpSession = PtpSession(ptpTransport)

vendorId = PtpValues.Vendors.STANDARD
try:
    ptpSession.OpenSession()
    deviceInfo = ptpSession.GetDeviceInfo()
    vendorId = deviceInfo.VendorExtensionID

    while True:
        ptpSession.InitiateCapture(objectFormatId=PtpValues.StandardObjectFormats.EXIF_JPEG)
        while True:
            evt = ptpSession.CheckForEvent(None)
            if evt.eventcode == PtpValues.StandardEvents.OBJECT_ADDED:
                break

        time.sleep(delay)

except PtpException, e:
    print "PTP Exception: %s" % PtpValues.ResponseNameById(e.responsecode, vendorId)
except Exception, e:
    print "An exception occurred: %s" % e
    traceback.print_exc()

del ptpSession
del ptpTransport
