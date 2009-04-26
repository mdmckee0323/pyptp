#!/usr/bin/python

import sys
import traceback
from pyptp.PtpUsbTransport import PtpUsbTransport
from pyptp.PtpSession import PtpSession, PtpException
from pyptp import PtpValues

ptpTransport = PtpUsbTransport(0, 0)
ptpSession = PtpSession(ptpTransport)

vendorId = PtpValues.Vendors.STANDARD
try:
    ptpSession.OpenSession()
    deviceInfo = ptpSession.GetDeviceInfo()
    vendorId = deviceInfo.VendorExtensionID
    
    id = 0
    while True:
        ptpSession.InitiateCapture(objectFormatId=PtpValues.StandardObjectFormats.EXIF_JPEG)

        objectid = None
        while True:
            evt = ptpSession.CheckForEvent(30000)
            if evt == None:
                raise Exception("Capture did not complete")
            if evt.eventcode == PtpValues.StandardEvents.OBJECT_ADDED:
                objectid = evt.params[0]
            if evt.eventcode == PtpValues.StandardEvents.CAPTURE_COMPLETE:
                break

        if objectid != None:
            file = open("capture_%i.jpg" % id, "w")
            ptpSession.GetObject(objectid, file)
            file.close()
            id+=1
            ptpSession.DeleteObject(objectid)

except PtpException, e:
    print "PTP Exception: %s" % PtpValues.ResponseNameById(e.responsecode, vendorId)
except Exception, e:
    print "An exception occurred: %s" % e
    traceback.print_exc()

del ptpSession
del ptpTransport