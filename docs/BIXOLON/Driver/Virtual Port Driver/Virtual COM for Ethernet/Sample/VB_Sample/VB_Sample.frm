VERSION 5.00
Object = "{648A5603-2C6E-101B-82B6-000000000014}#1.1#0"; "MSCOMM32.OCX"
Begin VB.Form VB_Sample 
   Caption         =   "VB_Sample"
   ClientHeight    =   2655
   ClientLeft      =   60
   ClientTop       =   450
   ClientWidth     =   3435
   LinkTopic       =   "VB_Sample"
   ScaleHeight     =   2655
   ScaleWidth      =   3435
   StartUpPosition =   3  'Windows Default
   Begin VB.CommandButton Command2 
      Caption         =   "Test Print (Label Printer)"
      Height          =   855
      Left            =   240
      TabIndex        =   1
      Top             =   1440
      Width           =   2895
   End
   Begin MSCommLib.MSComm MSComm1 
      Left            =   120
      Top             =   840
      _ExtentX        =   1005
      _ExtentY        =   1005
      _Version        =   393216
      DTREnable       =   -1  'True
   End
   Begin VB.CommandButton Command1 
      Caption         =   "Test Print (POS Printer)"
      Height          =   855
      Left            =   240
      TabIndex        =   0
      Top             =   240
      Width           =   2895
   End
End
Attribute VB_Name = "VB_Sample"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False

Private Sub Command1_Click()
' for POS Printer
MSComm1.Output = "===================================" + vbCrLf
MSComm1.Output = "====Virtual COM for USB Driver=====" + vbCrLf
MSComm1.Output = vbCrLf
MSComm1.Output = "======Visual Basic Sample Code=====" + vbCrLf
MSComm1.Output = "===================================" + vbCrLf
MSComm1.Output = Chr(&H1D) + Chr(&H56) + Chr(&H41) + Chr(0)
End Sub

Private Sub Command2_Click()
' for Label Printer
MSComm1.Output = "T50,100,3,1,1,0,0,N,N,'==================================='" + vbCrLf
MSComm1.Output = "T50,150,3,1,1,0,0,N,N,'====Virtual COM for USB Driver====='" + vbCrLf
MSComm1.Output = "T50,200,3,1,1,0,0,N,N,'======Visual Basic Sample Code====='" + vbCrLf
MSComm1.Output = "T50,250,3,1,1,0,0,N,N,'==================================='" + vbCrLf
MSComm1.Output = "P1" + vbCrLf
End Sub

Private Sub Form_Load()
Dim Sset$

' Virtual Com port : COM16
On Error GoTo errHed
MSComm1.CommPort = 16

Sset = "115200,n,8,1"
MSComm1.Settings = Sset

MSComm1.RThreshold = 1
MSComm1.InputMode = comInputModeText
MSComm1.PortOpen = True
MSComm1.InputLen = 0

If MSComm1.PortOpen = True Then
    Exit Sub
End If

errHed:
    MsgBox "Open Error"
End Sub

Private Sub Form_Unload(Cancel As Integer)
If MSComm1.PortOpen = True Then
    MSComm1.PortOpen = False
End If
End Sub
