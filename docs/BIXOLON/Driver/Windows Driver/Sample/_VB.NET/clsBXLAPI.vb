Public Class clsBXLAPI

#Region " Constant List "
    ' Rotation
    Public Const ROTATE_0 As Integer = 0
    Public Const ROTATE_90 As Integer = 1
    Public Const ROTATE_180 As Integer = 2
    Public Const ROTATE_270 As Integer = 3
#End Region

    Private m_Is64Bit As Boolean = False


    Public Sub New()
        m_Is64Bit = Is64Bit()
    End Sub

    Public Function Is64Bit() As Boolean
        Dim retVal As Boolean = True
        If System.Environment.GetEnvironmentVariable("PROCESSOR_ARCHITECTURE") = "x86" Then
            retVal = False
        End If

        Return retVal
    End Function

#Region " Function List "

    Public Function ConnectPrinter(ByVal szPrinterName As String) As Boolean
        If (m_Is64Bit) Then
            'MsgBox("x64")
            Return clsBXLAPI_x64.ConnectPrinterW(szPrinterName)
        Else
            'MsgBox("x86")
            Return clsBXLAPI_x86.ConnectPrinterW(szPrinterName)
        End If
    End Function

    Public Sub DisconnectPrinter()
        If m_Is64Bit = True Then
            'MsgBox("x64")
            clsBXLAPI_x64.DisconnectPrinter()
        Else
            'MsgBox("x86")
            clsBXLAPI_x86.DisconnectPrinter()
        End If
    End Sub

    Public Function Start_Doc(ByVal szDocName As String) As Boolean
        If (m_Is64Bit) Then
            Return clsBXLAPI_x64.Start_DocW(szDocName)
        Else
            Return clsBXLAPI_x86.Start_DocW(szDocName)
        End If
    End Function

    Public Sub End_Doc()
        If (m_Is64Bit) Then
            clsBXLAPI_x64.End_Doc()
        Else
            clsBXLAPI_x86.End_Doc()
        End If
    End Sub

    Public Function Start_Page() As Boolean
        If (m_Is64Bit) Then
            Return clsBXLAPI_x64.Start_Page()
        Else
            Return clsBXLAPI_x86.Start_Page()
        End If
    End Function

    Public Sub End_Page()
        If (m_Is64Bit) Then
            clsBXLAPI_x64.End_Page()
        Else
            clsBXLAPI_x86.End_Page()
        End If
    End Sub

    Public Function PrintDeviceFont(ByVal nPositionX As Integer, ByVal nPositionY As Integer, ByVal szFontName As String, ByVal nFontSize As Integer, ByVal szData As String) As Integer
        If (m_Is64Bit) Then
            Return clsBXLAPI_x64.PrintDeviceFontW(nPositionX, nPositionY, szFontName, nFontSize, szData)
        Else
            Return clsBXLAPI_x86.PrintDeviceFontW(nPositionX, nPositionY, szFontName, nFontSize, szData)
        End If
    End Function

    Public Function PrintTrueFont(ByVal nPositionX As Integer, ByVal nPositionY As Integer, ByVal szFontName As String, ByVal nFontSize As Integer, ByVal szData As String, _
                                    Optional ByVal bBold As Boolean = False, Optional ByVal nRotation As Integer = 0, Optional ByVal bItalic As Boolean = False, Optional ByVal bUnderline As Boolean = False) As Integer
        If (m_Is64Bit) Then
            Return clsBXLAPI_x64.PrintTrueFontW(nPositionX, nPositionY, szFontName, nFontSize, szData, _
                                            bBold, nRotation, bItalic, bUnderline)
        Else
            Return clsBXLAPI_x86.PrintTrueFontW(nPositionX, nPositionY, szFontName, nFontSize, szData, _
                                            bBold, nRotation, bItalic, bUnderline)
        End If
    End Function

    Public Function PrintBitmap(ByVal nPositionX As Integer, ByVal nPositionY As Integer, ByVal bitmapFile As String) As Integer
        If (m_Is64Bit) Then
            Return clsBXLAPI_x64.PrintBitmapW(nPositionX, nPositionY, bitmapFile)
        Else
            Return clsBXLAPI_x86.PrintBitmapW(nPositionX, nPositionY, bitmapFile)
        End If
    End Function

#End Region


End Class
