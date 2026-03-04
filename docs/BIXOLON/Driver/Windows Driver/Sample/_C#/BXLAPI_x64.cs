using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

using System.Runtime.InteropServices;

namespace SamplePg_CS
{
    class BXLAPI_x64
    {
        //////////////////////////////////////////////////////////////////////
        //  Function List
        [DllImport("BXLPDC_x64.dll")]
        public static extern bool ConnectPrinter(string szPrinterName);
        [DllImport("BXLPDC_x64.dll")]
        public static extern bool ConnectPrinterW([MarshalAs(UnmanagedType.LPWStr)]string szPrinterName);
        [DllImport("BXLPDC_x64.dll")]
        public static extern void DisconnectPrinter();
        [DllImport("BXLPDC_x64.dll")]
        public static extern bool Start_Doc(string szDocName);
        [DllImport("BXLPDC_x64.dll")]
        public static extern bool Start_DocW([MarshalAs(UnmanagedType.LPWStr)]string szDocName);
        [DllImport("BXLPDC_x64.dll")]
        public static extern void End_Doc();
        [DllImport("BXLPDC_x64.dll")]
        public static extern bool Start_Page();
        [DllImport("BXLPDC_x64.dll")]
        public static extern void End_Page();
        [DllImport("BXLPDC_x64.dll")]
        public static extern int PrintDeviceFont(int nPositionX, int nPositionY, string szFontName, int nFontSize, string szData);
        [DllImport("BXLPDC_x64.dll")]
        public static extern int PrintDeviceFontW(int nPositionX, int nPositionY, [MarshalAs(UnmanagedType.LPWStr)]string szFontName, int nFontSize, [MarshalAs(UnmanagedType.LPWStr)]string szData);
        [DllImport("BXLPDC_x64.dll")]
        public static extern int PrintTrueFont(int nPositionX,
                                                int nPositionY,
                                                string szFontName,
                                                int nFontSize,
                                                string szData,
                                                bool bBold,
                                                int nRotation,
                                                bool bItalic,
                                                bool bUnderline);
        [DllImport("BXLPDC_x64.dll")]
        public static extern int PrintTrueFontW(int nPositionX,
                                                int nPositionY,
                                                [MarshalAs(UnmanagedType.LPWStr)]string szFontName,
                                                int nFontSize,
                                                [MarshalAs(UnmanagedType.LPWStr)]string szData,
                                                bool bBold,
                                                int nRotation,
                                                bool bItalic,
                                                bool bUnderline);
        [DllImport("BXLPDC_x64.dll")]
        public static extern int PrintBitmap(int nPositionX, int nPositionY, string bitmapFile);
        [DllImport("BXLPDC_x64.dll")]
        public static extern int PrintBitmapW(int nPositionX, int nPositionY, [MarshalAs(UnmanagedType.LPWStr)]string bitmapFile);
    }
}
