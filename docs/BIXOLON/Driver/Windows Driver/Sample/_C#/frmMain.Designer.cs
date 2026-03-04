namespace SamplePg_CS
{
    partial class frmMain
    {
        /// <summary>
        /// 필수 디자이너 변수입니다.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// 사용 중인 모든 리소스를 정리합니다.
        /// </summary>
        /// <param name="disposing">관리되는 리소스를 삭제해야 하면 true이고, 그렇지 않으면 false입니다.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form 디자이너에서 생성한 코드

        /// <summary>
        /// 디자이너 지원에 필요한 메서드입니다.
        /// 이 메서드의 내용을 코드 편집기로 수정하지 마십시오.
        /// </summary>
        private void InitializeComponent()
        {
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.btnConnect = new System.Windows.Forms.Button();
            this.btnDisconnect = new System.Windows.Forms.Button();
            this.txtPrinterName = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.groupBox2 = new System.Windows.Forms.GroupBox();
            this.btnPrint_DeviceFont = new System.Windows.Forms.Button();
            this.cmbDeviceFont = new System.Windows.Forms.ComboBox();
            this.groupBox3 = new System.Windows.Forms.GroupBox();
            this.rdoCashdrawer_2 = new System.Windows.Forms.RadioButton();
            this.rdoCashdrawer_1 = new System.Windows.Forms.RadioButton();
            this.btnCashdrawer_Open = new System.Windows.Forms.Button();
            this.cmbCashdrawer_Speed = new System.Windows.Forms.ComboBox();
            this.label2 = new System.Windows.Forms.Label();
            this.groupBox4 = new System.Windows.Forms.GroupBox();
            this.btnPrint_Receipt = new System.Windows.Forms.Button();
            this.btnPartialCut_NoFeed = new System.Windows.Forms.Button();
            this.btnPartialCut = new System.Windows.Forms.Button();
            this.btnExit = new System.Windows.Forms.Button();
            this.groupBox1.SuspendLayout();
            this.groupBox2.SuspendLayout();
            this.groupBox3.SuspendLayout();
            this.groupBox4.SuspendLayout();
            this.SuspendLayout();
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.btnConnect);
            this.groupBox1.Controls.Add(this.btnDisconnect);
            this.groupBox1.Controls.Add(this.txtPrinterName);
            this.groupBox1.Controls.Add(this.label1);
            this.groupBox1.Location = new System.Drawing.Point(10, 18);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(596, 65);
            this.groupBox1.TabIndex = 0;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "Connection";
            // 
            // btnConnect
            // 
            this.btnConnect.Location = new System.Drawing.Point(326, 22);
            this.btnConnect.Name = "btnConnect";
            this.btnConnect.Size = new System.Drawing.Size(124, 32);
            this.btnConnect.TabIndex = 2;
            this.btnConnect.Text = "Connect Printer";
            this.btnConnect.UseVisualStyleBackColor = true;
            this.btnConnect.Click += new System.EventHandler(this.btnConnect_Click);
            // 
            // btnDisconnect
            // 
            this.btnDisconnect.Enabled = false;
            this.btnDisconnect.Location = new System.Drawing.Point(456, 22);
            this.btnDisconnect.Name = "btnDisconnect";
            this.btnDisconnect.Size = new System.Drawing.Size(124, 32);
            this.btnDisconnect.TabIndex = 2;
            this.btnDisconnect.Text = "Disconnect Printer";
            this.btnDisconnect.UseVisualStyleBackColor = true;
            this.btnDisconnect.Click += new System.EventHandler(this.btnDisconnect_Click);
            // 
            // txtPrinterName
            // 
            this.txtPrinterName.Location = new System.Drawing.Point(117, 29);
            this.txtPrinterName.Name = "txtPrinterName";
            this.txtPrinterName.Size = new System.Drawing.Size(198, 21);
            this.txtPrinterName.TabIndex = 1;
            this.txtPrinterName.Text = "BIXOLON SRP-275III";
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(9, 30);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(102, 15);
            this.label1.TabIndex = 0;
            this.label1.Text = "PRINTER NAME :";
            // 
            // groupBox2
            // 
            this.groupBox2.Controls.Add(this.btnPrint_DeviceFont);
            this.groupBox2.Controls.Add(this.cmbDeviceFont);
            this.groupBox2.Location = new System.Drawing.Point(10, 107);
            this.groupBox2.Name = "groupBox2";
            this.groupBox2.Size = new System.Drawing.Size(343, 65);
            this.groupBox2.TabIndex = 1;
            this.groupBox2.TabStop = false;
            this.groupBox2.Text = "Device Fonts";
            // 
            // btnPrint_DeviceFont
            // 
            this.btnPrint_DeviceFont.Enabled = false;
            this.btnPrint_DeviceFont.Location = new System.Drawing.Point(196, 22);
            this.btnPrint_DeviceFont.Name = "btnPrint_DeviceFont";
            this.btnPrint_DeviceFont.Size = new System.Drawing.Size(124, 32);
            this.btnPrint_DeviceFont.TabIndex = 1;
            this.btnPrint_DeviceFont.Text = "Print Device Font";
            this.btnPrint_DeviceFont.UseVisualStyleBackColor = true;
            this.btnPrint_DeviceFont.Click += new System.EventHandler(this.btnPrint_DeviceFont_Click);
            // 
            // cmbDeviceFont
            // 
            this.cmbDeviceFont.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.cmbDeviceFont.Enabled = false;
            this.cmbDeviceFont.FormattingEnabled = true;
            this.cmbDeviceFont.Location = new System.Drawing.Point(21, 27);
            this.cmbDeviceFont.Name = "cmbDeviceFont";
            this.cmbDeviceFont.Size = new System.Drawing.Size(151, 23);
            this.cmbDeviceFont.TabIndex = 0;
            // 
            // groupBox3
            // 
            this.groupBox3.Controls.Add(this.rdoCashdrawer_2);
            this.groupBox3.Controls.Add(this.rdoCashdrawer_1);
            this.groupBox3.Controls.Add(this.btnCashdrawer_Open);
            this.groupBox3.Controls.Add(this.cmbCashdrawer_Speed);
            this.groupBox3.Controls.Add(this.label2);
            this.groupBox3.Location = new System.Drawing.Point(10, 191);
            this.groupBox3.Name = "groupBox3";
            this.groupBox3.Size = new System.Drawing.Size(343, 133);
            this.groupBox3.TabIndex = 2;
            this.groupBox3.TabStop = false;
            this.groupBox3.Text = "Cash Drawers";
            // 
            // rdoCashdrawer_2
            // 
            this.rdoCashdrawer_2.AutoSize = true;
            this.rdoCashdrawer_2.Enabled = false;
            this.rdoCashdrawer_2.Location = new System.Drawing.Point(164, 88);
            this.rdoCashdrawer_2.Name = "rdoCashdrawer_2";
            this.rdoCashdrawer_2.Size = new System.Drawing.Size(109, 19);
            this.rdoCashdrawer_2.TabIndex = 3;
            this.rdoCashdrawer_2.Text = "Cash Drawer-2";
            this.rdoCashdrawer_2.UseVisualStyleBackColor = true;
            // 
            // rdoCashdrawer_1
            // 
            this.rdoCashdrawer_1.AutoSize = true;
            this.rdoCashdrawer_1.Checked = true;
            this.rdoCashdrawer_1.Enabled = false;
            this.rdoCashdrawer_1.Location = new System.Drawing.Point(28, 88);
            this.rdoCashdrawer_1.Name = "rdoCashdrawer_1";
            this.rdoCashdrawer_1.Size = new System.Drawing.Size(109, 19);
            this.rdoCashdrawer_1.TabIndex = 3;
            this.rdoCashdrawer_1.TabStop = true;
            this.rdoCashdrawer_1.Text = "Cash Drawer-1";
            this.rdoCashdrawer_1.UseVisualStyleBackColor = true;
            // 
            // btnCashdrawer_Open
            // 
            this.btnCashdrawer_Open.Enabled = false;
            this.btnCashdrawer_Open.Location = new System.Drawing.Point(196, 40);
            this.btnCashdrawer_Open.Name = "btnCashdrawer_Open";
            this.btnCashdrawer_Open.Size = new System.Drawing.Size(124, 32);
            this.btnCashdrawer_Open.TabIndex = 2;
            this.btnCashdrawer_Open.Text = "Open Cash Drawer";
            this.btnCashdrawer_Open.UseVisualStyleBackColor = true;
            this.btnCashdrawer_Open.Click += new System.EventHandler(this.btnCashdrawer_Open_Click);
            // 
            // cmbCashdrawer_Speed
            // 
            this.cmbCashdrawer_Speed.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.cmbCashdrawer_Speed.Enabled = false;
            this.cmbCashdrawer_Speed.FormattingEnabled = true;
            this.cmbCashdrawer_Speed.Location = new System.Drawing.Point(81, 44);
            this.cmbCashdrawer_Speed.Name = "cmbCashdrawer_Speed";
            this.cmbCashdrawer_Speed.Size = new System.Drawing.Size(91, 23);
            this.cmbCashdrawer_Speed.TabIndex = 1;
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(22, 48);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(52, 15);
            this.label2.TabIndex = 0;
            this.label2.Text = "Speed : ";
            // 
            // groupBox4
            // 
            this.groupBox4.Controls.Add(this.btnPrint_Receipt);
            this.groupBox4.Controls.Add(this.btnPartialCut_NoFeed);
            this.groupBox4.Controls.Add(this.btnPartialCut);
            this.groupBox4.Location = new System.Drawing.Point(369, 107);
            this.groupBox4.Name = "groupBox4";
            this.groupBox4.Size = new System.Drawing.Size(236, 216);
            this.groupBox4.TabIndex = 3;
            this.groupBox4.TabStop = false;
            // 
            // btnPrint_Receipt
            // 
            this.btnPrint_Receipt.Enabled = false;
            this.btnPrint_Receipt.Location = new System.Drawing.Point(21, 150);
            this.btnPrint_Receipt.Name = "btnPrint_Receipt";
            this.btnPrint_Receipt.Size = new System.Drawing.Size(195, 41);
            this.btnPrint_Receipt.TabIndex = 0;
            this.btnPrint_Receipt.Text = "Print Receipt";
            this.btnPrint_Receipt.UseVisualStyleBackColor = true;
            this.btnPrint_Receipt.Click += new System.EventHandler(this.btnPrint_Receipt_Click);
            // 
            // btnPartialCut_NoFeed
            // 
            this.btnPartialCut_NoFeed.Enabled = false;
            this.btnPartialCut_NoFeed.Location = new System.Drawing.Point(21, 91);
            this.btnPartialCut_NoFeed.Name = "btnPartialCut_NoFeed";
            this.btnPartialCut_NoFeed.Size = new System.Drawing.Size(195, 41);
            this.btnPartialCut_NoFeed.TabIndex = 0;
            this.btnPartialCut_NoFeed.Text = "Partial Cut without Feeding";
            this.btnPartialCut_NoFeed.UseVisualStyleBackColor = true;
            this.btnPartialCut_NoFeed.Click += new System.EventHandler(this.btnPartialCut_NoFeed_Click);
            // 
            // btnPartialCut
            // 
            this.btnPartialCut.Enabled = false;
            this.btnPartialCut.Location = new System.Drawing.Point(21, 32);
            this.btnPartialCut.Name = "btnPartialCut";
            this.btnPartialCut.Size = new System.Drawing.Size(195, 41);
            this.btnPartialCut.TabIndex = 0;
            this.btnPartialCut.Text = "Partial Cut";
            this.btnPartialCut.UseVisualStyleBackColor = true;
            this.btnPartialCut.Click += new System.EventHandler(this.btnPartialCut_Click);
            // 
            // btnExit
            // 
            this.btnExit.Location = new System.Drawing.Point(369, 343);
            this.btnExit.Name = "btnExit";
            this.btnExit.Size = new System.Drawing.Size(236, 41);
            this.btnExit.TabIndex = 4;
            this.btnExit.Text = "Exit";
            this.btnExit.UseVisualStyleBackColor = true;
            this.btnExit.Click += new System.EventHandler(this.btnExit_Click);
            // 
            // frmMain
            // 
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.None;
            this.ClientSize = new System.Drawing.Size(618, 406);
            this.Controls.Add(this.btnExit);
            this.Controls.Add(this.groupBox4);
            this.Controls.Add(this.groupBox3);
            this.Controls.Add(this.groupBox2);
            this.Controls.Add(this.groupBox1);
            this.Font = new System.Drawing.Font("Arial", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedDialog;
            this.Name = "frmMain";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Sample Program - C#";
            this.Load += new System.EventHandler(this.frmMain_Load);
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            this.groupBox2.ResumeLayout(false);
            this.groupBox3.ResumeLayout(false);
            this.groupBox3.PerformLayout();
            this.groupBox4.ResumeLayout(false);
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Button btnConnect;
        private System.Windows.Forms.Button btnDisconnect;
        private System.Windows.Forms.TextBox txtPrinterName;
        private System.Windows.Forms.GroupBox groupBox2;
        private System.Windows.Forms.ComboBox cmbDeviceFont;
        private System.Windows.Forms.Button btnPrint_DeviceFont;
        private System.Windows.Forms.GroupBox groupBox3;
        private System.Windows.Forms.RadioButton rdoCashdrawer_1;
        private System.Windows.Forms.Button btnCashdrawer_Open;
        private System.Windows.Forms.ComboBox cmbCashdrawer_Speed;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.RadioButton rdoCashdrawer_2;
        private System.Windows.Forms.GroupBox groupBox4;
        private System.Windows.Forms.Button btnPrint_Receipt;
        private System.Windows.Forms.Button btnPartialCut_NoFeed;
        private System.Windows.Forms.Button btnPartialCut;
        private System.Windows.Forms.Button btnExit;
    }
}

