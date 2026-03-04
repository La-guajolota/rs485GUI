Imports System.Runtime.InteropServices

Public Class clsBXLAPI_x64

#Region " DLL API Function "

    Public Declare Function ConnectPrinter Lib "BXLPDC_x64.dll" Alias "ConnectPrinter" (ByVal szPrinterName As String) As Boolean
    Public Declare Function ConnectPrinterW Lib "BXLPDC_x64.dll" Alias "ConnectPrinterW" (<MarshalAs(UnmanagedType.LPWStr)> ByVal szPrinterName As String) As Boolean

    Public Declare Sub DisconnectPrinter Lib "BXLPDC_x64.dll" Alias "DisconnectPrinter" ()

    Public Declare Function Start_Doc Lib "BXLPDC_x64.dll" Alias "Start_Doc" (ByVal szDocName As String) As Boolean
    Public Declare Function Start_DocW Lib "BXLPDC_x64.dll" Alias "Start_DocW" (<MarshalAs(UnmanagedType.LPWStr)> ByVal szDocName As String) As Boolean


    Public Declare Sub End_Doc Lib "BXLPDC_x64.dll" Alias "End_Doc" ()
    Public Declare Function Start_Page Lib "BXLPDC_x64.dll" Alias "Start_Page" () As Boolean
    Public Declare Sub End_Page Lib "BXLPDC_x64.dll" Alias "End_Page" ()

    Public Declare Function PrintDeviceFont Lib "BXLPDC_x64.dll" Alias "PrintDeviceFont" ( _
                                                ByVal nPositionX As Integer, _
                                                ByVal nPositionY As Integer, _
                                                ByVal szFontName As String, _
                                                ByVal nFontSize As Integer, _
                                                ByVal szData As String _
                                                ) As Integer

    Public Declare Function PrintDeviceFontW Lib "BXLPDC_x64.dll" Alias "PrintDeviceFontW" ( _
                                            ByVal nPositionX As Integer, _
                                            ByVal nPositionY As Integer, _
                                            <MarshalAs(UnmanagedType.LPWStr)> ByVal szFontName As String, _
                                            ByVal nFontSize As Integer, _
                                            <MarshalAs(UnmanagedType.LPWStr)> ByVal szData As String _
                                            ) As Integer

    Public Declare Function PrintTrueFont Lib "BXLPDC_x64.dll" Alias "PrintTrueFont" ( _
                                            ByVal nPositionX As Integer, _
                                            ByVal nPositionY As Integer, _
                                            ByVal szFontName As String, _
                                            ByVal nFontSize As Integer, _
                                            ByVal szData As String, _
                                            Optional ByVal bBold As Boolean = False, _
                                            Optional ByVal nRotation As Integer = 0, _
                                            Optional ByVal bItalic As Boolean = False, _
                                            Optional ByVal bUnderline As Boolean = False _
                                            ) As Integer

    Public Declare Function PrintTrueFontW Lib "BXLPDC_x64.dll" Alias "PrintTrueFontW" ( _
                                        ByVal nPositionX As Integer, _
                                        ByVal nPositionY As Integer, _
                                        <MarshalAs(UnmanagedType.LPWStr)> ByVal szFontName As String, _
                                        ByVal nFontSize As Integer, _
                                        <MarshalAs(UnmanagedType.LPWStr)> ByVal szData As String, _
                                        Optional ByVal bBold As Boolean = False, _
                                        Optional ByVal nRotation As Integer = 0, _
                                        Optional ByVal bItalic As Boolean = False, _
                                        Optional ByVal bUnderline As Boolean = False _
                                        ) As Integer

    Public Declare Function PrintBitmap Lib "BXLPDC_x64.dll" Alias "PrintBitmap" ( _
                                        ByVal nPositionX As Integer, _
                                        ByVal nPositionY As Integer, _
                                        ByVal bitmapFile As String _
                                        ) As Integer

    Public Declare Function PrintBitmapW Lib "BXLPDC_x64.dll" Alias "PrintBitmapW" ( _
                                    ByVal nPositionX As Integer, _
                                    ByVal nPositionY As Integer, _
                                    <MarshalAs(UnmanagedType.LPWStr)> ByVal bitmapFile As String _
                                    ) As Integer

#End Region

End Class
