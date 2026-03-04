<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()> _
Partial Class frmMain
    Inherits System.Windows.Forms.Form

    'Form은 Dispose를 재정의하여 구성 요소 목록을 정리합니다.
    <System.Diagnostics.DebuggerNonUserCode()> _
    Protected Overrides Sub Dispose(ByVal disposing As Boolean)
        Try
            If disposing AndAlso components IsNot Nothing Then
                components.Dispose()
            End If
        Finally
            MyBase.Dispose(disposing)
        End Try
    End Sub

    'Windows Form 디자이너에 필요합니다.
    Private components As System.ComponentModel.IContainer

    '참고: 다음 프로시저는 Windows Form 디자이너에 필요합니다.
    '수정하려면 Windows Form 디자이너를 사용하십시오.  
    '코드 편집기를 사용하여 수정하지 마십시오.
    <System.Diagnostics.DebuggerStepThrough()> _
    Private Sub InitializeComponent()
        Me.GroupBox1 = New System.Windows.Forms.GroupBox
        Me.btnDisconnect = New System.Windows.Forms.Button
        Me.btnConnect = New System.Windows.Forms.Button
        Me.txtPrinterName = New System.Windows.Forms.TextBox
        Me.Label1 = New System.Windows.Forms.Label
        Me.GroupBox2 = New System.Windows.Forms.GroupBox
        Me.btnPrint_DeviceFont = New System.Windows.Forms.Button
        Me.cmbDeviceFont = New System.Windows.Forms.ComboBox
        Me.GroupBox3 = New System.Windows.Forms.GroupBox
        Me.rdoCashdrawer_2 = New System.Windows.Forms.RadioButton
        Me.rdoCashdrawer_1 = New System.Windows.Forms.RadioButton
        Me.btnCashdrawer_Open = New System.Windows.Forms.Button
        Me.cmbCashdrawer_Speed = New System.Windows.Forms.ComboBox
        Me.Label2 = New System.Windows.Forms.Label
        Me.GroupBox4 = New System.Windows.Forms.GroupBox
        Me.btnPrint_Receipt = New System.Windows.Forms.Button
        Me.btnPartialCut_NoFeed = New System.Windows.Forms.Button
        Me.btnPartialCut = New System.Windows.Forms.Button
        Me.btnExit = New System.Windows.Forms.Button
        Me.GroupBox1.SuspendLayout()
        Me.GroupBox2.SuspendLayout()
        Me.GroupBox3.SuspendLayout()
        Me.GroupBox4.SuspendLayout()
        Me.SuspendLayout()
        '
        'GroupBox1
        '
        Me.GroupBox1.Controls.Add(Me.btnDisconnect)
        Me.GroupBox1.Controls.Add(Me.btnConnect)
        Me.GroupBox1.Controls.Add(Me.txtPrinterName)
        Me.GroupBox1.Controls.Add(Me.Label1)
        Me.GroupBox1.Location = New System.Drawing.Point(7, 4)
        Me.GroupBox1.Name = "GroupBox1"
        Me.GroupBox1.Size = New System.Drawing.Size(594, 57)
        Me.GroupBox1.TabIndex = 0
        Me.GroupBox1.TabStop = False
        Me.GroupBox1.Text = "Connection"
        '
        'btnDisconnect
        '
        Me.btnDisconnect.Enabled = False
        Me.btnDisconnect.Location = New System.Drawing.Point(461, 18)
        Me.btnDisconnect.Name = "btnDisconnect"
        Me.btnDisconnect.Size = New System.Drawing.Size(126, 31)
        Me.btnDisconnect.TabIndex = 2
        Me.btnDisconnect.Text = "Disconnect Printer"
        Me.btnDisconnect.UseVisualStyleBackColor = True
        '
        'btnConnect
        '
        Me.btnConnect.Location = New System.Drawing.Point(328, 18)
        Me.btnConnect.Name = "btnConnect"
        Me.btnConnect.Size = New System.Drawing.Size(126, 31)
        Me.btnConnect.TabIndex = 2
        Me.btnConnect.Text = "Connect Printer"
        Me.btnConnect.UseVisualStyleBackColor = True
        '
        'txtPrinterName
        '
        Me.txtPrinterName.Location = New System.Drawing.Point(123, 23)
        Me.txtPrinterName.Name = "txtPrinterName"
        Me.txtPrinterName.Size = New System.Drawing.Size(199, 21)
        Me.txtPrinterName.TabIndex = 1
        Me.txtPrinterName.Text = "BIXOLON SRP-275III"
        '
        'Label1
        '
        Me.Label1.AutoSize = True
        Me.Label1.Location = New System.Drawing.Point(12, 25)
        Me.Label1.Name = "Label1"
        Me.Label1.Size = New System.Drawing.Size(105, 15)
        Me.Label1.TabIndex = 0
        Me.Label1.Text = "PRINTER NAME : "
        '
        'GroupBox2
        '
        Me.GroupBox2.Controls.Add(Me.btnPrint_DeviceFont)
        Me.GroupBox2.Controls.Add(Me.cmbDeviceFont)
        Me.GroupBox2.Location = New System.Drawing.Point(10, 81)
        Me.GroupBox2.Name = "GroupBox2"
        Me.GroupBox2.Size = New System.Drawing.Size(325, 85)
        Me.GroupBox2.TabIndex = 1
        Me.GroupBox2.TabStop = False
        Me.GroupBox2.Text = "Device Fonts"
        '
        'btnPrint_DeviceFont
        '
        Me.btnPrint_DeviceFont.Enabled = False
        Me.btnPrint_DeviceFont.Location = New System.Drawing.Point(188, 31)
        Me.btnPrint_DeviceFont.Name = "btnPrint_DeviceFont"
        Me.btnPrint_DeviceFont.Size = New System.Drawing.Size(126, 31)
        Me.btnPrint_DeviceFont.TabIndex = 1
        Me.btnPrint_DeviceFont.Text = "Print Device Font"
        Me.btnPrint_DeviceFont.UseVisualStyleBackColor = True
        '
        'cmbDeviceFont
        '
        Me.cmbDeviceFont.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList
        Me.cmbDeviceFont.Enabled = False
        Me.cmbDeviceFont.FormattingEnabled = True
        Me.cmbDeviceFont.Location = New System.Drawing.Point(14, 35)
        Me.cmbDeviceFont.Name = "cmbDeviceFont"
        Me.cmbDeviceFont.Size = New System.Drawing.Size(165, 23)
        Me.cmbDeviceFont.TabIndex = 0
        '
        'GroupBox3
        '
        Me.GroupBox3.Controls.Add(Me.rdoCashdrawer_2)
        Me.GroupBox3.Controls.Add(Me.rdoCashdrawer_1)
        Me.GroupBox3.Controls.Add(Me.btnCashdrawer_Open)
        Me.GroupBox3.Controls.Add(Me.cmbCashdrawer_Speed)
        Me.GroupBox3.Controls.Add(Me.Label2)
        Me.GroupBox3.Location = New System.Drawing.Point(10, 189)
        Me.GroupBox3.Name = "GroupBox3"
        Me.GroupBox3.Size = New System.Drawing.Size(325, 107)
        Me.GroupBox3.TabIndex = 2
        Me.GroupBox3.TabStop = False
        Me.GroupBox3.Text = "Cash Drawer"
        '
        'rdoCashdrawer_2
        '
        Me.rdoCashdrawer_2.AutoSize = True
        Me.rdoCashdrawer_2.Enabled = False
        Me.rdoCashdrawer_2.Location = New System.Drawing.Point(151, 74)
        Me.rdoCashdrawer_2.Name = "rdoCashdrawer_2"
        Me.rdoCashdrawer_2.Size = New System.Drawing.Size(109, 19)
        Me.rdoCashdrawer_2.TabIndex = 3
        Me.rdoCashdrawer_2.Text = "Cash Drawer-2"
        Me.rdoCashdrawer_2.UseVisualStyleBackColor = True
        '
        'rdoCashdrawer_1
        '
        Me.rdoCashdrawer_1.AutoSize = True
        Me.rdoCashdrawer_1.Checked = True
        Me.rdoCashdrawer_1.Enabled = False
        Me.rdoCashdrawer_1.Location = New System.Drawing.Point(19, 74)
        Me.rdoCashdrawer_1.Name = "rdoCashdrawer_1"
        Me.rdoCashdrawer_1.Size = New System.Drawing.Size(109, 19)
        Me.rdoCashdrawer_1.TabIndex = 3
        Me.rdoCashdrawer_1.TabStop = True
        Me.rdoCashdrawer_1.Text = "Cash Drawer-1"
        Me.rdoCashdrawer_1.UseVisualStyleBackColor = True
        '
        'btnCashdrawer_Open
        '
        Me.btnCashdrawer_Open.Enabled = False
        Me.btnCashdrawer_Open.Location = New System.Drawing.Point(188, 30)
        Me.btnCashdrawer_Open.Name = "btnCashdrawer_Open"
        Me.btnCashdrawer_Open.Size = New System.Drawing.Size(126, 31)
        Me.btnCashdrawer_Open.TabIndex = 2
        Me.btnCashdrawer_Open.Text = "Open Cash Drawer"
        Me.btnCashdrawer_Open.UseVisualStyleBackColor = True
        '
        'cmbCashdrawer_Speed
        '
        Me.cmbCashdrawer_Speed.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList
        Me.cmbCashdrawer_Speed.Enabled = False
        Me.cmbCashdrawer_Speed.FormattingEnabled = True
        Me.cmbCashdrawer_Speed.Location = New System.Drawing.Point(78, 33)
        Me.cmbCashdrawer_Speed.Name = "cmbCashdrawer_Speed"
        Me.cmbCashdrawer_Speed.Size = New System.Drawing.Size(92, 23)
        Me.cmbCashdrawer_Speed.TabIndex = 1
        '
        'Label2
        '
        Me.Label2.AutoSize = True
        Me.Label2.Location = New System.Drawing.Point(15, 36)
        Me.Label2.Name = "Label2"
        Me.Label2.Size = New System.Drawing.Size(52, 15)
        Me.Label2.TabIndex = 0
        Me.Label2.Text = "Speed : "
        '
        'GroupBox4
        '
        Me.GroupBox4.Controls.Add(Me.btnPrint_Receipt)
        Me.GroupBox4.Controls.Add(Me.btnPartialCut_NoFeed)
        Me.GroupBox4.Controls.Add(Me.btnPartialCut)
        Me.GroupBox4.Location = New System.Drawing.Point(350, 81)
        Me.GroupBox4.Name = "GroupBox4"
        Me.GroupBox4.Size = New System.Drawing.Size(249, 215)
        Me.GroupBox4.TabIndex = 3
        Me.GroupBox4.TabStop = False
        '
        'btnPrint_Receipt
        '
        Me.btnPrint_Receipt.Enabled = False
        Me.btnPrint_Receipt.Location = New System.Drawing.Point(33, 144)
        Me.btnPrint_Receipt.Name = "btnPrint_Receipt"
        Me.btnPrint_Receipt.Size = New System.Drawing.Size(183, 42)
        Me.btnPrint_Receipt.TabIndex = 0
        Me.btnPrint_Receipt.Text = "Print Receipt"
        Me.btnPrint_Receipt.UseVisualStyleBackColor = True
        '
        'btnPartialCut_NoFeed
        '
        Me.btnPartialCut_NoFeed.Enabled = False
        Me.btnPartialCut_NoFeed.Location = New System.Drawing.Point(33, 88)
        Me.btnPartialCut_NoFeed.Name = "btnPartialCut_NoFeed"
        Me.btnPartialCut_NoFeed.Size = New System.Drawing.Size(183, 42)
        Me.btnPartialCut_NoFeed.TabIndex = 0
        Me.btnPartialCut_NoFeed.Text = "Partial Cut without Feeding"
        Me.btnPartialCut_NoFeed.UseVisualStyleBackColor = True
        '
        'btnPartialCut
        '
        Me.btnPartialCut.Enabled = False
        Me.btnPartialCut.Location = New System.Drawing.Point(33, 32)
        Me.btnPartialCut.Name = "btnPartialCut"
        Me.btnPartialCut.Size = New System.Drawing.Size(183, 42)
        Me.btnPartialCut.TabIndex = 0
        Me.btnPartialCut.Text = "Partial Cut"
        Me.btnPartialCut.UseVisualStyleBackColor = True
        '
        'btnExit
        '
        Me.btnExit.Location = New System.Drawing.Point(350, 315)
        Me.btnExit.Name = "btnExit"
        Me.btnExit.Size = New System.Drawing.Size(249, 42)
        Me.btnExit.TabIndex = 4
        Me.btnExit.Text = "Exit"
        Me.btnExit.UseVisualStyleBackColor = True
        '
        'frmMain
        '
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.None
        Me.ClientSize = New System.Drawing.Size(613, 368)
        Me.Controls.Add(Me.btnExit)
        Me.Controls.Add(Me.GroupBox4)
        Me.Controls.Add(Me.GroupBox3)
        Me.Controls.Add(Me.GroupBox2)
        Me.Controls.Add(Me.GroupBox1)
        Me.Font = New System.Drawing.Font("Arial", 9.0!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedDialog
        Me.Name = "frmMain"
        Me.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen
        Me.Text = "Sample Program - VB.NET"
        Me.GroupBox1.ResumeLayout(False)
        Me.GroupBox1.PerformLayout()
        Me.GroupBox2.ResumeLayout(False)
        Me.GroupBox3.ResumeLayout(False)
        Me.GroupBox3.PerformLayout()
        Me.GroupBox4.ResumeLayout(False)
        Me.ResumeLayout(False)

    End Sub
    Friend WithEvents GroupBox1 As System.Windows.Forms.GroupBox
    Friend WithEvents btnDisconnect As System.Windows.Forms.Button
    Friend WithEvents btnConnect As System.Windows.Forms.Button
    Friend WithEvents txtPrinterName As System.Windows.Forms.TextBox
    Friend WithEvents Label1 As System.Windows.Forms.Label
    Friend WithEvents GroupBox2 As System.Windows.Forms.GroupBox
    Friend WithEvents btnPrint_DeviceFont As System.Windows.Forms.Button
    Friend WithEvents cmbDeviceFont As System.Windows.Forms.ComboBox
    Friend WithEvents GroupBox3 As System.Windows.Forms.GroupBox
    Friend WithEvents btnCashdrawer_Open As System.Windows.Forms.Button
    Friend WithEvents cmbCashdrawer_Speed As System.Windows.Forms.ComboBox
    Friend WithEvents Label2 As System.Windows.Forms.Label
    Friend WithEvents rdoCashdrawer_2 As System.Windows.Forms.RadioButton
    Friend WithEvents rdoCashdrawer_1 As System.Windows.Forms.RadioButton
    Friend WithEvents GroupBox4 As System.Windows.Forms.GroupBox
    Friend WithEvents btnPrint_Receipt As System.Windows.Forms.Button
    Friend WithEvents btnPartialCut_NoFeed As System.Windows.Forms.Button
    Friend WithEvents btnPartialCut As System.Windows.Forms.Button
    Friend WithEvents btnExit As System.Windows.Forms.Button

End Class
