Imports System.Runtime.InteropServices

Public Class clsBXLAPI_x86

#Region " DLL API Function "

    Public Declare Function ConnectPrinterW Lib "BXLPDC.dll" Alias "ConnectPrinterW" (<MarshalAs(UnmanagedType.LPWStr)> ByVal szPrinterName As String) As Boolean

    Public Declare Sub DisconnectPrinter Lib "BXLPDC.dll" Alias "DisconnectPrinter" ()

    Public Declare Function Start_Doc Lib "BXLPDC.dll" Alias "Start_Doc" (ByVal szDocName As String) As Boolean
    Public Declare Function Start_DocW Lib "BXLPDC.dll" Alias "Start_DocW" (<MarshalAs(UnmanagedType.LPWStr)> ByVal szDocName As String) As Boolean


    Public Declare Sub End_Doc Lib "BXLPDC.dll" Alias "End_Doc" ()
    Public Declare Function Start_Page Lib "BXLPDC.dll" Alias "Start_Page" () As Boolean
    Public Declare Sub End_Page Lib "BXLPDC.dll" Alias "End_Page" ()

    Public Declare Function PrintDeviceFont Lib "BXLPDC.dll" Alias "PrintDeviceFont" ( _
                                                ByVal nPositionX As Integer, _
                                                ByVal nPositionY As Integer, _
                                                ByVal szFontName As String, _
                                                ByVal nFontSize As Integer, _
                                                ByVal szData As String _
                                                ) As Integer

    Public Declare Function PrintDeviceFontW Lib "BXLPDC.dll" Alias "PrintDeviceFontW" ( _
                                            ByVal nPositionX As Integer, _
                                            ByVal nPositionY As Integer, _
                                            <MarshalAs(UnmanagedType.LPWStr)> ByVal szFontName As String, _
                                            ByVal nFontSize As Integer, _
                                            <MarshalAs(UnmanagedType.LPWStr)> ByVal szData As String _
                                            ) As Integer

    Public Declare Function PrintTrueFont Lib "BXLPDC.dll" Alias "PrintTrueFont" ( _
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

    Public Declare Function PrintTrueFontW Lib "BXLPDC.dll" Alias "PrintTrueFontW" ( _
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

    Public Declare Function PrintBitmap Lib "BXLPDC.dll" Alias "PrintBitmap" ( _
                                        ByVal nPositionX As Integer, _
                                        ByVal nPositionY As Integer, _
                                        ByVal bitmapFile As String _
                                        ) As Integer

    Public Declare Function PrintBitmapW Lib "BXLPDC.dll" Alias "PrintBitmapW" ( _
                                    ByVal nPositionX As Integer, _
                                    ByVal nPositionY As Integer, _
                                    <MarshalAs(UnmanagedType.LPWStr)> ByVal bitmapFile As String _
                                    ) As Integer


#End Region

End Class
