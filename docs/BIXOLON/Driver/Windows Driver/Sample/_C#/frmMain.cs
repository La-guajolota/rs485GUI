using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Diagnostics;
using System.Runtime.InteropServices;


namespace SamplePg_CS
{
    public partial class frmMain : Form
    {
        //	Cash Draw Speed
        public const int    SPEED_50MS  = 0;
        public const int    SPEED_100MS	= 1;
        public const int    SPEED_150MS	= 2;
        public const int    SPEED_200MS	= 3;
        public const int    SPEED_250MS = 4;

        public frmMain()
        {
            InitializeComponent();
        }

        private void frmMain_Load(object sender, EventArgs e)
        {
            cmbDeviceFont.Items.Clear();

            // FontA
            cmbDeviceFont.Items.Add("FontA1x1");
            cmbDeviceFont.Items.Add("FontA1x1[255]");
            cmbDeviceFont.Items.Add("FontA1x1[Ext.]");
            cmbDeviceFont.Items.Add("FontA1x2");
            cmbDeviceFont.Items.Add("FontA1x2[255]");
            cmbDeviceFont.Items.Add("FontA1x2[Ext.]");
            cmbDeviceFont.Items.Add("FontA2x1");
            cmbDeviceFont.Items.Add("FontA2x1[255]");
            cmbDeviceFont.Items.Add("FontA2x1[Ext.]");
            cmbDeviceFont.Items.Add("FontA2x2");
            cmbDeviceFont.Items.Add("FontA2x2[255]");
            cmbDeviceFont.Items.Add("FontA2x2[Ext.]");

            // FontB
            cmbDeviceFont.Items.Add("FontB1x1");
            cmbDeviceFont.Items.Add("FontB1x1[255]");
            cmbDeviceFont.Items.Add("FontB1x1[Ext.]");
            cmbDeviceFont.Items.Add("FontB1x2");
            cmbDeviceFont.Items.Add("FontB1x2[255]");
            cmbDeviceFont.Items.Add("FontB1x2[Ext.]");
            cmbDeviceFont.Items.Add("FontB2x1");
            cmbDeviceFont.Items.Add("FontB2x1[255]");
            cmbDeviceFont.Items.Add("FontB2x1[Ext.]");
            cmbDeviceFont.Items.Add("FontB2x2");
            cmbDeviceFont.Items.Add("FontB2x2[255]");
            cmbDeviceFont.Items.Add("FontB2x2[Ext.]");

            // Korean fonts
            cmbDeviceFont.Items.Add("Korean1x1");
            cmbDeviceFont.Items.Add("Korean1x2");
            cmbDeviceFont.Items.Add("Korean2x1");
            cmbDeviceFont.Items.Add("Korean2x2");

            // Chinese fonts
            cmbDeviceFont.Items.Add("Chinese2312_1x1");
            cmbDeviceFont.Items.Add("Chinese2312_1x2");
            cmbDeviceFont.Items.Add("Chinese2312_2x1");
            cmbDeviceFont.Items.Add("Chinese2312_2x2");

            cmbDeviceFont.Items.Add("ChineseBIG5_1x1");
            cmbDeviceFont.Items.Add("ChineseBIG5_1x2");
            cmbDeviceFont.Items.Add("ChineseBIG5_2x1");
            cmbDeviceFont.Items.Add("ChineseBIG5_2x2");

            cmbDeviceFont.SelectedIndex = 0;

            // Initialize Cash Drawer Speed
            cmbCashdrawer_Speed.Items.Add("50ms");
            cmbCashdrawer_Speed.Items.Add("100ms");
            cmbCashdrawer_Speed.Items.Add("150ms");
            cmbCashdrawer_Speed.Items.Add("200ms");
            cmbCashdrawer_Speed.Items.Add("250ms");

            cmbCashdrawer_Speed.SelectedIndex = 0;
        }

        private void EnableCtrls(bool bConnect)
        {
            txtPrinterName.Enabled = !bConnect;
            btnConnect.Enabled = !bConnect;

            btnDisconnect.Enabled = bConnect;

            cmbDeviceFont.Enabled = bConnect;
            btnPrint_DeviceFont.Enabled = bConnect;

            cmbCashdrawer_Speed.Enabled = bConnect;
            btnCashdrawer_Open.Enabled = bConnect;
            rdoCashdrawer_1.Enabled = bConnect;
            rdoCashdrawer_2.Enabled = bConnect;

            btnPartialCut.Enabled = bConnect;
            btnPartialCut_NoFeed.Enabled = bConnect;
            btnPrint_Receipt.Enabled = bConnect;
        }

