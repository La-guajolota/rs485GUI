using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

using System.Runtime.InteropServices;

using System.Windows.Forms;

namespace SamplePg_CS
{
    class BXLAPI
    {
        public static bool Is64Bit()
        {
            bool retVal = true;
            if (System.Environment.GetEnvironmentVariable("PROCESSOR_ARCHITECTURE") == "x86")
                retVal = false;

            return retVal;
        }

        //	Rotation
        public const int ROTATE_0 = 0;
        public const int ROTATE_90 = 1;
        public const int ROTATE_180 = 2;
        public const int ROTATE_270 = 3;

        public static bool ConnectPrinter(string szPrinterName)
        {
            if (Is64Bit())
                return BXLAPI_x64.ConnectPrinterW(szPrinterName);
            else
                return BXLAPI_x86.ConnectPrinterW(szPrinterName);
        }

        public static void DisconnectPrinter()
        {
            if (Is64Bit())
                BXLAPI_x64.DisconnectPrinter();
            else
                BXLAPI_x86.DisconnectPrinter();
        }

        public static bool Start_Doc(string szDocName)
        {
            if (Is64Bit())
                return BXLAPI_x64.Start_DocW(szDocName);
            else
                return BXLAPI_x86.Start_DocW(szDocName);
        }

        public static void End_Doc()
        {
            if (Is64Bit())
                BXLAPI_x64.End_Doc();
            else
                BXLAPI_x86.End_Doc();
        }

        public static bool Start_Page()
        {
            if (Is64Bit())
                return BXLAPI_x64.Start_Page();
            else
                return BXLAPI_x86.Start_Page();
        }

        public static void End_Page()
        {
            if (Is64Bit())
                BXLAPI_x64.End_Page();
            else
                BXLAPI_x86.End_Page();
        }

        public static int PrintDeviceFont(int nPositionX, int nPositionY, string szFontName, int nFontSize, string szData)
        {
            if (Is64Bit())
                return BXLAPI_x64.PrintDeviceFontW(nPositionX, nPositionY, szFontName, nFontSize, szData);
            else
                return BXLAPI_x86.PrintDeviceFontW(nPositionX, nPositionY, szFontName, nFontSize, szData);
        }

        public static int PrintTrueFont(int nPositionX,
                                        int nPositionY,
                                        string szFontName,
                                        int nFontSize,
                                        string szData,
                                        bool bBold,
                                        int nRotation,
                                        bool bItalic,
                                        bool bUnderline)
        {
            if (Is64Bit())
                return BXLAPI_x64.PrintTrueFontW(nPositionX, nPositionY, szFontName, nFontSize, szData, bBold, nRotation, bItalic, bUnderline);
            else
                return BXLAPI_x86.PrintTrueFontW(nPositionX, nPositionY, szFontName, nFontSize, szData, bBold, nRotation, bItalic, bUnderline);
        }

        public static int PrintBitmap(int nPositionX, int nPositionY, string bitmapFile)
        {
            if (Is64Bit())
                return BXLAPI_x64.PrintBitmapW(nPositionX, nPositionY, bitmapFile);
            else
                return BXLAPI_x86.PrintBitmapW(nPositionX, nPositionY, bitmapFile);
        }
    }
}
