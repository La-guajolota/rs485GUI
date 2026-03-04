VERSION 5.00
Begin VB.Form MainForm 
   Caption         =   "Sample"
   ClientHeight    =   1410
   ClientLeft      =   60
   ClientTop       =   450
   ClientWidth     =   3270
   LinkTopic       =   "Form1"
   ScaleHeight     =   1410
   ScaleWidth      =   3270
   StartUpPosition =   3  'Windows Default
   Begin VB.CommandButton Command1 
      Caption         =   "Receipt Sample"
      Height          =   1035
      Left            =   180
      TabIndex        =   0
      Top             =   240
      Width           =   2895
   End
End
Attribute VB_Name = "MainForm"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Private Sub Command1_Click()

    For Each prnPrinter In Printers
        If prnPrinter.DeviceName = "BIXOLON SRP-275III" Then
            Set Printer = prnPrinter
            Exit For
        End If
    Next

    If Printer.DeviceName = "BIXOLON SRP-275III" Then
    
        Dim pic As Picture
    
        Printer.Font.Size = 9
        Printer.FontName = "FontControl"
        Printer.Print "x"
        
        Printer.Font.Size = 9
        Printer.FontName = "FontA2x1"
        Printer.Print "* Joshua Cafe *"
        
        Printer.Font.Size = 9
        Printer.FontName = "FontControl"
        Printer.Print "w"
        
        Printer.Font.Size = 9
        Printer.FontName = "FontA1x1"
        
        Printer.Print "    3000 Spring Street, Rancho,"
        Printer.Print "    California 10093,"
        Printer.Print "    Tel) 858-519-3698 Fax) 3852"
        
        Printer.Print vbCrLf + "---------------------------------"  'LF
        Printer.Print "Orange Juice                 5.00"
        Printer.Print "6 Bufalo Wing               24.00"
        Printer.Print "Potato Skin                 12.00"

        Printer.ForeColor = RGB(255, 0, 0)
        Printer.Print "Subtotal                    41.00"
        Printer.ForeColor = RGB(0, 0, 0)
        
        Printer.Print "Tax 6%                       2.46"
        Printer.ForeColor = RGB(255, 0, 0)
        Printer.Print "Member Discount              2.30"
        Printer.ForeColor = RGB(0, 0, 0)
        
        Printer.Print "Cash                       100.00"
        Printer.Print "Amt. Paid                   41.16"
        Printer.ForeColor = RGB(255, 0, 0)
        
        Printer.Print "Change Due                  58.84"
        Printer.ForeColor = RGB(0, 0, 0)
        Printer.Print "---------------------------------"
        
        Printer.Font.Size = 9
        Printer.FontName = "FontControl"
        Printer.Print "x"
        
        Printer.Font.Size = 9
        Printer.FontName = "FontA1x1"
        Printer.Print "Member Number :  452331949" + vbCrLf
        
        Printer.Font.Size = 9
        Printer.FontName = "FontA1x1"
        Printer.Print "Have a nice day !" + vbCrLf
        
        Printer.Print "Sale Date: 07/01/03"
        Printer.Print "Time: 12:30:45"
        

        Printer.EndDoc
    Else
        MsgBox "SRP-275III windows driver is not installed."
    End If
        
End Sub