        private void btnConnect_Click(object sender, EventArgs e)
        {
            if( BXLAPI.ConnectPrinter(txtPrinterName.Text.Trim()))
            {
                EnableCtrls(true);
            }
        }

        private void btnDisconnect_Click(object sender, EventArgs e)
        {
            BXLAPI.DisconnectPrinter();
            EnableCtrls(false);
        }

        private void btnCashdrawer_Open_Click(object sender, EventArgs e)
        {
            string strBuffer = "";
            int nPositionX = 0;
            int nPositionY = 0;
            int nTextHeight = 0;

            // Start Document
            if (BXLAPI.Start_Doc("Open Cash Drawer"))
            {
                // Start Page
                BXLAPI.Start_Page();

                switch (cmbCashdrawer_Speed.SelectedIndex)
                {
                    case SPEED_50MS: strBuffer = "a"; break;
                    case SPEED_100MS: strBuffer = "b"; break;
                    case SPEED_150MS: strBuffer = "c"; break;
                    case SPEED_200MS: strBuffer = "d"; break;
                    case SPEED_250MS: strBuffer = "e"; break;
                    default: strBuffer = "f"; break;
                }

                if (rdoCashdrawer_1.Checked)
                    strBuffer = strBuffer.ToUpper();
                else if (rdoCashdrawer_2.Checked)
                    strBuffer = strBuffer.ToLower();

                //Debug.WriteLine("SPEED = " + cmbCashdrawer_Speed.SelectedIndex + ", Buffer = " + strBuffer);

                nPositionY += nTextHeight;
                nTextHeight = BXLAPI.PrintDeviceFont(nPositionX, nPositionY, "FontControl", 9, strBuffer);

                BXLAPI.End_Page();	// End Page
                BXLAPI.End_Doc();	// End Document
            }
        }

        private void btnPrint_DeviceFont_Click(object sender, EventArgs e)
        {
            string strFontName = "";
            string strBuffer = "";
            int nFontSize = 0;
            int nPositionX = 0;
            int nPositionY = 0;

            // Start Document
            if (BXLAPI.Start_Doc("Print Device Font"))
            {
                // Start Page
                BXLAPI.Start_Page();

                //	Get selected font device name
                strFontName = cmbDeviceFont.Text;

                //	Load Font
                nFontSize = 9;

                if (strFontName.IndexOf("Font") >= 0)
                {
                    if (strFontName.IndexOf("x2") >= 0)
                        nFontSize = 18;
                    else
                        nFontSize = 9;
                }
                else
                {
                    if (strFontName.IndexOf("x2") >= 0)
                        nFontSize = 32;
                    else
                        nFontSize = 16;
                }

                strBuffer = "FontName : " + strFontName;
                nPositionY += BXLAPI.PrintDeviceFont(nPositionX, nPositionY, strFontName, nFontSize, strBuffer);

                strBuffer = "TEST";
                nPositionY += BXLAPI.PrintDeviceFont(nPositionX, nPositionY, strFontName, nFontSize, strBuffer);

                BXLAPI.End_Page();	// End Page
                BXLAPI.End_Doc();	// End Document
            }
        }

        private void btnPartialCut_Click(object sender, EventArgs e)
        {
            int nPositionX = 0;
            int nPositionY = 0;
            int nTextHeight = 0;

            // Start Document
            if (BXLAPI.Start_Doc("Partial Cut") == false)
                return;
            // Start Page
            BXLAPI.Start_Page();

            nPositionY += nTextHeight;
            nTextHeight = BXLAPI.PrintDeviceFont(nPositionX, nPositionY, "FontControl", 9, "P");

            BXLAPI.End_Page();	// End Page
            BXLAPI.End_Doc();	// End Document
        }

        private void btnPartialCut_NoFeed_Click(object sender, EventArgs e)
        {
            int nPositionX = 0;
            int nPositionY = 0;
            int nTextHeight = 0;

            // Start Document
            if (BXLAPI.Start_Doc("Partial Cut without Feeding"))
            {
                // Start Page
                BXLAPI.Start_Page();

                nPositionY += nTextHeight;
                nTextHeight = BXLAPI.PrintDeviceFont(nPositionX, nPositionY, "FontControl", 9, "g");

                BXLAPI.End_Page();	// End Page
                BXLAPI.End_Doc();	// End Document
            }
        }

        private void btnPrint_Receipt_Click(object sender, EventArgs e)
        {
            int nPositionX = 0;
            int nPositionY = 0;
            int nTextHeight = 0;

            // Start Document
            if (BXLAPI.Start_Doc("Print Receipt") == false)
                return;
            // Start Page
            BXLAPI.Start_Page();

            nPositionY += nTextHeight;
            nTextHeight = BXLAPI.PrintDeviceFont(nPositionX, nPositionY, "FontControl", 9, "x");		// ALIGNS TEXT TO THE CENTER

            nPositionY += nTextHeight;
            nTextHeight = BXLAPI.PrintDeviceFont(nPositionX, nPositionY, "FontA2x2", 18, "* BIXOLON CAFE *");

            nPositionY += nTextHeight;
            nTextHeight = BXLAPI.PrintDeviceFont(nPositionX, nPositionY, "FontA1x1", 9, "Bundang-gu, Seongam-si");

            nPositionY += nTextHeight;
            nTextHeight = BXLAPI.PrintDeviceFont(nPositionX, nPositionY, "FontA1x1", 9, "Sampyeong-dong, 685");

            nPositionY += nTextHeight;
            nTextHeight = BXLAPI.PrintDeviceFont(nPositionX, nPositionY, "FontA1x1", 9, "Tel) 858-519-3698 Fax) 3852");

            nPositionY += nTextHeight;
            nTextHeight = BXLAPI.PrintDeviceFont(nPositionX, nPositionY, "FontControl", 9, "w");	// ALIGNS TEXT TO THE LEFT

            nPositionY += nTextHeight * 2;
            nTextHeight = BXLAPI.PrintDeviceFont(nPositionX, nPositionY, "FontA1x1", 9, "------------------------------");

            nPositionY += nTextHeight;
            nTextHeight = BXLAPI.PrintDeviceFont(nPositionX, nPositionY, "FontA1x1", 9, "ORANGE                   $3,500");

            nPositionY += nTextHeight;
            nTextHeight = BXLAPI.PrintDeviceFont(nPositionX, nPositionY, "FontA1x1", 9, "BUFALO WING              $3,000");

            nPositionY += nTextHeight;
            nTextHeight = BXLAPI.PrintDeviceFont(nPositionX, nPositionY, "FontA1x1", 9, "POTATO                   $1,200");

            nPositionY += nTextHeight;
            nTextHeight = BXLAPI.PrintDeviceFont(nPositionX, nPositionY, "FontA1x1", 9, "------------------------------");

            nPositionY += nTextHeight;
            nTextHeight = BXLAPI.PrintDeviceFont(nPositionX, nPositionY, "FontA1x1", 9, "Total                    $7,700");

            nPositionY += nTextHeight;
            nTextHeight = BXLAPI.PrintDeviceFont(nPositionX, nPositionY, "FontA1x1", 9, "Tax 6%                     $470");

            nPositionY += nTextHeight;
            nTextHeight = BXLAPI.PrintDeviceFont(nPositionX, nPositionY, "FontA1x1", 9, "Member Discount            $900");

            nPositionY += nTextHeight;
            nTextHeight = BXLAPI.PrintDeviceFont(nPositionX, nPositionY, "FontA1x1", 9, "Money received          $10,000");

            nPositionY += nTextHeight;
            nTextHeight = BXLAPI.PrintDeviceFont(nPositionX, nPositionY, "FontA1x1", 9, "Change                   $2,730");

            nPositionY += nTextHeight;
            nTextHeight = BXLAPI.PrintDeviceFont(nPositionX, nPositionY, "FontA1x1", 9, "------------------------------");

            nPositionY += nTextHeight;
            nTextHeight = BXLAPI.PrintDeviceFont(nPositionX, nPositionY, "FontControl", 9, "x");

            nPositionX = 25;
            nPositionY += nTextHeight / 2;
            nTextHeight = BXLAPI.PrintTrueFont(nPositionX, nPositionY, "Arial", 10, "Member Number : 452331949", false, 0, true, false);

            nPositionY += nTextHeight;
            nTextHeight = BXLAPI.PrintTrueFont(nPositionX, nPositionY, "Arial", 10, "HAVE A NICE DAY!", false, 0, true, false);

            nPositionY += nTextHeight;
            nTextHeight = BXLAPI.PrintTrueFont(nPositionX, nPositionY, "Arial", 10, "Sale Date: 07/01/03", false, 0, true, false);

            nPositionY += nTextHeight;
            nTextHeight = BXLAPI.PrintTrueFont(nPositionX, nPositionY, "Arial", 10, "Time: 12:30:45", false, 0, true, false);

            BXLAPI.End_Page();	// End Page
            BXLAPI.End_Doc();	// End Document
        }

        private void btnExit_Click(object sender, EventArgs e)
        {
            BXLAPI.DisconnectPrinter();

            this.Close();
        }

        
    }
}
